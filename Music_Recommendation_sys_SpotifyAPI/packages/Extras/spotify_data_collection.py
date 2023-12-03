import pandas as pd
import spotipy
import authentication

from spotipy.oauth2 import SpotifyOAuth

def get_trending_playlist(playlist_id, access_token):
    # setup spotify with access token
    sp = spotipy.Spotify(auth=access_token)

    # Getting tracks 
    play_tracks = sp.playlist_tracks(playlist_id,fields='items(track(id,name,artists,albums(id,name)))')

    # Extracting data #
    music_data =[]

    for tracks_info in play_tracks['items']:
        track =tracks_info['track']
        track_name = track['name']
        artists = ','.join([artist['name'] for artist in track['artists']])
        album_name = track['album']['name']
        album_id = track['album']['id']
        track_id = track['id']
    music_data.append(tracks_info)
    return music_data