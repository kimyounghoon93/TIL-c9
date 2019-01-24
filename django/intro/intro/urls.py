"""intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('bootstrap/', views.bootstrap),
    path('naver/', views.naver),
    path('catch/', views.catch),
    path('throw/', views.throw),
    path('opgg/<str:nick>', views.opgg),
    # 꺽쇠는 주소를 변동가능하게 안할거면 안써도 됨
    path('personalities/', views.personalities),
    # 동적인 주소 <str:name>
    path('hello/<str:name>/', views.hello),
    path('dinner/', views.dinner),
    path('index/', views.index),
    path('admin/', admin.site.urls),
]
