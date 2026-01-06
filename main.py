import json
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# DATE = input(Which year would you like to travel to? --> Type the date in this format YYYY-MM-DD):)
DATE = "2026-01-03"
year = DATE.split("-")[0]

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"}


url = "https://www.billboard.com/charts/hot-100/"  # +DATE
response = requests.get(url=url, headers=header)


soup = BeautifulSoup(response.content, "html.parser")
song_list = [song.getText().strip() for song in soup.select("li ul li h3")]

with open("song_list.json", "w", encoding="utf-8") as file:
    json.dump(song_list, file, indent=4)

# SPOTIFY AUTHENTICATION (OAuth)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

# Load Song list
with open("song_list.json", "r", encoding="utf-8") as file:
    song_names = json.load(file)

# search each song in spotify:

song_uris = []

for song in song_names:
    result = sp.search(
        q=f"track:{song} year:{year}",
        type="track",
        limit=1
    )

    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} not found on Spotify. Skipped.")

# CREATE SPOTIFY PLAYLIST

playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{DATE} Billboard Hot 100",
    public=False
)

# add songs to playlist:
sp.playlist_add_items(
    playlist_id=playlist["id"],
    items=song_uris
)
