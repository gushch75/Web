n = input()
summa = 0
 
for digit in n :
    if digit.isdigit():
          summa += int(digit)

print("Сумма:", summa)
