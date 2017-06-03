from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True)
    embed_code = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True) # time added
    updated = models.DateTimeField(auto_now=True) # last saved

    def __str__(self):
        return self.title
