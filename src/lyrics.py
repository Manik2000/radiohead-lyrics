import pandas as pd
import json
from lyricsgenius import Genius


def get_genius_searcher(API_key):
    return Genius(API_key,
                  verbose=False, 
                  remove_section_headers=True,
                  skip_non_songs=True, 
                  timeout=10
                  )


def get_artist_songs(genius_searcher, artist_name):
    artist = genius_searcher.search_artist(artist_name, sort='popularity')
    return artist.songs


def extract_songs_details(song):
    album = song._body['album']
    return {
        'title': song.title,
        'album': album['name'] if album else None,
        'release_date': song._body['release_date'],
        'lyrics': song.lyrics
    }

def get_songs_details(songs):
    return list(map(extract_songs_details, songs))


def get_df_of_lyrics(songs_details):
    return pd.DataFrame(songs_details)

def get_artist_songs_df(genius_searcher, artist_name):
    songs = get_artist_songs(genius_searcher, artist_name)
    songs_details = get_songs_details(songs)
    return get_df_of_lyrics(songs_details)
