from django.shortcuts import render
import os
from dotenv import load_dotenv
import requests

load_dotenv()

TMDB_API_KEY = os.environ.get("TMDB_SECRET_KEY")

# Create your views here.

def home(request):
    return render(request, 'home.html')

def Kamal(request):
    actor_id = 93193
    api_url = f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_people={actor_id}&sort_by=popularity.desc&page=1"

    try:
        response = requests.get(api_url)
        response.raise_for_status()  
        data = response.json()
        movies = data['results']  
        processed_movies = [
            {
                'title': movie['title'],
                # 'genres': ', '.join(movie['genres']),
                'poster_path': movie['poster_path'],
                'average_vote': movie['vote_average'],
            }
            for movie in movies
        ]
 
        return render(request, 'kamal.html', {'movies': processed_movies})
    except requests.exceptions.RequestException as e:
        
        return render(request, 'kamal.html', {'error_message': str(e)})