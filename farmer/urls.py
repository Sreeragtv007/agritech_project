
from django.urls import path,include
from .views import index,registerUser,loginUser,logoutUser
urlpatterns = [
    path('',index,name='index'),
    path('register/',registerUser,name='register'),
    path('login/',loginUser,name='login'),
    path('logut/',logoutUser,name='logout'),
]
