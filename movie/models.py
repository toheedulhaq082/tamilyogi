from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField

# Create your models here.
class BlogModel(models.Model):
    TAG_CHOICES = [
        ('tamil', 'Tamil'),
        ('telugu', 'Telugu'),
        ('dubbed', 'Dubbed'),
        ('hindi', 'Hindi'),
    ]
    title = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000, blank=True, null=True)
    tag = models.CharField(max_length=1000, choices=TAG_CHOICES, blank=True, null=True)
    content = FroalaField()
    slug = models.SlugField(max_length=1000, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            from .helpers import generate_slug
            self.slug = generate_slug(self.name)
        super(BlogModel, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/{self.slug}'