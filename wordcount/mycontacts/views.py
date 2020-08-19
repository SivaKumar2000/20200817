from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import operator
def name(requests):
    return render(requests,'mycontacts/name.html')
def numbers(requests):
    return render(requests,'mycontacts/numbers.html')
