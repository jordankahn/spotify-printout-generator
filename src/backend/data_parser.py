'''This class parses retrieved Spotify API data for both playlists and albums'''
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import qrcode
import PIL as pillow
import re

os.environ["SPOTIPY_CLIENT_ID"] = '19d46d1de89a44c9813248a047e1788f'
os.environ["SPOTIPY_CLIENT_SECRET"] = 'bdffc7ce17c34d2fb13883afb54d7cf2'

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)


def get_playlist_id(playlist_url):
    result = re.search('playlist/(.*)', playlist_url)
    get_id = result.group(1).split('?')[0]
    playlist_id = 'spotify:playlist:' + get_id
    return playlist_id


def get_album_id(album_url):
    result = re.search('album/(.*)', album_url)
    get_id = result.group(1).split('?')[0]
    album_id = 'spotify:album:' + get_id
    return album_id


def get_playlist_title(playlist_id):
    results = sp.playlist(playlist_id)
    return results["name"]


def get_album_title(album_id):
    results = sp.album(album_id)
    artist_name = results["artists"][0]["name"]
    return artist_name + " - " + results["name"]


def get_playlist_songs(playlist_id):
    results = sp.user_playlist_tracks("officialboxout", playlist_id)
    parsed_songs = []
    for i, item in enumerate(results['items']):
        track = item['track']
        parsed_songs.append(track['artists'][0]
                            ['name'] + " - " + track['name'])
    return parsed_songs


def get_album_songs(album_id):
    results = sp.album(album_id)
    song_list = results["tracks"]["items"]
    parsed_songs = []
    for i in range(len(song_list)):
        parsed_songs.append(song_list[i]["name"])
    return parsed_songs


def get_playlist_image(playlist_id):
    return sp.playlist_cover_image(playlist_id)[0]["url"]


def get_album_image(album_id):
    return sp.album(album_id)["images"][0]["url"]


def generate_qr_code(playlist_url):
    qr_code = qrcode.make(playlist_url)
    qr_code.save('../SpotifyPrintoutGenerator/qr_codes/code.jpg')


def route_album_or_playlist(url):
    if url.find("playlist") != -1:
        generate_qr_code(url)
        playlist_id = get_playlist_id(url)
        return {"type": "playlist",
                "title": get_playlist_title(playlist_id),
                "songs": get_playlist_songs(playlist_id),
                "image": get_playlist_image(playlist_id)}
    elif url.find("album") != -1:
        generate_qr_code(url)
        album_id = get_album_id(url)
        return {"type": "album",
                "title": get_album_title(album_id),
                "songs": get_album_songs(album_id),
                "image": get_album_image(album_id)}
    else:
        return {"error": "Given URL is not for a Spotify album or playlist"}


def main():
    print("Enter a playlist or album")
    url = input()
    print(route_album_or_playlist(url))


if __name__ == "__main__":
    main()
