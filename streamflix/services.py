import requests

TMDB_API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxODVmYTVkNmY5M2UwODJlMWMzYjkyYTU5MzgyZTYxOCIsIm5iZiI6MTczNzUwNjA0MC43MTIsInN1YiI6IjY3OTAzY2Y4YmU5YTlhYTc4Mjc3NDA5MCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Jkkt9V0WEXsWNVmQjx7QJeyYmvrBlKxyfPCYUjbAcfM"

class TMDBService:
    @classmethod
    def fetch_content(cls, tmdb_id):
        headers = {"Authorization": f"Bearer {TMDB_API_KEY}"}
        params = {"language": "pt-BR"}

        resp = requests.get(f"https://api.themoviedb.org/3/movie/{tmdb_id}", headers=headers, params=params)
        if resp.status_code == 200:
            return resp.json()

        resp = requests.get(f"https://api.themoviedb.org/3/tv/{tmdb_id}", headers=headers, params=params)
        if resp.status_code == 200:
            return resp.json()

        resp.raise_for_status()