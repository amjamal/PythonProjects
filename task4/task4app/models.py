from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=30)
    img = models.ImageField(upload_to='pictures')
    loc = models.CharField(max_length=50)
    desc = models.TextField()

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=30)
    img = models.ImageField(upload_to='pictures')
    movie = models.CharField(max_length=30)
    info = models.TextField()

    def __str__(self):
        return self.name
