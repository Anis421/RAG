import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
from youtube_search import YoutubeSearch


load_dotenv()
imdb_api_key = os.getenv('API_KEY')

def omdb(movie_name):
    url = f"https://www.omdbapi.com/?t={movie_name} & apikey = {imdb_api_key}"
    response = requests.get(url)
    data = response.json()

    if data["Response"] == "True":
        return {
            "Title": data["Title"],
            "Year": data["Year"],
            "IMDb Rating": data["imdbRating"],
            "Plot": data["Plot"]
        }
    return "Movie not found."

def youtube(query):
    results = YoutubeSearch(f"{query} trailer", max_results=1).to_dict()
    trailer_url = f"https://youtube.com/watch?v={results[0]['id']}"
    return trailer_url

def youtube_trailer(movie_name):
    query = f"{movie_name} official trailer"
    # query = f"https://www.youtube.com/results?search_query={movie_name}"
    return youtube(query)
