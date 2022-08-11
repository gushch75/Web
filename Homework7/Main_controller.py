
import User_interface as Iface
import Input as inp
import Calculator as cl
import Output as ou
import Logger as lg

Iface.Intface("Welcome")
lg.fopen('a')

while(True):
    Iface.Intface("Menu")
    i = int(inp.Variable())
    match i:
        case 1: 
            ou.plog("Mode",str(i))
            vrb = inp.Reader("Ir")
            ou.plog("Variables",vrb[0])
            ou.plog("Result",str(cl.Calculate(vrb)))
            Iface.Intface("End")
            if(int(inp.Variable()) == 2): 
                ou.plog("Exit")
                break
        case 2:
            ou.plog("Mode",str(i))
            vrb = inp.Reader("Comp")
            ou.plog("Variables","("+ vrb[0]+")"+vrb[1]+"("+ vrb[2]+")")
            ou.plog("Result",str(cl.Calculate(vrb)))
            Iface.Intface("End")
            if(int(inp.Variable()) == 2): 
                ou.plog("Exit")
                break
        case 3:
            ou.plog("Mode",str(i))
            ou.viewlog()
            Iface.Intface("End")
            if(int(inp.Variable()) == 2): 
                ou.plog("Exit")
                break
        case 4:
            ou.plog("Mode",str(i))
            print('Запущен выход из программы')
            break
        case _: print("Нет данных")

