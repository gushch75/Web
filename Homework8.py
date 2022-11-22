from dataclasses import dataclass
import json


def vvod(): # Ввод данных справочника 
    global name,comment,number
    name= input('Введите Ф.И.О.')
    comment= input('Введите должность ')
    number = input('Введите номер телефона ')

def convert_data():
    data = (name,comment,number )  
    book = {} 
    book[name]= data
    return book

def save_data():
    with open ('book.txt','a',encoding='utf-8') as telephon_book:
         telephon_book.writelines(convert_data())  

def load_data():
    with open('book.txt','r',encoding='utf-8')  as telephon_book:
        data_from_telephon_book = telephon_book.read() 
        return data_from_telephon_book

def save_data_json():
    with open ('book.json','a',encoding='utf-8') as telephon_book:
         telephon_book.write(json.dumps(convert_data(),ensure_ascii=False))  
         print('  ')

def load_data_json():
    with open('book.json','r',encoding='utf-8')  as telephon_book:
        data_from_telephon_book = json.load (telephon_book) 
        return data_from_telephon_book




#vvod()
#save_data_json()
#print('Данные были успешно сохранены')
text=load_data_json() 
print(text)
print ('Данные были успешно загружены')
