from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Witaj!")
    return render(request, 'pizza/index.html')


def news(request):
    return HttpResponse("<h1>Nowości w barze</h1>")


def widok(request):
    return HttpResponse("<h1>Widok</h1>")


def gallery(request):
    return render(request, 'pizza/gallery.html')