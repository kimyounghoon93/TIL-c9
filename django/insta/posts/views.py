from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .forms import PostForm, CommentForm, ImageFormSet
from .models import Post, Comment
from django.db import transaction
from itertools import chain
from django.http import JsonResponse
# Create your views here.

def explore(request):
    posts = Post.objects.order_by('-id').all()
    comment_form = CommentForm()
    return render(request, 'posts/list.html',{
                            'posts': posts,
                            'comment_form': comment_form
    })

@login_required
def list(request):
    # posts = Post.objects.order_by('-id').all() # 최신글 상단배치 ('-id')
    # 1. 내가 follow 하고 있는 사람들의 리스트
    followings = request.user.followings.all()
    # 2. 내 followings 변수와 나를 묶음
    followings = chain(followings,[request.user])
    # 2. 내가 팔로우한 사람들이 작성한 Post들만 뽑아옴.
    posts = Post.objects.filter(user__in=followings).order_by('-id')
    comment_form = CommentForm()
    return render(request, 'posts/list.html', {'posts': posts, 'comment_form': comment_form})


@login_required
def create(request):
    if request.method == 'POST':
        request.POST #=> {'content:'}:asdfif.iser+id_busf:1{}
        post_form = PostForm(request.POST)
        image_formset = ImageFormSet(request.POST, request.FILES)
        if post_form.is_valid() and image_formset.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            
        # 순서를 보장하도록 하는 메소드
            with transaction.atomic():
                # 첫번째
                post.save() # 실제 데이터 베이스에 저장
                # 두번째
                image_formset.instance = post
                image_formset.save() # 실제 데이터베이스에 저장
                
            return redirect('posts:list')
    else:
        post_form = PostForm()
        image_formset = ImageFormSet()
    return render(request, 'posts/form.html', {'post_form': post_form, 
                                               'image_formset': image_formset,
                                            })
@login_required
def update(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if post.user != request.user:
        return redirect('posts:list')
    
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        image_formset = ImageFormSet(request.POST, request.FILES, instance=post)
        if post_form.is_valid() and image_formset.is_valid():
            post_form.save()
            image_formset.save()
            return redirect('posts:list')
    else:
        post_form = PostForm(instance=post)
        image_formset = ImageFormSet(instance=post)
    return render(request,'posts/form.html', {
                                            'post_form': post_form,
                                            'image_formset': image_formset,
                                        })
    
@login_required
def delete(request, post_id):
    # post = Post.objects.get(id=post_id)
    post = get_object_or_404(Post, id=post_id) # 좀 더 직관적인 표현
    
    if post.user != request.user:
        return redirect('post:list')
    
    post.delete()
    # if post.user == request.user:
    #     post.delete()
    
    return redirect('posts:list')
@login_required
@require_POST
def comment_create(request, post_id):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.post_id = post_id
        comment.save()
    # return redirect('posts:list')
    return JsonResponse({
                        'id': comment.id, 
                        'postId': post_id,
                        'username': comment.user.username,
                        'content': comment.content,
    })
    
@require_http_methods(['GET','POST'])
def comment_delete(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    
    if comment.user != request.user:
        return redirect('posts:list')
        
    comment.delete()
    return redirect('posts:list')
@login_required
def like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.user in post.like_users.all():
        post.like_users.remove(request.user)
        liked = False
    else:
        post.like_users.add(request.user)
        liked = True
    # return redirect('posts:list')
    return JsonResponse({'liked': liked, 'count': post.like_users.count()})