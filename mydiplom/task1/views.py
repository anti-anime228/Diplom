from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')


