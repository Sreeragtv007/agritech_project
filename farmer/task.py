# myapp/tasks.py

from celery import shared_task
from time import sleep
import pytesseract
from PIL import Image
from .ocr import ocr_converter
import cv2
from .models import Uploadedimage, Farmerdata

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

import logging

logger = logging.getLogger(__name__)
@shared_task
def ocr_task(image_path):
    
    logger.info("This is a log statement inside the Celery task.")    
    return "test"
    # Simulate a long-running task
    image = Image.open(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
    thresh_img = cv2.adaptiveThreshold(
        binary, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    denoised_img = cv2.fastNlMeansDenoising(
        thresh_img, None, 30, 7, 21)
    text = pytesseract.image_to_string(denoised_img, lang='eng')
    
    

    converted_data = ocr_converter(text)

    farmer_obj = Farmerdata.objects.create(
        **converted_data)
    
    return farmer_obj
    

    
    
