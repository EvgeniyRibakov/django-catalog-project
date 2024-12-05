from django.contrib import admin
from django.urls import path, include
from newapp.apps import NewappConfig
from newapp.views import home

app_name = NewappConfig.name

urlpatterns = [
    path('', home, name="home")
]
