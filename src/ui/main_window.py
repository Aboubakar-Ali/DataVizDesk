import tkinter as tk
from tkinter import Menu, Label, Entry, Button, Frame, messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO
import sys
from pathlib import Path
import sqlite3
import os
from base64 import b64encode

# Add the src directory to sys.path to enable inter-module imports
root_dir = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(root_dir / 'src'))


db_path = 'my_database.db'


# Import
from data.spotify_data_manager import get_spotify_token, find_album_by_artist_and_name


global_album_data = None

import requests

def fetch_album_tracks(album_id, access_token):
    endpoint = f"https://api.spotify.com/v1/albums/{album_id}/tracks"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(endpoint, headers=headers)
    if response.status_code == 200:
        tracks_data = response.json().get('items', [])  
        return tracks_data
    else:
        print(f"Failed to fetch tracks for album {album_id}")
        return []

def search_album_data_callback(artist_name, album_name):
    global global_album_data
    client_id = 'YOUR_CLIENT_ID'
    client_secret = ' YOUR_SECRET_KEY'
    
    access_token = get_spotify_token(client_id, client_secret)
    
    if access_token:
        album_data = find_album_by_artist_and_name(access_token, artist_name, album_name)
        if album_data:
            album_id = album_data['id']
            tracks_data = fetch_album_tracks(album_id, access_token)
            album_data['tracks'] = tracks_data 
            global_album_data = album_data
            display_album_info(album_data)
        else:
            messagebox.showinfo("Info", "Album not found.")
    else:
        messagebox.showerror("Error", "Failed to authenticate with Spotify.")


# Fonction pour afficher les informations de l'album
def display_album_info(album_data):
    artist_name = album_data['artists'][0]['name']  
    album_name = album_data['name']  
    album_cover_url = album_data['images'][0]['url'] 

    # Display the artist and album name
    artist_album_label = Label(window, text=f"Artist: {artist_name}, Album: {album_name}")
    artist_album_label.pack()

    # Download and display the album cover
    response = requests.get(album_cover_url)
    img_data = BytesIO(response.content)
    img = Image.open(img_data)
    img_tk = ImageTk.PhotoImage(img)
    album_cover_label = Label(window, image=img_tk)
    album_cover_label.image = img_tk 
    album_cover_label.pack()

# Window initialization
def init_main_window():
    global window
    window = tk.Tk()
    window.title("DataVizDesk")
    window.geometry("800x600")
    window.resizable(False, False)

   
    menu_bar = Menu(window)
    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Open...")
    file_menu.add_command(label="Save")
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=window.quit)
    menu_bar.add_cascade(label="File", menu=file_menu)

    window.config(menu=menu_bar)

    # wigdets
    add_widgets(window)

    return window 

def download_album_callback():
    global global_album_data
    if global_album_data is None:
        messagebox.showerror("Error", "No album data to download.")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Check if the album is already in the database
    album_name = global_album_data['name']
    cursor.execute("SELECT id FROM albums WHERE name = ?", (album_name,))
    album = cursor.fetchone()

    if album:
        messagebox.showinfo("Info", "This album is already in your database.")
        conn.close()  
        return
    else:
        # Insert the artist into the database
        for artist in global_album_data['artists']:
            artist_name = artist['name']
            cursor.execute("INSERT OR IGNORE INTO artists (name) VALUES (?)", (artist_name,))
            cursor.execute("SELECT id FROM artists WHERE name = ?", (artist_name,))
            artist_id = cursor.fetchone()[0]

        # Insert the album into the database
        album_name = global_album_data['name']
        album_cover_url = global_album_data['images'][0]['url']
        cursor.execute("INSERT INTO albums (artist_id, name, cover_url) VALUES (?, ?, ?)", (artist_id, album_name, album_cover_url))
        album_id = cursor.lastrowid

        # Insert the songs into the database
        for track in global_album_data.get('tracks', []):
            song_name = track['name']
            duration_ms = track.get('duration_ms', 0)  
            cursor.execute("INSERT INTO songs (name, duration_ms) VALUES (?, ?)", (song_name, duration_ms))


        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Album downloaded successfully.")


def create_tables():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS artists (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS albums (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        artist_id INTEGER,
        name TEXT NOT NULL,
        cover_url TEXT,
        FOREIGN KEY (artist_id) REFERENCES artists (id)
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS songs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        duration_ms INTEGER
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS songs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    duration_ms INTEGER  
    );
    ''')

    conn.commit()
    conn.close()

    



def add_widgets(window):
    control_frame = Frame(window)
    control_frame.pack(fill='x', padx=5, pady=5)
    artist_label = Label(control_frame, text="Artist Name:")
    artist_label.pack(side='left')

    artist_entry = Entry(control_frame)
    artist_entry.pack(side='left', fill='x', expand=True)

    album_label = Label(control_frame, text="Album Name:")
    album_label.pack(side='left')

    album_entry = Entry(control_frame)
    album_entry.pack(side='left', fill='x', expand=True)

    search_button = Button(control_frame, text="Search Album", command=lambda: search_album_data_callback(artist_entry.get(), album_entry.get()))
    search_button.pack(side='right')

    # Ajout du bouton de téléchargement
    download_button = Button(control_frame, text="Download Album", command=download_album_callback)
    download_button.pack(side='right')

if __name__== "__main__":
    create_tables() 
    main_window = init_main_window()
    main_window.mainloop()
    
