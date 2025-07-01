
# tmdb_api.py - TMDB API

import requests
from dotenv import load_dotenv
import os

load_dotenv()

TMDB_API_KEY = os.environ['TMDB_API_KEY']
TMDB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"

def get_movie_details(movie_title):
    params = {
        'api_key': TMDB_API_KEY,
        'query': movie_title
    }

    response = requests.get(TMDB_SEARCH_URL, params=params)

    if response.status_code == 200 and response.json()['results']:
        movie = response.json()['results'][0]
        poster_path = movie.get('poster_path')
        poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else "No poster available"
        return {
            'title': movie.get('title'),
            'release_date': movie.get('release_date'),
            'rating': movie.get('vote_average'),
            'overview': movie.get('overview'),
            'poster_url': poster_url
        }
    else:
        return {'error': 'Movie not found on TMDB.'}
