from django.db import models
from users.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name




class Note(models.Model):
    text = models.TextField()
    title = models.CharField(max_length=255)
    time_created = models.DateTimeField(auto_now_add=True)
    time_edited = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    categories = models.ManyToManyField(Category, related_name='notes')
    starred = models.BooleanField(default=False)

