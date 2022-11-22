import os.path

#import easyocr
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\\Users\\DV\\AppData\\Local\\Tesseract-OCR\\tesseract.exe"




def teseract_recognition(path_img):
    return pytesseract.image_to_string(Image.open('test.png'), lang='rus+eng', config=r'--oem 3 --psm 6')

teseract_recognition('test.png')
