from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app3(request):
    return HttpResponse('<h1>i will come in to day</h1 >')