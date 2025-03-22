from django.db import models
from django.utils.text import slugify

class Kategori(models.Model):
    name = models.CharField(max_length=100)
    slug=models.SlugField(null=True,blank=True,db_index=True)
    

    def save(self, *args,**kwargs):
        self.slug=slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name

class Notlar(models.Model):
    ad = models.CharField(max_length=100)
    aciklama = models.TextField()  
    resim = models.ImageField(upload_to="resimler")
    slug=models.SlugField(null=True,blank=True,db_index=True) 
    kategori=models.ManyToManyField(Kategori)

    def save(self, *args,**kwargs):
        self.slug=slugify(self.ad)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.ad
    

    
