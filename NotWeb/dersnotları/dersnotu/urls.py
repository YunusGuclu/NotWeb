from.import views
from django.urls import path

urlpatterns=[
    path("",views.index,name="home"),
    path("dersnotu/<slug:slug>", views.dersnotu,name="dersnotu"),
    path("kategori/<slug:slug>", views.kategoridetayı,name="kategoridetay"),
   
]