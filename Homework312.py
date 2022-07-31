
list_ = [10, 'bla', 2, 1, 'bla', 'qwerty', 6, 6, 'кенни', 'eretet', 'bla', 4]
print (list_)
new_list = sorted([i for i in list_ if isinstance(i, int)])
print("Новый отсортированный список с числами",new_list)

substr=str(input('Введите название элемента, который нужно найти : '))

indexes = []


for i in range(0, len(list_)):
    if list_[i] == substr:
        indexes.append(i)
    elif list_[i] != substr:
        pass
if len(indexes)>1:
   print("Порядковые номера выбранного элемента в списке: ", indexes)
   s= indexes[1]-indexes[0]
   print ("Позиция второго вхождения строки :",s) 
else:
   print ("Позиций второго вхождения строки нет:")  

   