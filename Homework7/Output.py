from asyncio.log import logger
import Logger

def plog(i,line:str = None):
    match i:
        case "Mode":
            print("Pежим: " + line)
            Logger.wlog(i,line)
        case "Variables":
            print("Операция : "+ line)
            Logger.wlog(i,line)
        case "Result":
            print("Результат: " + line)
            Logger.wlog(i,line)
        case "Exit":
            Logger.wlog(i)

def viewlog():
    Logger.fopen('r')
    for line in Logger.file:    
        print(line)
    Logger.file.close()
    Logger.fopen('a')
