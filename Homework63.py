path = 'file1.txt'
data = open(path, 'r')
for line in data:
 print('Текст считанный из файла:',line)



def rle_encode(data):
    if not data:
        return ''

    

    count = 0
    prev_char = ''
    encode = ''

    for char in data:
        if char != prev_char:
            if prev_char:
                encode += str(count) + prev_char
                prev_char = char
                count = 1
            else:
                prev_char = char
                count += 1
        else:
            count += 1
    encode += str(count) + prev_char
    return encode

print('Закодированный файл :',rle_encode(line))

path = 'file2.txt'
data = open(path, 'r')
for line1 in data:
 print('Текст считанный из файла:',line1)
#data.close()


def rle_decode(data): #декодирование
    decode = '' 
    count = '' 
    for char in data:
       if char.isdigit():
          count += char 
       else:  
            decode += char * int(count) 
            count = '' 
    return decode
decoded_val = rle_decode(line1) 
print('Декодированный файл:',decoded_val)
