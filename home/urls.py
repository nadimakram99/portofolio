
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index, name='home'),
    path("post",views.about, name='post'),
    path("resume",views.resume, name='resume'),
    path("contact",views.contact, name='contact')

 
    
]
