import pytesseract
import cv2
import matplotlib.pyplot as plt
from PIL import Image
# Указываем путь к библиотеке tesseract (помогающей работать с изображениями)
pytesseract.pytesseract.tesseract_cmd = r"C:\\Users\\DV\\AppData\\Local\\Tesseract-OCR\\tesseract.exe"

# Читаем изображение с помощью OpenCV (библиотека компьютерного зрения)

print("Привет,давай прочитаем изображение")
img = cv2.imread('test6.png')
print ("Текст прочитан")

# Распознаем картинку с учетом цветовых параметров
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# Выводим данные на экран с задержкой 
cv2.imshow('Result',img)
cv2.waitKey(0)
print (img.shape)

# Меняем разрешение картинки (если потребуется)
img = cv2.resize(img,(500,500))
print (img.shape)


# Считываем изображение для последующего преобразования в строку 
img = Image.open("test6.png")
print ('Изображение готово для преобразования в строку')

# Преобразовываем в строки (для русского языка lang ='rus')
string = pytesseract.image_to_string((img),lang='rus')

# Печатаем полученный текст на экране 
print(string)

# Сохраняем преобразованный текст в файл - save_ocr.txt
f = open('save_ocr.txt', 'w',encoding='utf-8')
f.write(string)
f.close()
print ('Текст успешно сохранен в файл')


       