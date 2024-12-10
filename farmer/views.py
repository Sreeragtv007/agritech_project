from django.shortcuts import render
import pytesseract
from PIL import Image
from .models import Farmer
from .ocr import ocr_converter
# Create your views here.
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def index(request):

    if request.method == 'POST' and request.FILES['image']:
        uploaded_image = request.FILES['image']
        image = Image.open(uploaded_image)

        text = pytesseract.image_to_string(image, lang='eng')
        
        converted_data = ocr_converter(text)
        
        print(converted_data)

        farmer_obj = Farmer.objects.create(image=uploaded_image)

    return render(request, 'index.html')
