from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import operator
def drinks(requests):
    return render(requests,'blogs/drinks.html')
def food(requests):
    return render(requests,'blogs/food.html')