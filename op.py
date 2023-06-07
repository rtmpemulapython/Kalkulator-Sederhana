#OPERATOR PAGE
# import os 
# import help_list
import logicapp

xr = logicapp

def opr () : 
    while True:
        

        # nested function
        print ('\n"//help" if u need help\n')
        x = input('$: ')

        # LOGIC
        if x.find(' ') != -1:
                h = True
        else :
                h = False
        xr.isSpace(h, x)

        # res = True
        res = xr.opSpace()

        # cancel / break control diluar file op.py ini
        if res == False:
              break