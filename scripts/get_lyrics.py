import os

import yaml
from dotenv import load_dotenv

from src.lyrics import get_artist_songs_df, get_genius_searcher


load_dotenv()

with open("config.yaml", 'r') as stream:
    config = yaml.safe_load(stream)

artist = config['lyrics']['artist']

genius = get_genius_searcher(os.getenv("GENIUS_API_KEY"))

df = get_artist_songs_df(genius, artist)
df.to_csv(os.path.join('data', config["lyrics"]["output"]), index=False)
