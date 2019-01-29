from django.contrib import admin
from django.urls import path, include
from students import views

urlpatterns = [

    path('students/', include('students.urls')),
    path('admin/', admin.site.urls),
]
