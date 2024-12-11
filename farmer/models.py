from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Farmerdata(models.Model):
    
    latitude = models.DecimalField(max_digits=9,decimal_places=6,blank=True, null=True)
    longitude = models.DecimalField(max_digits=9,decimal_places=6,blank=True, null=True)
    elevation = models.CharField(max_length=50,blank=True, null=True)
    accuracy =models.CharField(max_length=50,blank=True, null=True)
    azimuth = models.CharField(blank=True, null=True,max_length=50)
    pitch = models.CharField(blank=True, null=True,max_length=50)
    time = models.CharField(max_length=50,blank=True, null=True)
    farmer_id = models.IntegerField(blank=True, null=True)
    farmer_name =models.CharField(max_length=50,blank=True, null=True)
    crop_name = models.CharField(blank=True, null=True,max_length=50)
    image = models.OneToOneField('Uploadedimage',on_delete=models.CASCADE,blank=True, null=True)
    
    
class Uploadedimage(models.Model):
    image = models.ImageField(upload_to='image',blank=True, null=True)
    user = models.ForeignKey(User,blank=True, null=True,on_delete=models.CASCADE)


    

    
    