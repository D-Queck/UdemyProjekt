from django.shortcuts import render
from . models import *

# Create your views here.

def shop(request):
    artikels = Artikel.objects.all()
    ctx = {'artikels':artikels}
    return render(request, 'shop/shop.html', ctx)

def warenkorb(request):
<<<<<<< HEAD
    if request.user.is_authenticated:
        kunde = request.user.kunde
        bestellung, created = Bestellung.objects.get_or_create(kunde=kunde, erledigt=False)
        artikels = bestellung.bestellteartikel_set.all()
    else:
        artikels = []
        bestellung = []

    ctx = {"artikels":artikels, "bestellung":bestellung}        
    return render(request, 'shop/warenkorb.html',ctx)

def kasse(request):
    if request.user.is_authenticated:
        kunde = request.user.kunde
        bestellung, created = Bestellung.objects.get_or_create(kunde=kunde, erledigt=False)
        artikels = bestellung.bestellteartikel_set.all()
    else:
        artikels = []
        bestellung = []

    ctx = {"artikels":artikels, "bestellung":bestellung}      
    return render(request, 'shop/kasse.html', ctx)
=======
    return render(request, 'shop/warenkorb.html')

def kasse(request):
    return render(request, 'shop/kasse.html')
>>>>>>> a1e55d60fcd3a69728f825bcfa3c46dde77d6268
    
    