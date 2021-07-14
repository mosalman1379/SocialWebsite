from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='image_created')
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)
    url = models.URLField()
    image = models.ImageField('images/')
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    users_like = models.ManyToManyField(User, related_name='images_liked', blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
