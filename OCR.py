import pytesseract
import cv2
import matplotlib.pyplot as plt
from PIL import Image


# читать изображение с помощью OpenCV
image = cv2.imread("test.jpg")
# или вы можете использовать подушку
# image = Image.open("test.png")
# получаем строку
string = pytesseract.image_to_string(image)
# печатаем
print(string)