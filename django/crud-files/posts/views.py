from django.shortcuts import render, redirect
from .models import Post, Comment
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
    image = request.FILES.get('image')
    
    # DB INSERT 
    post = Post(title=title, content=content, image=image)
    post.save()
    # 렌더는 GET에만 사용한다.
    # return render(request, 'create.html')
    # POST는 리 다이렉트를 사용한다 위에 임포트 해줘야 된다.
    return redirect('posts:detail', post.pk)
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
    return redirect('posts:list')

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
    
    return redirect('posts:detail', post.pk)
    
    
def comments_create(request, post_id):
    #댓글을 달 게시물
    post = Post.objects.get(pk=post_id)

    #form에서 넘어온 댓글 내용
    content = request.POST.get('content')
    
    #댓글 생성 및 저장
    comment = Comment(post=post, content=content)
    comment.save()
    
    return redirect('posts:detail', post.pk)
    
def comments_delete(request, post_id, comments_id):
    comment = Comment().objects.get(pk=comment_id)
    comment.delete()
    return redirect('posts:detail', post_id)
    