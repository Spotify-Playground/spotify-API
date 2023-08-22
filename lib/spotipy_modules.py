# IMPORT MODULES
import spotipy, json
from spotipy.oauth2 import SpotifyClientCredentials

# MODULE : connect spotify
def connect_spotify():
    client_id = '3d918c9fcbe44e099ba189c46cdedd8d'
    client_secret = '9c1ff7f73f4b424ebaf54977cde68f83'
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, \
                                                          client_secret=client_secret)
    global sp
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# MODULE : dump JSON
def dump_json(data, filename, DIRECTORY):
    with open(f"{DIRECTORY}/{filename}.json", "w") as file:
        json.dump(data, file, indent=4)

# MODULE : get playlist
def get_playlist(playlist_id, dump=False, DIRECTORY=None):
    connect_spotify()
    playlist = sp.playlist(playlist_id)
    playlist_name = playlist['name']
    if dump == True:
        dump_json(playlist, playlist_name, DIRECTORY)
        print(f"{playlist_name} dump completed")
    return playlist

# MODULE : search artist
def search_artist(artist_name, dump=False, DIRECTORY=None):
    connect_spotify()
    artist_info = sp.search(artist_name, type='artist')
    if dump == True:
        dump_json(artist_info, artist_name, DIRECTORY)
        print(f"{artist_name} info dump completed")
    return artist_info

# MODULE : search artist albums
def search_artist_albums(artist_name, dump=False, DIRECTORY=None):
    artist_info = search_artist(artist_name)
    artist_id = artist_info['artists']['items'][0]['id']
    artist_album_info = sp.artist_albums(artist_id)
    if dump == True:
        dump_json(artist_album_info, artist_name, DIRECTORY)
        print(f"{artist_name} albums dump completed")
    return artist_album_info

# MODULE + 개인기록들

# TEST
if __name__ == "__main__":
    pass
