from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


# Create your views here.
def contacts(request):
    return render(request, 'catalog/contacts.html')
