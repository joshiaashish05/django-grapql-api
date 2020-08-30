from django.db import models
from django.contrib.auth.models import User
from apiapp.models import Director
# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField(default=2000)
    watch = models.BooleanField(default=False)
    user = models.ManyToManyField(User, null=True)
    director = models.ForeignKey(Director, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.title
