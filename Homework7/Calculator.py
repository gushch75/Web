import re

def Calculate (cl):
    if(len(cl) == 1):
        return round(eval(cl[0]),3)
    else:
        match cl[0][1]:
            case "+": return complex(cl[0][0])+complex(cl[0][2])
            case "-": return complex(cl[0][0])-complex(cl[0][2])
            case "*": return complex(cl[0][0])*complex(cl[0][2])
            case "/": return complex(cl[0][0])/complex(cl[0][2])
            case "^": return complex(cl[0][0])**complex(cl[0][2])