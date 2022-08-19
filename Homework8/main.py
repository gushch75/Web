import Inpt
import Otpt
from Interface import Interface

Interface('Welcome')

while(True):
    Interface('Menu')
    i = Inpt.Variable()
    match i:
        case 1: 
            Inpt.AddPerson()
            Interface('End')
            if(Inpt.Variable() == 2): 
                break
       
        case 2:
            Inpt.DelPerson()
            Interface('End')
            if(Inpt.Variable() == 2): 
                break
        case 3:
            Inpt.FindPerson()
            Interface('End')
            if(Inpt.Variable() == 2): 
                break
        case 4: 
            Otpt.PrintJson(Inpt.base)
            Interface('End')
            if(Inpt.Variable() == 2): 
                break
        case 5:
            Inpt.SafeBase()
            Interface('End')
            if(Inpt.Variable() == 2): 
                break
        case 6: 
            Inpt.SafeBase()
            break