from django.shortcuts import render
from django.http import HttpResponse

# Create a basic index view
def index(request):
    return HttpResponse("<h1>Welcome to the hotel_pms app!</h1>")
