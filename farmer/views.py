from django.shortcuts import render, get_object_or_404
import pytesseract
from PIL import Image
from .models import Farmerdata, Uploadedimage
from .ocr import ocr_converter
import cv2
# Create your views here.
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'



def register(request):
    
    
    return render(request,'register.html')

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
        
        
        if len(converted_data) > 4 :
            print("image not clear")
        else:
            
            farmer_obj = Farmerdata.objects.create(image=image_obj,**converted_data)

        return render(request, 'index.html')
    else:
        return render(request, 'index.html')
