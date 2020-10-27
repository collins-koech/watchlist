import urllib.request,json
from .models import Movie

# Getting api key
api_key = '74ae3b3698d4de9e18b4b5e5afe35f45'
# Getting the movie base url
base_url = 'https://api.themoviedb.org/3/movie/550?api_key=74ae3b3698d4de9e18b4b5e5afe35f45'

def configure_request(app):
    global api_key,base_url
    api_key = app.config['74ae3b3698d4de9e18b4b5e5afe35f45']
    base_url = app.config['https://api.themoviedb.org/3/movie/550?api_key=74ae3b3698d4de9e18b4b5e5afe35f45']