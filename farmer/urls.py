
from django.urls import path,include
from .views import registerUser,loginUser,logoutUser,home,detail,mapapi
urlpatterns = [
    path('register/',registerUser,name='register'),
    path('login/',loginUser,name='login'),
    path('logout/',logoutUser,name='logout'),
    path('',home,name='home'),
    path('detail/<str:pk>/',detail,name='detail'),
    path('apimap/',mapapi,name='mapapi'),
]
