from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleModelForm
# Create your views here.
def create(request):
    if request.method == 'POST':
        form = ArticleModelForm(request.POST)
        # title = .get('title)
        if form.is_valid():
            # 폼이라는 것이 모델에 대한 정보와 필드에 들어갈 데이터들을 다 가지고 있기에 폼.세이브 사용가능
            article = form.save()
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # =
            # article = Article(title=title, content=content)
            # article.save()
            # article = Article.objects.create(title=title, content=content)
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleModelForm()
        
    return render(request, 'form.html', {'form':form})
        
def detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(request, 'detail.html', {'article':article})
    
def update(request, article_id):
    article = Article.objects.get(pk=article_id)
    if request.method == 'POST':
        form = ArticleModelForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleModelForm(instance=article)
        
    return render(request, 'form.html', {'form':form})