import os
import op


def opSpace(): 
    os.system('cls')
    #COMMAND VALUE = DONE HAHAHA KONTOL CAPE NGENTOT
    # print ('x:', x)
    j = x.split(' ')
    ks = ['1', '2', '3', '4', '5', '6', '7', '8', '9','0']
    keluar = ['quit', 'close', 'end', 'keluar']
    opm = ['+', '-', '*', '/']

    # print(j)
    if j[0] == '//':
        if j[1] == 'help': 
            print ('Help \n')
            print ('Tolong Aku! \n Aku Punya Ini! \n Aku Punya Ini \n Maju Maju Maju! \n Kerja Bagus! \n Mainnya Hebat!')
            op.opr()
        elif j[1] in keluar:
            print ('Bye Bye!')
            global tx
            tx = False
            return tx
            # op.opr()
    # kr = list(x)
    
    
    #skip to 75

    def pbr(): 
        runningKR = True
        if len(str(j[0])) > 1 | len(str(j[2])) == 1: 
            if  len(str(j[2])) > 1:
                print (j[0], 'dan', j[2], 'memiliki value puluhan atau ratusan 1')
            elif len(str(j[2])) == 1:
                print (j[0], 'Memiliki Value Puluhan atau ratusan 1')

        if len(str(j[2])) > 1 | len(str(j[0])) == 1: 
            if  len(str(j[1])) > 1:
                print (j[0], 'dan', j[2], 'memiliki value puluhan atau ratusan 2')
            elif len(str(j[1])) == 1:
                print (j[2], 'Memiliki Value Puluhan atau ratusan 2')

        if len(str(j[0])) > 1 and len(str(j[2])) > 1:
            print(j[0], 'dan', j[2], ', keduanya memiliki value puluhan atau ratusan x')

        if j[0] in ks:
        # print('Pihak Memakai Kalkulator')
            if j[1] in opm:
            
                if j[2] in ks: 
                    if j[1] == opm[0]: 
                        hasil = int(j[0]) + int(j[2])
                    elif j[1] == opm[1]:
                        hasil = int(j[0]) - int(j[2])
                    elif j[1] == opm[2]:
                        hasil = int(j[0]) * int(j[2])
                    elif j[1] == opm[3]: 
                        hasil = int(j[0]) / int(j[2])
                    
                # detector
                    if runningKR == True:
                        print (j[0], j[1], j[2], '=', hasil)

        if j[1] not in opm: 
            print ('Operator', j[1], 'Tidak Di Kenali. Operator Disini Hanya Ada (+, -, *, /)')
            runningKR = False
    # JIKA ANGKA DI VALUE PERTAMA LEBIH DARI 9 ATAU BERVALUE PULUHAN ATAU RATUSAN

    # print(j)
    if int(j[0].isdigit()) == True:
        # int(j[0]).isdigi
        pbr()
        # print ('pengguna menggunakan kalkulator')
    else :
        print ('pengguna tidak menggunakan kalkulator')

def isSpace(TrueOrFalse, value) :
    global x
    x = value
    if TrueOrFalse == True :
        # os.system('cls')
        # print ('Kata Mengandung Space')
        opSpace()
    else :
        os.system('cls')
        print ('Kata Tidak Mengandung Space')
        global tx
        op.opr()
        # opNtSpace()



