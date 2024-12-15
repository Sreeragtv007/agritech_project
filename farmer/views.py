from celery.result import AsyncResult
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404, redirect
import pytesseract
from PIL import Image
from .models import Farmerdata, Uploadedimage
from .ocr import ocr_converter
import cv2

import numpy as np
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


from .task import ocr_task

# Create your views here.
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def registerUser(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        confirm = request.POST['confirm']

        print(username, password)

        if User.objects.filter(username=username).exists():

            messages.error(request, "user name already taken")
            return redirect('register')
        if password != confirm:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        user = User.objects.create(
            username=username, password=password)

        login(request, user)

        messages.error(request, "login sucessfully")

        return redirect('index')

    return render(request, 'register.html')


def loginUser(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        print(username, password)

        user = authenticate(request, username=username, password=password)

        print(user)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('index')
        else:

            messages.error(request, "credential not valid")

            return redirect('login')

    return render(request, 'login.html')


def logoutUser(request):

    logout(request)

    messages.success(request, "logout sucessfully")
    return redirect('login')


@login_required(login_url='login')
def home(request):

    print("1")

    obj = Farmerdata.objects.all()

    context = {'obj': obj}
    if request.method == 'POST' and request.FILES['images']:
        uploaded_image = request.FILES['images']
        image_obj = Uploadedimage.objects.create(
            image=uploaded_image, user=request.user)

        image = Image.open(image_obj.image.path)

        text = pytesseract.image_to_string(image, lang="eng")

        converted_data = ocr_converter(text.lower())
        
        print(converted_data)
        if converted_data == False:
            messages.error(request,"invalid geotaged image")
            return render(request,"home.html",context)
        try:
        
            farmer_obj = Farmerdata.objects.create(image=image_obj,**converted_data)
        except Exception as e:
            messages.error(request,"invalid geotaged image")
            print(e)
        finally:
            obj = Farmerdata.objects.all()
            context = {'obj': obj}
            return render(request,"home.html",context)
        
        
    else:
        return render(request,"home.html",context)

        

def index(request):

    return render(request, 'home.html')
