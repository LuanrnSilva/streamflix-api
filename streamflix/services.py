import requests

TMDB_API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxODVmYTVkNmY5M2UwODJlMWMzYjkyYTU5MzgyZTYxOCIsIm5iZiI6MTczNzUwNjA0MC43MTIsInN1YiI6IjY3OTAzY2Y4YmU5YTlhYTc4Mjc3NDA5MCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Jkkt9V0WEXsWNVmQjx7QJeyYmvrBlKxyfPCYUjbAcfM";  # coloque a sua

class TMDBService:
    BASE = "https://api.themoviedb.org/3/movie/"

    @classmethod
    def fetch_movie(cls, tmdb_id):
        url = f"{cls.BASE}{tmdb_id}"

        resp = requests.get(url, 
            headers={
                "Authorization": f"Bearer {TMDB_API_KEY}", 
            },
            params={
                "language": "pt-BR"
            }
        )
        resp.raise_for_status()
        return resp.json()