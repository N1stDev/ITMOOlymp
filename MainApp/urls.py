from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/movies", views.movies, name="movies"),
    path("api/movies/<int:id>", views.movie, name="movie"),
    path("api/directors", views.directors, name="directors"),
    path("api/directors/<int:id>", views.director, name="director")

]