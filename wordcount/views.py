from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return render(request, 'home.html', {'hell':'20 words'})

def count(request):
    text = request.GET['fulltext']
    textd = text.split()
    worddict = {}
    for i in textd:
        if i in worddict:
            worddict[i] += 1
        else:
            worddict[i] = 1
    return render(request, 'count.html', {'text':text, 'textd':len(textd), 'countd':worddict.items()})

def about(request):
    return render(request, 'about.html')