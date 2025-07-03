import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ['Utelly_API']   # your RapidAPI key
LOOKUP_URL = "https://utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com/lookup"

def get_movie_provider(movie_title: str, country: str = "us"):
    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com"
    }
    params = {
        "term": movie_title,
        "country": country
    }

    resp = requests.get(LOOKUP_URL, headers=headers, params=params)
    if resp.status_code != 200:
        return {"error": f"Utelly API returned {resp.status_code}"}

    data = resp.json().get("results")
    if not data:
        return {"error": "No results from Utelly"}

    locations = data[0].get("locations", [])
    providers = [loc.get("display_name") for loc in locations if loc.get("display_name")]

    if not providers:
        return {"error": "No streaming providers found"}

    return {"provider": ", ".join(providers)}
