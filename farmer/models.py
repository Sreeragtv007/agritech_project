from django.db import models

# Create your models here.


class Farmer(models.Model):
    
    image = models.ImageField(upload_to='image')
    
    data = models.TextField(blank=True, null=True)