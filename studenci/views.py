from django.shortcuts import render
from studenci.models import Miasto, Uczelnia


# Create your views here.

def index(request):
    return render(request, 'studenci/index.html')

def miasta(request):

    if request.method == 'POST':
        nazwa = request.POST.get('nazwa')
        kod = request.POST.get('kod')
        m = Miasto(nazwa=nazwa, kod=kod)
        m.save()
        print(nazwa)
        print(kod)

    miasta = Miasto.objects.all()
    kontekst = {
        'miasta': miasta
    }
    return render(request, 'studenci/miasta.html', kontekst)

def uczelnie(request):

    if request.method == 'POST':
        nazwa = request.POST.get('uczelnia')
        m = Uczelnia(nazwa=nazwa)
        m.save()


    uczelnie = Uczelnia.objects.all()
    kontekst = {
        'uczelnie': uczelnie
    }
    return render(request, 'studenci/uczelnie.html', kontekst)
