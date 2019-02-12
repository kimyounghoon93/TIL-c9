from django.contrib import admin
from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [

    
    #주소명을 추후에 변경 하더라도 일일이 찾아가서 안바꿔도 자동으로 네이밍 되도록 함 그리고 슬레쉬를 신경 안써도 된다! 중괄호{}나 %를 걱정하면된다..
    path('github/<str:username>', views.github, name='github'),
    path('naver/<str:q>', views.naver, name='naver'),
    path('', views.index, name='list'), # GET
    
    # path('create/', views.create, name='create'), #GET(new), POST(creat)
    path('write/', views.new, name='new'),
    path('<int:post_id>/', views.detail, name='detail'), #GET
    path('<int:post_id>/delete/', views.delete, name='delete'), # GET (confirm)
    path('<int:post_id>/edit/', views.edit, name='edit'), # GET, POST(update)
    # path('<int:post_id>/update/', views.update, name='update'),
    path('<int:post_id>/comments/create/', views.comments_create, name='comments_create'),
    path('<int:post_id>/comments/<int:comment_id>/delete/', views.comments_delete, name='comments_delete'),
    
]
