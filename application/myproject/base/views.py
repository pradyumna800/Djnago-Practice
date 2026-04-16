from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>This is the base application view</h1>')

def car(request):
    return render(request, 'car.html')