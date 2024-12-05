from django.urls import path
from newapp.apps import NewappConfig
from newapp.views import home, contacts

app_name = NewappConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
]
