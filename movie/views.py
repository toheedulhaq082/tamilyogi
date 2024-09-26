from django.shortcuts import render
import os
from dotenv import load_dotenv
import requests
from .helpers import drop_decimal_but_first
from .models import BlogModel
from django.views.generic import ListView

load_dotenv()

TMDB_API_KEY = os.environ.get("TMDB_SECRET_KEY")

# Create your views here.

class HomePageView(ListView): 
    template_name = 'home.html'
    model = BlogModel
    context_object_name = 'all_posts_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get blog posts by tag
        context['tamil_posts'] = BlogModel.objects.filter(tag='tamil').order_by('-created_at')
        context['telugu_posts'] = BlogModel.objects.filter(tag='telugu').order_by('-created_at')
        context['dubbed_posts'] = BlogModel.objects.filter(tag='dubbed').order_by('-created_at')
        context['hindi_posts'] = BlogModel.objects.filter(tag='hindi').order_by('-created_at')
        return context

def blog_detail(request, slug):
    context = {}
    try:
        blog_obj = BlogModel.objects.filter(slug=slug).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'blog_detail.html', context=context)

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
                'title': movie['title'],
                # 'genres': ', '.join(movie['genres']),
                'poster_path': movie['poster_path'],
                'average_vote': drop_decimal_but_first(movie['vote_average']),
            }
            for movie in movies
        ]
 
        return render(request, 'suryasiva.html', {'movies': processed_movies})
    except requests.exceptions.RequestException as e:
        
        return render(request, 'suryasiva.html', {'error_message': str(e)})