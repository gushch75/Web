logfile = 'log.txt'
file = None

def fopen(mode):
    global file
    global logfile
    if(file == None):
        file = open(logfile,mode)
    else:
        file.close()
        file = open(logfile,mode)

def fclose():
    global file
    if(file != None):
        wlog("Exit")
        file.close()

def wlog(flag,line:str = None):
    global file
    if(file != None):
        match flag:
            case "Mode":
                file.write(f"Pежим: {line}\n")
            case "Variables":
                file.write(f"Операция: {line}\n")
            case "Result":
                file.write(f"Результат: {line}\n")
            case "Exit":
                file.write(f"Выход\n")
