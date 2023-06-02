#OPERATOR PAGE
import os 
# import help_list
import logicapp

xr = logicapp
# global x
# x = 'kok g masuk yah'

def opr () : 
    # os.system('cls')
    # koj = ml
    # tof = True
    # if koj == True:
    #     tof = True
    # elif koj == False:
    #      tof = False
    # global tof
    # xr.opTF()
    while True:
        # h = None
        # x = None
        

        # nested function
        print ('\n "//help" if u need help\n')
        x = input('$: ')

        # LOGIC
        if x.find(' ') != -1:
                h = True
        else :
                h = False
        # y = x.split(" ")w
        # return x
        xr.isSpace(h, x)

        # res = True
        res = xr.opSpace()

        # cancel / break control diluar file op.py ini
        # print ('\n', res, '\n')
        if res == False:
              break