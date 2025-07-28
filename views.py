from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required  
from .models import Movie
from .forms import MovieForm
from django.contrib import messages


@login_required(login_url='login')
def movie_list(request):
    query = request.GET.get('q', '')
    if query:
        movies = Movie.objects.filter(title__icontains=query).order_by('-id')
    else:
        movies = Movie.objects.all().order_by('-id')
    return render(request, 'movies/movie_list.html', {'movies': movies, 'query': query})


@login_required(login_url='login')
def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'movies/movie_form.html', {'form': form})

@login_required(login_url='login') 
def movie_update(request, id):
    movie = get_object_or_404(Movie, id=id)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movies/movie_form.html', {'form': form})

@login_required(login_url='login') 
def movie_delete(request, id):
    movie = get_object_or_404(Movie, id=id)
    if request.method == 'POST':
        movie.delete()
        return redirect('movie_list')
    return render(request, 'movies/movie_confirm_delete.html', {'movie': movie})


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Llogaria u krijua me sukses! Tani je i kyçur.')
            return redirect('movie_list')
        else:
            messages.error(request, 'Ka ndodhur një gabim. Ju lutem kontrolloni fushat më poshtë.')
    else:
        form = UserCreationForm()
    return render(request, 'movies/signup.html', {'form': form})


