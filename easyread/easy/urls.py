from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

app_name='home'

urlpatterns = [
    path('', views.index, name='index'),
	url(r'^timeline/(?P<id>[\w-]+)/$', views.timetable, name="schedule"),
]

# (?P<file_name>[\w.]{0,256})/$