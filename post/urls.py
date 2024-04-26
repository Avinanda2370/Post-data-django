from django.contrib import admin
from django.urls import path
from post.views import hi

urlpatterns = [
    path('',hi,name='hi'),
]