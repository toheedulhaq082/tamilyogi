from django.shortcuts import render
import os
from dotenv import load_dotenv
import requests
from .helpers import drop_decimal_but_first, get_language_full_name
from .models import BlogModel
from django.views.generic import TemplateView
from django.http import Http404
from django.utils.text import slugify
from django.http import HttpResponse
from .movies_lists import (
    action_movies, thriller_movies, crime_movies,
    drama_movies, romance_movies, comedy_movies, adventure_movies
)


load_dotenv()

TMDB_API_KEY = os.environ.get("TMDB_SECRET_KEY")

GENRE_MAP = {
    28: 'Action',
    80: 'Crime',
    18: 'Drama',
    53: 'Thriller',
    12: 'Adventure',
    16: 'Animation',
    35: 'Comedy',
    14: 'Fantasy',
    27: 'Horror',
    36: 'History',
    10402: 'Music',
    99: 'Documentary',
    878: 'Science Fiction',
    10751: 'Family',
    10749: 'Romance',
    10752: 'War',
    37: 'Western'
}

# Create your views here.

def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow:",
        "Sitemap: https://tamilyogi.moviechoose.com/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

def homepage(request):
    return render(request, 'home.html', {
        'action_movies': action_movies,
        # 'thriller_movies': thriller_movies,
        # 'crime_movies': crime_movies,
        # 'drama_movies': drama_movies,
        # 'romance_movies': romance_movies,
        # 'comedy_movies': comedy_movies,
        # 'adventure_movies': adventure_movies,
    })
    


def blog_detail(request, slug):
    context = {}
    try:
        blog_obj = BlogModel.objects.filter(slug=slug).first() 
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'blog_detail.html', context=context)

def anime(request):
    genre_id = 16  # Genre ID for 'Animation' which often includes anime
    # api_url = f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_genres={genre_id}&sort_by=popularity.desc&page=1"
    api_url = f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_genres={genre_id}&with_original_language=ja&sort_by=popularity.desc&page=1"

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for 4xx/5xx responses
        data = response.json()
        movies = data['results']  # Extract the list of anime movies from the response
        processed_movies = [
            {
                'title': movie['title'],
                'poster_path': movie['poster_path'],  # Poster image for the movie
                'average_vote': drop_decimal_but_first(movie['vote_average']),  # Format the average vote
            }
            for movie in movies
        ]

        return render(request, 'anime.html', {'movies': processed_movies})  # Render the movies in the template
    except requests.exceptions.RequestException as e:
        return render(request, 'anime.html', {'error_message': str(e)})  # Render an error message in the template
    

def Kamal(request):
    actor_id = 93193
    api_url = f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_people={actor_id}&sort_by=popularity.desc&page=1"

    try:
        response = requests.get(api_url)
        response.raise_for_status()  
        data = response.json()
        movies = data['results']  
        
        processed_movies = []

        for movie in movies:
            # Extract the first genre ID
            first_genre_id = movie.get('genre_ids', [])[0] if movie.get('genre_ids') else None

            # Get the genre name using the GENRE_MAP (or another API call if you prefer)
            first_genre_name = GENRE_MAP.get(first_genre_id, 'Unknown Genre')

            processed_movies.append({
                'id': movie['id'],
                'title': movie['title'],
                'slug': slugify(movie['title']),
                'poster_path': movie['poster_path'],
                'average_vote': drop_decimal_but_first(movie['vote_average']),
                'genre': first_genre_name,  # Add the genre name here
            })

        return render(request, 'Kamal.html', {'movies': processed_movies})
    except requests.exceptions.RequestException as e:
        return render(request, 'Kamal.html', {'error_message': str(e)})
    
def dhanush(request):
    actor_id = 550165
    api_url = f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_people={actor_id}&sort_by=popularity.desc&page=1"

    try:
        response = requests.get(api_url)
        response.raise_for_status()  
        data = response.json()
        movies = data['results']  
        
        processed_movies = []

        for movie in movies:
            # Extract the first genre ID
            first_genre_id = movie.get('genre_ids', [])[0] if movie.get('genre_ids') else None

            # Get the genre name using the GENRE_MAP (or another API call if you prefer)
            first_genre_name = GENRE_MAP.get(first_genre_id, 'Unknown Genre')

            processed_movies.append({
                'id': movie['id'],
                'title': movie['title'],
                'slug': slugify(movie['title']),
                'poster_path': movie['poster_path'],
                'average_vote': drop_decimal_but_first(movie['vote_average']),
                'genre': first_genre_name,  # Add the genre name here
            })

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
        
        processed_movies = []

        for movie in movies:
            # Extract the first genre ID
            first_genre_id = movie.get('genre_ids', [])[0] if movie.get('genre_ids') else None

            # Get the genre name using the GENRE_MAP (or another API call if you prefer)
            first_genre_name = GENRE_MAP.get(first_genre_id, 'Unknown Genre')

            processed_movies.append({
                'id': movie['id'],
                'title': movie['title'],
                'slug': slugify(movie['title']),
                'poster_path': movie['poster_path'],
                'average_vote': drop_decimal_but_first(movie['vote_average']),
                'genre': first_genre_name,  # Add the genre name here
            })

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
        
        processed_movies = []

        for movie in movies:
            # Extract the first genre ID
            first_genre_id = movie.get('genre_ids', [])[0] if movie.get('genre_ids') else None

            # Get the genre name using the GENRE_MAP (or another API call if you prefer)
            first_genre_name = GENRE_MAP.get(first_genre_id, 'Unknown Genre')

            processed_movies.append({
                'id': movie['id'],
                'title': movie['title'],
                'slug': slugify(movie['title']),
                'poster_path': movie['poster_path'],
                'average_vote': drop_decimal_but_first(movie['vote_average']),
                'genre': first_genre_name,  # Add the genre name here
            })

        return render(request, 'vijaysethupathi.html', {'movies': processed_movies})
    except requests.exceptions.RequestException as e:
        return render(request, 'vijaysethupathi.html', {'error_message': str(e)})
    
