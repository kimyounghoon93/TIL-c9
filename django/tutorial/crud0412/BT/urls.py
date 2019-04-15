from django.urls import path
from . import views
app_name = 'BT'
urlpatterns = [
    path('create/', views.create, name='create'),
]
