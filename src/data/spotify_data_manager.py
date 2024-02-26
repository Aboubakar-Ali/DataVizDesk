import requests
from base64 import b64encode

def get_spotify_token(client_id, client_secret):
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + b64encode(f"{client_id}:{client_secret}".encode()).decode(),
        "Content-Type": "application/x-www-form-urlencoded"
    }
    body = {"grant_type": "client_credentials"}

    response = requests.post(url, headers=headers, data=body)
    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        print("Failed to get token:", response.text)
        return None


def search_for_artist(access_token, artist_name):
    endpoint = f"https://api.spotify.com/v1/search?q={artist_name}&type=artist&limit=1"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(endpoint, headers=headers)
    if response.status_code == 200:
        results = response.json()['artists']['items']
        if results:
            return results[0]['id'] 
    return None


def find_album_by_artist_and_name(access_token, artist_name, album_name):
    # Search for the artist ID
    search_artist_url = f"https://api.spotify.com/v1/search?q={artist_name}&type=artist"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(search_artist_url, headers=headers)
    if response.status_code != 200:
        print("Failed to search for artist:", response.text)
        return None
    artists_data = response.json()
    if not artists_data['artists']['items']:
        print("Artist not found")
        return None
    artist_id = artists_data['artists']['items'][0]['id']

    # Search for the album by artist ID and album name
    search_album_url = f"https://api.spotify.com/v1/artists/{artist_id}/albums?include_groups=album,single&market=US"
    response = requests.get(search_album_url, headers=headers)
    if response.status_code != 200:
        print("Failed to search for albums:", response.text)
        return None
    albums_data = response.json()
    for album in albums_data['items']:
        if album['name'].lower() == album_name.lower():
            return album  

    print("Album not found")
    return None
