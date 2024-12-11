
from django.urls import path,include
from .views import registerFarmer



urlpatterns = [
    
    path('register/',registerFarmer,name='register_farmer'),
]

