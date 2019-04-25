from . import views
from django.urls import path

app_name = 'person'

urlpatterns = [
    # path('', views.list,name='person_list'),
    path('', views.PersonList.as_view(), name='person_list'),
    # path('create/', views.create,name='create'),
    path('create/', views.PersonCreate.as_view(), name='create'),
]