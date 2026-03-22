from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    picture = models.ImageField(upload_to='profile_pics')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()

    def __str__(self):
        return self.nickname