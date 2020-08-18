from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(requests):
   return HttpResponse('<h1>This is my page</h1>')
def aboutus(requests):
    return HttpResponse('<p><b>Name:</b> Siva Kumar<br><b>College:</b> Vasavi college of engineering<br><p>')
def hobbies(requests):
    return HttpResponse('<ul><li>Reading books</li><li>browsing net</li><li>playing cricket</li><li>playing online game</li></ul>') 