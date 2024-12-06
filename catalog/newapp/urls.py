from django.urls import path
from catalog.newapp.apps import NewappConfig
from catalog.newapp.views import home, contacts

app_name = NewappConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
]