def suriya(request):
    actor_id = 85720
    api_url = f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_people={actor_id}&sort_by=popularity.desc&page=1"

    try:
        response = requests.get(api_url)
        response.raise_for_status()  
        data = response.json()
        movies = data['results']  
        
        processed_movies = []

        for movie in movies:
            # Extract the first genre ID
            first_genre_id = movie.get('genre_ids', [])[0] if movie.get('genre_ids') else None

            # Get the genre name using the GENRE_MAP (or another API call if you prefer)
            first_genre_name = GENRE_MAP.get(first_genre_id, 'Unknown Genre')

            processed_movies.append({
                'id': movie['id'],
                'title': movie['title'],
                'slug': slugify(movie['title']),
                'poster_path': movie['poster_path'],
                'average_vote': drop_decimal_but_first(movie['vote_average']),
                'genre': first_genre_name,  # Add the genre name here
            })

        return render(request, 'suryasiva.html', {'movies': processed_movies})
    except requests.exceptions.RequestException as e:
        return render(request, 'suryasiva.html', {'error_message': str(e)})
    
def movie_list(request, genre):
    """Fetch movies based on the genre passed in the URL and provide next genre for navigation."""
    genre_ids = {
        'action': 28,
        'adventure': 12,
        'animation': 16,
        'comedy': 35,
        'crime': 80,
        'documentary': 99,
        'drama': 18,
        'family': 10751,
        'fantasy': 14,
        'history': 36,
        'horror': 27,
        'music': 10402,
        'mystery': 9648,
        'romance': 10749,
        'science-fiction': 878,
        'tv-movie': 10770,
        'thriller': 53,
        'war': 10752
    }

    genre_keys = list(genre_ids.keys())

    genre_key = genre.lower()
    genre_id = genre_ids.get(genre_key)

    if not genre_id:
        return render(request, 'error.html', {'error_message': 'Invalid genre or genre not found.'})

    # Determine next genre
    current_index = genre_keys.index(genre_key)
    next_index = (current_index + 1) % len(genre_keys)
    next_genre_key = genre_keys[next_index]
    next_genre_name = next_genre_key.capitalize()

    api_url = (
        f"https://api.themoviedb.org/3/discover/movie?"
        f"api_key={TMDB_API_KEY}&with_genres={genre_id}"
        f"&sort_by=popularity.desc&page=1&with_original_language=ta"
    )

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        movies = data['results']

        processed_movies = [
            {
                'id': movie['id'],
                'title': movie['title'],
                'poster_path': movie['poster_path'],
                'average_vote': drop_decimal_but_first(movie['vote_average']),
            }
            for movie in movies
        ]
        
        return render(
            request,
            'movie_list.html',
            {
                'movies': processed_movies,
                'genre': genre_key,
                'next_genre': next_genre_name,
                'next_genre_key': next_genre_key,
            }
        )

    except requests.exceptions.RequestException as e:
        return render(request, 'error.html', {'error_message': str(e)})
   
def movie_detail(request, genre, id, slug):
    api_key = TMDB_API_KEY

    # Fetch movie details
    tmdb_url = f"https://api.themoviedb.org/3/movie/{id}?api_key={api_key}&append_to_response=credits"
    response = requests.get(tmdb_url)
    if response.status_code != 200:
        raise Http404("Movie not found.")

    movie = response.json()

    # Fetch genre list to map genre name to ID
    genre_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=en-US"
    genre_response = requests.get(genre_url)
    if genre_response.status_code != 200:
        raise Http404("Genre list could not be fetched.")

    genre_list = genre_response.json().get('genres', [])
    genre_id = next((g['id'] for g in genre_list if g['name'].lower() == genre.lower()), None)

    similar_movies = []
    if genre_id:
        # Fetch movies by genre
        genre_movies_url = (
        f"https://api.themoviedb.org/3/discover/movie?"
        f"api_key={TMDB_API_KEY}&with_genres={genre_id}"
        f"&sort_by=popularity.desc&page=1&with_original_language=ta"
    )
        genre_movies_response = requests.get(genre_movies_url)
        if genre_movies_response.status_code == 200:
            all_genre_movies = genre_movies_response.json().get('results', [])
            # Exclude the current movie and pick top 5
            similar_movies = [m for m in all_genre_movies if m['id'] != id][:5]

    language_full = get_language_full_name(movie.get('original_language'))
    
    context = {
        'title': movie.get('title'),
        'poster_path': movie.get('poster_path'),
        'overview': movie.get('overview'),
        'genres': movie.get('genres', []),
        'release_date': movie.get('release_date'),
        'runtime': movie.get('runtime'),
        'vote_average': movie.get('vote_average'),
        'tagline': movie.get('tagline'),
        'status': movie.get('status'),
        'language': language_full,
        'credits': movie.get('credits', {}),
        'similar_movies': similar_movies,
        'selected_genre': genre,
    }
    print(context)
    return render(request, 'movie_detail.html', context)
