from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(requests):
   return render(requests,'wcount/home.html',{'name':'SivaKumar'})
def aboutus(requests):
   return render(requests,'wcount/about.html',{'userid':'SivaKumar2000'})
def hobbies(requests):
   return render(requests,'wcount/hobbies.html')
