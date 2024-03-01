# image.py
from tkinter import Label, Entry, Button, Toplevel, messagebox
from PIL import Image
import requests
from io import BytesIO
import os

def download_and_show_image(window):
    def download_and_fill_crop_area():
        image_url = url_entry.get()
        crop_width = int(width_entry.get())
        crop_height = int(height_entry.get())

        response = requests.get(image_url)
        if response.status_code == 200:
            img = Image.open(BytesIO(response.content))

            # Redimensionnement et recadrage
            img_ratio = img.width / img.height
            desired_ratio = crop_width / crop_height
            if img_ratio > desired_ratio:
                new_height = crop_height
                new_width = int(new_height * img_ratio)
            else:
                new_width = crop_width
                new_height = int(new_width / img_ratio)
            
            img_resized = img.resize((new_width, new_height), Image.LANCZOS)

            start_x = (new_width - crop_width) // 2
            start_y = (new_height - crop_height) // 2
            img_cropped = img_resized.crop((start_x, start_y, start_x + crop_width, start_y + crop_height))

            # Définir le chemin de sauvegarde et créer le dossier s'il n'existe pas
            save_directory = 'Data Explorration/Image'
            if not os.path.exists(save_directory):
                os.makedirs(save_directory)
            save_path = os.path.join(save_directory, 'downloaded_image.jpg')

            # Sauvegarder l'image
            img_cropped.save(save_path)
            messagebox.showinfo("Image Téléchargée", f"L'image a été téléchargée avec succès et enregistrée sous {save_path}.")
        else:
            messagebox.showerror("Erreur", "Impossible de télécharger l'image.")

    download_window = Toplevel(window)
    download_window.title("Télécharger Image")

    Label(download_window, text="URL de l'image:").pack()
    url_entry = Entry(download_window, width=50)
    url_entry.pack()

    Label(download_window, text="Largeur de recadrage:").pack()
    width_entry = Entry(download_window, width=50)
    width_entry.pack()

    Label(download_window, text="Hauteur de recadrage:").pack()
    height_entry = Entry(download_window, width=50)
    height_entry.pack()

    Button(download_window, text="Télécharger et recadrer", command=download_and_fill_crop_area).pack()

