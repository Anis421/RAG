import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
# import re
from youtube_search import YoutubeSearch



load_dotenv()
imdb_api_key = os.getenv('API_KEY')

# def google(query):
#     url = f"https://www.google.com/search?q={query}"
#     headers = {"User-Agent": "Mozilla/5.0"}
#     response = requests.get(url, headers = headers, timeout = 10)
#     soup = BeautifulSoup(response.text, "html.parser")
#
#     for link in soup.find_all("a", href=True):
#         if "url?q=" in link["href"]:
#             return link["href"].split("url?q=")[1].split("&")[0]
#     return "No results found."

def omdb(movie_name):
    url = f"https://www.omdbapi.com/?t={movie_name}&apikey={imdb_api_key}"
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

# def youtube(query):
#     url = f"https://www.youtube.com/results?search_query={query}"
#     headers = {"User-Agent": "Mozilla/5.0"}
#     response = requests.get(url, headers = headers, timeout = 10)
#
#     video_ids = re.findall(r'"videoId":"([a-zA-Z0-9_-]{11})"', response.text)
#     if video_ids:
#         return f"https://www.youtube.com/watch?v={video_ids[0]}"
#     return "No results found."


def youtube(query):
    results = YoutubeSearch(f"{query} trailer", max_results=1).to_dict()
    trailer_url = f"https://youtube.com/watch?v={results[0]['id']}"
    return trailer_url

def youtube_trailer(movie_name):
    query = f"{movie_name} official trailer"
    # query = f"https://www.youtube.com/results?search_query={movie_name}"
    return youtube(query)
