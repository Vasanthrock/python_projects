from pprint import pprint

import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

URL = "https://www.billboard.com/charts/hot-100/"
date = input("which year you would like to travel? Type the date in this format YYYY-MM-DD: ")


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
response = requests.get(url = URL+date, headers = headers)
response.raise_for_status()
data= response.text


soup = BeautifulSoup(data,"html.parser")
songs = soup.select("li ul li h3")
song_list = [song.get_text().strip() for song in songs]
print(song_list)



sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id= os.getenv("client_id"),
        client_secret= os.getenv("client_secret"),
        show_dialog=True,
        cache_path="token.txt",
        username= "Rock",
    )
)

user_id = sp.current_user()["id"]


song_uri = []
year = date.split("-")[0]

for song in song_list:
    result = sp.search(q=f"track: {song} year: {year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uri.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date}Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uri)