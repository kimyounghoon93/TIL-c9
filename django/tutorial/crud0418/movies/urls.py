from django.urls import path
from . import views
# 변수         # [리스트]
app_name = 'movies'         # 암거나 써도 됨 하지만 보통은 앱네임을 사용함

urlpatterns = [
    path('', views.list, name='list'),
    path('create/', views.create, name='create'),
    path('<int:movie_id>/', views.detail, name='detail'),
    path('<int:movie_id>/update/', views.update, name='update'),
    path('<int:movie_id>/delete/', views.delete, name='delete'),
    path('<int:movie_id>/comments/create/', views.comments_create, name='comments_create'),
    path('<int:movie_id>/comments/<int:comment_id>/delete/', views.comments_delete, name='comments_delete'),
]