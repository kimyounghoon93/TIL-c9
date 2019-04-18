from django.urls import path
from . import views
# 변수         # [리스트]
urlpatterns = [
    path('create/',views.create),
]