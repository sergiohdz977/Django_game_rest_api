from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    release_year = models.IntegerField()

    def __str__(self):
        return self.name

# Create your models here.
