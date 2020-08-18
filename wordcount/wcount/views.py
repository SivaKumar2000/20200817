from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(requests):
   return HttpResponse('<h1>This is my page</h1>')
