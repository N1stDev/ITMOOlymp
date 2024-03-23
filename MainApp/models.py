from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Director(models.Model):
    id = models.IntegerField(primary_key=True)
    fio = models.CharField(max_length=100)


class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    year = models.IntegerField(validators=[MaxValueValidator(1900), MinValueValidator(2100)])
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    length = models.TimeField()
    rating = models.IntegerField(validators=[MaxValueValidator(0), MinValueValidator(10)])
