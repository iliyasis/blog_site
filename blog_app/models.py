from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    category = models.ManyToManyField(Category)
    content = models.TextField()
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{ self.title }   ------------  {self.content[:25]} "