from django.shortcuts import render
import os
from dotenv import load_dotenv
import requests
from .helpers import drop_decimal_but_first

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
                'average_vote': drop_decimal_but_first(movie['vote_average']),
            }
            for movie in movies
        ]
 
        return render(request, 'kamal.html', {'movies': processed_movies})
    except requests.exceptions.RequestException as e:
        
        return render(request, 'kamal.html', {'error_message': str(e)})
    
def dhanush(request):
    actor_id = 550165
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
                'average_vote': drop_decimal_but_first(movie['vote_average']),
            }
            for movie in movies
        ]
 
        return render(request, 'dhanush.html', {'movies': processed_movies})
    except requests.exceptions.RequestException as e:
        
        return render(request, 'dhanush.html', {'error_message': str(e)})
    
def vikram(request):
    actor_id = 93191
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
                'average_vote': drop_decimal_but_first(movie['vote_average']),
            }
            for movie in movies
        ]
 
        return render(request, 'vikram.html', {'movies': processed_movies})
    except requests.exceptions.RequestException as e:
        
        return render(request, 'vikram.html', {'error_message': str(e)})
    
def vijay_sethupathi(request):
    actor_id = 1123766
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
                'average_vote': drop_decimal_but_first(movie['vote_average']),
            }
            for movie in movies
        ]
 
        return render(request, 'vijaysethupathi.html', {'movies': processed_movies})
    except requests.exceptions.RequestException as e:
        
        return render(request, 'vijaysethupathi.html', {'error_message': str(e)})