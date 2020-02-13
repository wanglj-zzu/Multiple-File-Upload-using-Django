from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from index import views
urlpatterns = [
    path('form/', views.Form),
    path('upload', views.Upload),
]
