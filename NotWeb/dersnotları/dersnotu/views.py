from django.shortcuts import render, get_object_or_404
from .models import Kategori,Notlar



def index(request):
    query = request.GET.get('q')  # Arama sorgusunu alıyoruz
    if query:
        notlar= Notlar.objects.filter(ad__icontains=query)
    else:
        notlar = Notlar.objects.all()

    data = {
        "kategoriler": Kategori.objects.all(),
        "notlar": notlar,
       
    }
    return render(request, "index.html", data)

def dersnotu(request, slug):
    data = {
        "notlar": get_object_or_404(Notlar, slug=slug)
    }
    return render(request, "dersnotu.html", data)

def kategoridetayı(request, slug):
    kategori = get_object_or_404(Kategori, slug=slug)
    data = {
        "kategoriler": [kategori],  # Kategori nesnesini liste olarak dönüştür
        "notlar": kategori.notlar_set.all(),
    }
    return render(request, "index.html", data)

