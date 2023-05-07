import requests

api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjY2NlNjVjZTA2OWUyMjA0ZmFhMzFmZmY2ZDNkYzVmZiIsInN1YiI6IjY0MmMzNGJmYzA0NDI5MDFmMDAzYmFkMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.1BwAwv6HS7rMSkH7DiyDCj1Hbs8jPQPF74cgLLXusBI"
api_key = "ccce65ce069e2204faa31fff6d3dc5ff"


def get_popular_movies(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {"Authorization": f"Bearer {api_token}"}
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {"Authorization": f"Bearer {api_token}"}
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {"Authorization": f"Bearer {api_token}"}
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]


def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {"Authorization": f"Bearer {api_token}"}
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()


def get_movies(how_many, list_type):
    data = get_popular_movies(list_type)
    return data["results"][:how_many]


import requests
from requests.exceptions import HTTPError


import requests

api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjY2NlNjVjZTA2OWUyMjA0ZmFhMzFmZmY2ZDNkYzVmZiIsInN1YiI6IjY0MmMzNGJmYzA0NDI5MDFmMDAzYmFkMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.1BwAwv6HS7rMSkH7DiyDCj1Hbs8jPQPF74cgLLXusBI"
api_key = "ccce65ce069e2204faa31fff6d3dc5ff"


def get_popular_movies(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {"Authorization": f"Bearer {api_token}"}
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {"Authorization": f"Bearer {api_token}"}
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {"Authorization": f"Bearer {api_token}"}
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]


def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {"Authorization": f"Bearer {api_token}"}
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()


def get_movies(how_many, list_type):
    data = get_popular_movies(list_type)
    return data["results"][:how_many]


import requests
from requests.exceptions import HTTPError


def call_tmdb_api(endpoint):
    api_key = "ccce65ce069e2204faa31fff6d3dc5ff"
    url = f"https://api.themoviedb.org/3/{endpoint}"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {api_key}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except Exception as err:
        print(f"Other error occurred: {err}")
        return None

    return response.json()
