


# def fibo(n):
#     if n in [1,2] :
#           return 1
#     else :
#           return fibo(n)+fibo(n-2)       
# list=[]
# x= int (input('Введите число элементов '))
# for i in range (1,x+1):
    # list.append (fibo(i))
    # print (list)
import json 
a= int ( input('Введите число :'))

def numprint(x):
  x=list(range(-x,x+1))
  return x

b=numprint(a)
print(b)
with open('data.json','w',encoding='utf-8') as fh:
    fh.write(json.dumps(b,ensure_ascii=False))
    print ('Данные в формате json успешно загружены')
with open('data.txt','w') as fh:
    fh.write(str(b))
    print ('Данные в формате txt успешно загружены')
