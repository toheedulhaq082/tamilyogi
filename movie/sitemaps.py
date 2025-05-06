from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from dotenv import load_dotenv
import os
from .movies_lists import action_movies

load_dotenv()

TMDB_API_KEY = os.environ.get("TMDB_SECRET_KEY")

class MovieSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    protocol = 'https'

    def items(self):
        static_urls = [
            ('static', 'home'),
            ('static', 'kamal_haasan'),
            ('static', 'dhanush'),
            ('static', 'vikram'),
            ('static', 'vijay-sethupathi'),
            ('static', 'suriya_sivakumar'),
            ('static', 'anime'),
        ]

        genres = [
            'action', 'adventure', 'animation', 'comedy', 'crime', 'documentary',
            'drama', 'family', 'fantasy', 'history', 'horror', 'music', 'mystery',
            'romance', 'science-fiction', 'tv-movie', 'thriller', 'war'
        ]
        genre_urls = [('genre', genre) for genre in genres]

        # Assuming all movies in action_movies belong to 'action' genre
        movie_urls = [('movie', 'action', movie['id'], movie['slug']) for movie in action_movies]

        return static_urls + genre_urls + movie_urls

    def location(self, item):
        type_ = item[0]

        if type_ == 'static':
            return reverse(item[1])
        elif type_ == 'genre':
            return reverse('movie_list', kwargs={'genre': item[1]})
        elif type_ == 'movie':
            return reverse('movie_detail', kwargs={'genre': item[1], 'id': item[2], 'slug': item[3]})
