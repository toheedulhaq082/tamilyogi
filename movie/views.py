from django.shortcuts import render
import os
from dotenv import load_dotenv
import requests
from .helpers import drop_decimal_but_first
from .models import BlogModel
from django.views.generic import TemplateView
from django.http import Http404
from django.utils.text import slugify
from django.http import HttpResponse


load_dotenv()

TMDB_API_KEY = os.environ.get("TMDB_SECRET_KEY")

# Create your views here.

def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow:",
        "Sitemap: https://tamilyogi.moviechoose.com/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        api_key = TMDB_API_KEY
        
        url = 'https://api.themoviedb.org/3/discover/movie'
        params = {
            'api_key': api_key,
            'with_original_language': 'ta',
            'sort_by': 'vote_average.desc',
            'vote_count.gte': 100,  # filters out movies with very few votes
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            context['movies'] = data.get('results', [])
        except requests.exceptions.RequestException as e:
            context['movies'] = []
            context['error'] = str(e)

        return context
    


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
        processed_movies = [
            {
                'id': movie['id'],
                'title': movie['title'],
                'slug': slugify(movie['title']),
                'poster_path': movie['poster_path'],
                'average_vote': drop_decimal_but_first(movie['vote_average']),
            }
            for movie in movies
        ]

        return render(request, 'vikram.html', {'movies': processed_movies})
    except requests.exceptions.RequestException as e:
        return render(request, 'vikram.html', {'error_message': str(e)})
    
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
                'id': movie['id'],
                'title': movie['title'],
                'slug': slugify(movie['title']),
                'poster_path': movie['poster_path'],
                'average_vote': drop_decimal_but_first(movie['vote_average']),
            }
            for movie in movies
        ]

        return render(request, 'vikram.html', {'movies': processed_movies})
    except requests.exceptions.RequestException as e:
        return render(request, 'vikram.html', {'error_message': str(e)})
    
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
                'id': movie['id'],
                'title': movie['title'],
                'slug': slugify(movie['title']),
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
                'id': movie['id'],
                'title': movie['title'],
                'slug': slugify(movie['title']),
                'poster_path': movie['poster_path'],
                'average_vote': drop_decimal_but_first(movie['vote_average']),
            }
            for movie in movies
        ]

        return render(request, 'vikram.html', {'movies': processed_movies})
    except requests.exceptions.RequestException as e:
        return render(request, 'vikram.html', {'error_message': str(e)})
    
def suriya(request):
    actor_id = 85720
    api_url = f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_people={actor_id}&sort_by=popularity.desc&page=1"

    try:
        response = requests.get(api_url)
        response.raise_for_status()  
        data = response.json()
        movies = data['results']  
        processed_movies = [
            {
                'id': movie['id'],
                'title': movie['title'],
                'slug': slugify(movie['title']),
                'poster_path': movie['poster_path'],
                'average_vote': drop_decimal_but_first(movie['vote_average']),
            }
            for movie in movies
        ]

        return render(request, 'vikram.html', {'movies': processed_movies})
    except requests.exceptions.RequestException as e:
        return render(request, 'vikram.html', {'error_message': str(e)})
    
def movie_list(request, genre):
    """Fetch movies based on the genre passed in the URL."""
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

    genre_id = genre_ids.get(genre.lower())

    if not genre_id:
        return render(request, 'error.html', {'error_message': 'Invalid genre or genre not found.'})

    # Fetch movies from TMDb API
    api_url = (
    f"https://api.themoviedb.org/3/discover/movie?"
    f"api_key={TMDB_API_KEY}&with_genres={genre_id}"
    f"&sort_by=popularity.desc&page=1&with_original_language=ta"
)

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for 4xx/5xx responses
        data = response.json()
        movies = data['results']  # Extract the list of movies from the response
        
        # Process movie data
        processed_movies = [
    {
        'id': movie['id'],  # Add this
        'title': movie['title'],
        'poster_path': movie['poster_path'],
        'average_vote': drop_decimal_but_first(movie['vote_average']),
    }
    for movie in movies
]
        genre = genre.capitalize()
        
        # Render the movie list template
        return render(request, 'movie_list.html', {'movies': processed_movies, 'genre': genre})
    
    except requests.exceptions.RequestException as e:
        # Handle API request error
        return render(request, 'error.html', {'error_message': str(e)})
    
def movie_detail(request, id, slug):
    api_key = TMDB_API_KEY
    tmdb_url = f"https://api.themoviedb.org/3/movie/{id}?api_key={api_key}&append_to_response=credits"

    response = requests.get(tmdb_url)
    if response.status_code != 200:
        raise Http404("Movie not found.")

    movie = response.json()

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
        'language': movie.get('original_language'),
        'credits': movie.get('credits', {}),
    }
    return render(request, 'movie_detail.html', context)
