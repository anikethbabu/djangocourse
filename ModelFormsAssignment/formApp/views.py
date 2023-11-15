from django.shortcuts import render
from formApp.models import Movie
from formApp.forms import MovieForm
# Create your views here.

def index(request):
    return render(request, 'index.html')

def listMovies(request):
    movieslist = Movie.objects.all()
    return render(request, 'listMovies.html', {'movies': movieslist})

def addMovies(request):
    form = MovieForm()
    if request.method=='POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    return render(request, 'addMovies.html', {'form':form})