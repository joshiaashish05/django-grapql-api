from django.urls import path
from .import views

app_name = 'movieapp'
urlpatterns = [
    path('allmovies/', views.allmovies, name='allmovies'),
    path('moviewatched/', views.moviewatched, name='moviewatched'),
    path('recommendedmovies/', views.recommendedmovies, name='recommendedmovies'),
    path('viewmovie/<int:movie_pk>', views.viewmovie, name='viewmovie'),
    path('viewmovie/<int:movie_pk>/watchmovie', views.watchmovie, name='watchmovie'),
]
