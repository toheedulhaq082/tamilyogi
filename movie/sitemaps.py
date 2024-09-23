from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class MovieSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    protocol = 'https'

    def items(self):
        return ['home', 'kamal_haasan', 'dhanush', 'vikram', 'vijay-sethupathi'] 

    def location(self, item):
        return reverse(item)