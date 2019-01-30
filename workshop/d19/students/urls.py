from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('github/<str:username>', views.github),
    path('naver/<str:q>', views.naver),
    path('', views.index),
    path('create/', views.create),
    path('detail/', views.detail),
    path('new/', views.new),
    path('<int:student_id>/', views.detail),
    path('<int:student_id>/delete/', views.delete),
    path('<int:student_id>/edit/', views.edit),
    path('<int:student_id>/update/', views.update),
    
]
