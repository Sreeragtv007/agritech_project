from django.shortcuts import render, get_object_or_404, redirect
import pytesseract
from PIL import Image
from .models import Farmerdata, Uploadedimage
from .ocr import ocr_converter
import cv2
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def registerUser(request):
    if request.method == 'POST':
        
        

        username = request.POST['username']
        password = request.POST['password']
        confirm = request.POST['confirm']
        
        
        print(username,password)

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

        username = username = request.POST['username']
        password = username = request.POST['password']
        
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
                login(request, user) 
                messages.success(request, "Login successful!")
                return redirect('index') 

    return render(request, 'login.html')


def logoutUser(request):
    
    logout(request)
    
    messages.success(request,"logout sucessfully")
    return redirect('login')
    
    


def index(request):

    if request.method == 'POST' and request.FILES['image']:
        uploaded_image = request.FILES['image']
        # image = Image.open(uploaded_image)
        image_obj = Uploadedimage.objects.create(
            image=uploaded_image, user=request.user)

        image = cv2.imread(image_obj.image.path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
        thresh_img = cv2.adaptiveThreshold(
            binary, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        denoised_img = cv2.fastNlMeansDenoising(thresh_img, None, 30, 7, 21)

        text = pytesseract.image_to_string(denoised_img, lang='eng')

        print(text)

        print("_______________________________________")
        converted_data = ocr_converter(text)

        if len(converted_data) > 4:
            print("image not clear")
        else:

            farmer_obj = Farmerdata.objects.create(
                image=image_obj, **converted_data)

        return render(request, 'index.html')
    else:
        return render(request, 'index.html')
