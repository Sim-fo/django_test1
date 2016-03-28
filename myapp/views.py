from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'myapp/home.html')


def contact(request):
    return render(request, 'myapp/basic.html', {'content':['тут текст','a@b.com\n','другой текст','еще текст\n']})
