from urllib.parse import urlencode, quote
from collections import OrderedDict
from dotenv import load_dotenv
import os
load_dotenv()

def generate_spotify_auth_url ():     
    SPOTIFY_AUTH_URL = os.getenv('SPOTIFY_AUTH_URL')
    SPOTIFY_CLIENT_ID=os.getenv('SPOTIFY_CLIENT_ID')
    SPOTIFY_CLIENT_SECRET=os.getenv('SPOTIFY_CLIENT_SECRET')
    SPOTIFY_REDIRECT_URI=os.getenv('SPOTIFY_REDIRECT_URI')
    query_string = urlencode(OrderedDict(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET, redirect_uri=SPOTIFY_REDIRECT_URI, response_type='code',))
    url = '{spotify_url}?'.format(spotify_url=SPOTIFY_AUTH_URL) + query_string 
    return url