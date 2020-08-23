from django.shortcuts import render
from django.http import HttpResponse
import operator

def home(requests):
    return render(requests,'wcount/home.html')
def helpme(requests):
    return render(requests,'wcount/help.html')
def count(requests):
    myText=requests.GET['fulltext']
    words=myText.split()
    l1=[]
    for i in words:
        if [i,words.count(i)] not in l1:
            l1.append([i,words.count(i)])
    if(len(l1)==0):
        return HttpResponse("No input given please refer help")
    else:
        return render(requests,'wcount/count.html',{'yourlist':l1})
