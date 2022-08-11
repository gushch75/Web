def Variable():
    return input('№ выбранного пункта : ')

def Reader(i:str):
    match i:
        case "Ir":
            return [input('Вводим выражение: ')]
        case "Comp":
            x = input('Первое значение: ')
            y = input('Второе значение: ')
            z = input('Знак операции: ')
            match z:
                case "+": return [x,'+',y]
                case "-": return [x,'-',y]
                case "*": return [x,'*',y]
                case "/": return [x,'/',y]
                case "^": return [x,'**',y]