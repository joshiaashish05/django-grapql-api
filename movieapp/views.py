from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
from django.contrib.auth.models import User

# Create your views here.


def allmovies(request):
    allmovies = Movie.objects.all()
    return render(request, 'moviesapp/allmovies.html', {'allmovies': allmovies})


def moviewatched(request):
    movie = Movie.objects.filter(watch=True)
    return render(request, 'moviesapp/watchmovie.html', {'movie': movie})


def viewmovie(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'GET':
        form = MovieForm(instance=movie)
        return render(request, 'moviesapp/viewmovie.html', {'movie': movie, 'form': form})
    else:
        try:
            form = MovieForm(request.POST, instance=movie)
            form.save()
            return redirect('movieapp:allmovies')
        except ValueError:
            return render(request, 'moviesapp/allmovies.html', {'movie': movie, 'form': form, 'error': 'Bad info'})


def recommendedmovies(request):
    movie = Movie.objects.filter(watch=False)
    return render(request, 'moviesapp/recommendedmovies.html', {'movie': movie})


def watchmovie(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk, user=request.user)
    if request.method == 'POST':
        movie.watch
        movie.save()
        return redirect('movieapp:allmovies')
