from django.shortcuts import render, redirect, get_object_or_404
from .forms import MovieForm
from .models import Movie
from django.views.decorators.http import require_POST
# Create your views here.
def create(request):
    if request.method == 'POST':
        # request.POST #=> 바디안에 입력한 값이 {'title': 'asdf'} # models.py에 title로 만들어서 title이라고 되어있음
        # request.GET #=> 주소창에 {'q': 'xyz'}
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            # print(movie)
            # print(movie.id)
            # print(movie.title)
            # return redirect('/movies/{}/'.format(movie.id))
            return redirect('movies:detail', movie.id) # movie_id = movie.id
            # -->> 번역하는 과정이 들어감
            # 'movies:detail', movie.id #=> /movies/1/(GET요청)  # movie_id = 1
    else:
        form = MovieForm()
    return render(request, 'movies/form.html', {'form': form})
    
    # return이 if 줄에 있는 이유는 else가 오던 is_valid()를 통과 못하면 사용 하기위함

def detail(request, movie_id): # urls.py에 <int:movie_id>와 이름이 같아야 됨
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})

def list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/list.html', {'movies':movies})
    
def update(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method =='POST':
        form = MovieForm(request.POST, instance=movie)
        # movie.title = 'asdf'
        if form.is_valid():
            movie = form.save()
            # movie.save()
            return redirect('movies:detail', movie.id) # <<-- movie_id를 사용해도 된다.
        
    else:
        form = MovieForm(instance=movie)
        
    return render(request, 'movies/form.html', {'form':form})


# POST로 만든 delete
@require_POST
def delete(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    movie.delete()
    return redirect('movies:list')