from django.contrib import admin
from django.urls import path, include
from . import views

app_name='home'

urlpatterns = [
    path('', views.index, name='index'),
    path('timetable/', views.timetable, name='schedule'),
]
