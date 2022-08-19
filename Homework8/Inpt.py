from collections import defaultdict
import os
import json
from sys import path_hooks
import Otpt
file = None
path = 'Base.json'

base = {}
base = defaultdict(list)

def addinbase(FIO,Type,Number):
    global base
    
    base[Type].append({
        'FIO' : FIO,
        'Type': Type,
        'Num': Number
    })

def FindPerson():
    prson = input('Введите точное ФИО для поиска: ')
    global base
    keys = base.keys()
    flag = False
    count = 0
    fbase = {}
    fbase = defaultdict(list)
    for types in keys:
        for i in range(len(base[types])):
            if(base[types][i]['FIO']==prson):
                fbase[types].append(base[types][i])
                flag = True
                count +=1
    if flag == True:
        print(f'Найдено {count} элементов')
        Otpt.PrintJson(fbase)
    else:
        print(f'Элемент {prson} не найден в базе')

def DelPerson():
    prson = input('Введите точное ФИО для удаления: ')
    global base
    keys = base.keys()
    flag = False
    count = 0
    for types in keys:
        for i in range(len(base[types])):
            if(base[types][i]['FIO']==prson):
                base[types].pop(i)
                flag = True
                count += 1
    if flag == True:
        print(f'Удалено {count} элементов')
    else:
        print(f'Элемент {prson} не найден в базе')

def AddPerson():
   addinbase(input('Введите ФИО: '),input('Введите группу: '),input('Введите номер телефона: '))


def SafeBase():
    global file
    global base
    global path

    file = open(path,'w',encoding='utf-8')

    if(file != None):
      
        json.dump(base,file, ensure_ascii=False)
        print ('Данные успешно сохранены')
        file.close()
        file = None


def Variable():
    return int(input('Введите номер действия '))

