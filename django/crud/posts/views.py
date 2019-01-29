from django.shortcuts import render, redirect
from .models import Post
# Create your views here.
# views.py >> urls.py >> template.py
# def throw
# def catch

def index(request):
    return render(request,'index.html')

# Form tag
def new(request):
    return render(request, 'new.html')
    
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    # DB INSERT 
    post = Post(title=title, content=content)
    post.save()
    # 렌더는 GET에만 사용한다.
    # return render(request, 'create.html')
    # POST는 리 다이렉트를 사용한다 위에 임포트 해줘야 된다.
    return redirect(f'/posts/{post.pk}/')
    # 외부 사이트로도 리다이렉트 가능함
# def rd(request, 변수):
def naver(request, q):
    return redirect(f'https://search.naver.com/search.naver?query={q}')
    
    # https://playground-busanteam.c9users.io/posts/naver/검색\
    # 깃헙처럼 id값이 주소창에 입력 되는 경우
def github(request, username):
    return redirect(f'https://github.com/{username}')

def index(request):
    # All Post
    posts = Post.objects.all()
    
    return render(request, 'index.html', {'posts':posts})
    
def detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'detail.html', {'post': post})
    
def delete(request, post_id):
    # 삭제하는 코드
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('/posts/')

def edit(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'edit.html', {'post':post})

def update(request, post_id):
    # 수정하는 코드
    # 수정하기 위해 수정 할 것을 불러온다
    post = Post.objects.get(pk=post_id)
    post.title = request.POST.get('title')
    post.content = request.POST.get('content')
    # 실제로 반영하기위해선 세이브를 해주어야 한다
    post.save()
    
    return redirect(f'/posts/{post_id}/')
    
    
    
    
    
    
    