# IMPORT MODULES
import os, sys, json
os.chdir('/Users/kimdohoon/git/Spotify-Playground/spotify-API')
lib_dir = f"{os.getcwd()}/Airflow/sample_hooniegit/lib"
sys.path.append(lib_dir)
import spotipy_modules as lib_spotify

# VARIABLES
DIRECTORY_playlist = f'{os.getcwd()}/Airflow/sample_hooniegit/datas/JSON/playlists'
DIRECTORY_wishlist = f'{os.getcwd()}/Airflow/sample_hooniegit/datas/wishlists/playlists.json'
print(f"DIRECTORY_PLAYLIST : {DIRECTOR dY_playlist}")

# PLAYLISTS
with open(DIRECTORY_wishlist, 'r') as file:
    playlists_json = json.load(file)
playlists = playlists_json['playlists']

# LIB : MAKE PLAYLIST JSON DATAS
for playlist_id in playlists:
    lib_spotify.get_playlist(playlist_id, True, DIRECTORY_playlist)