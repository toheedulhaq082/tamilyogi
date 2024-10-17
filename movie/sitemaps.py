from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import BlogModel

class MovieSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    protocol = 'https'

    def items(self):
        return ['home', 'kamal_haasan', 'dhanush', 'vikram', 'vijay-sethupathi', 'suriya_sivakumar', 'anime'] 

    def location(self, item):
        return reverse(item)
    
class BlogSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9
    protocol = 'https'

    def items(self):
        return BlogModel.objects.all()

    def lastmod(self, obj):
        return obj.updated_at