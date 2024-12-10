from django.db import models

# Create your models here.


class Farmer(models.Model):
    
    image = models.ImageField(upload_to='image')
    latitude = models.DecimalField(max_digits=9,decimal_places=6,blank=True, null=True)
    longitude = models.DecimalField(max_digits=9,decimal_places=6,blank=True, null=True)
    accuracy =models.CharField(max_length=50,blank=True, null=True)
    azimuth = models.DecimalField(max_digits=5,decimal_places=5,blank=True, null=True)
    pitch = models.DecimalField(max_digits=5,decimal_places=5,blank=True, null=True)
    time = models.CharField(max_length=50,blank=True, null=True)
    farmer_id = models.IntegerField(blank=True, null=True)
    farmer_name =models.CharField(max_length=50,blank=True, null=True)
    crop_name = models.TextField(blank=True, null=True)
    
    
    