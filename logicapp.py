# LOGIC APP

import os
import op


def opSpace(): 
    os.system('cls')
    #COMMAND VALUE = DONE HAHAHA KONTOL CAPE NGENTOT
    j = x.split(' ')
    ks = ['1', '2', '3', '4', '5', '6', '7', '8', '9','0']
    keluar = ['quit', 'close', 'end', 'keluar']
    command = ['help', 'credit']
    opm = ['+', '-', '*', '/']

    if j[0] == '//':
        if j[1] == command[0]: 
            print ('Help List: \n')
            print ('Sekedar Informasi Bahwa Kalkulator Ini Menggunakan Sistem Atau Pola Perhitungan Operator, \nyaitu sebuah perhitungan dimana kali (*) adalah yang diutamakan, \nlalu bagi (/), tambah(+) dan kurang(-)')
            print ('\n // quit (Untuk Keluar Dari Proggram) \n // help (Untuk Menampilak Help List Yang Ada Disini) \n // credit (untuk menampilkan developer)')
            print ('\n\n(Kalkulator Ini Hanya Menerima Maksimal Input 3 penjumlahan, \nlebih dari itu system akan eror dengan sendirinya karna developer \nmalas melanjutkan proggram ini)')
            op.opr()
        elif j[1] in keluar:
            print ('Bye Bye!')
            global tx
            tx = False
            return tx
        elif j[1] == command[1]:
            print('Credit: \n')
            print('Dibuat oleh kasih sayang dan Cinta\n')
            print('Instagram: @rtm.nyata\nGithub: @rtmpemulapython && @HiiIamDev\nFacebook: @Rizky Tegar Milo \n(ling: https://www.facebook.com/profile.php?id=100046696805724)')
            print('\n\nDibuat Sendirian :( g ada temen yg sefrekuensi ama gw.\njadi buat lu boleh tuh jadi ayang aku dm aja ig aku >///< (laki skip aja ajg kecuali mau temenan)')
            print('\n\nVersion: 1.0.0')
        else: 
            print ('Perintah', j[1], 'Tidak Dikenali, "// help" untuk meminta bantuan')
    
    def pbr(): 
        global runningKR
        runningKR = True
        # perbandingan jika operator tidak dikenali maka perintah tidak akan dilaksanakan
        def isKelebihan():
            global runningKR
            if j[1] not in opm:
                print ('Operator', j[1], 'Tidak Dikenali, Mohon mengisi dengan (+, -, *, /) atau \n"// help" untuk meminta bantuan')
                runningKR = False
            elif len(j) > 4:
                if j[3] not in opm:
                    print ('Operator', j[3], 'Tidak Dikenali, Mohon mengisi dengan (+, -, *, /) atau \n"// help" untuk meminta bantuan')
                    runningKR = False
            elif j[1] not in opm and len[j] > 4:
                if j[3] not in opm:
                    print ('Operator', j[1], 'dan', j[3], 'Tidak Dikenali, Mohon mengisi dengan (+, -, *, /) atau \n"// help" untuk meminta bantuan')
            
            

        isKelebihan()
        # namanya emang aneh hahah isKelebihan :V

        def operatorPlus():
            # opm = 0 = +, 1 = -,  2 = *, 3 = /
            global hasil
            if j[1] == opm[0]: 
                if j[3] == opm[0]:
                    hasil = int(j[0]) + int(j[2]) + int(j[4])
                elif j[3] == opm[1]:
                    hasil = int(j[0]) + int(j[2]) - int(j[4])
                elif j[3] == opm[2]:
                    hasil = int(j[0]) + int(j[2]) * int(j[4])
                elif j[3] == opm[3]:
                    hasil = int(j[0]) + int(j[2]) / int(j[4])

            if j[1] == opm[1]: 
                if j[3] == opm[0]:
                    hasil = int(j[0]) - int(j[2]) + int(j[4])
                elif j[3] == opm[1]:
                    hasil = int(j[0]) - int(j[2]) - int(j[4])
                elif j[3] == opm[2]:
                    hasil = int(j[0]) - int(j[2]) * int(j[4])
                elif j[3] == opm[3]:
                    hasil = int(j[0]) - int(j[2]) / int(j[4])

            if j[1] == opm[2]: 
                if j[3] == opm[0]:
                    hasil = int(j[0]) * int(j[2]) + int(j[4])
                elif j[3] == opm[1]:
                    hasil = int(j[0]) * int(j[2]) - int(j[4])
                elif j[3] == opm[2]:
                    hasil = int(j[0]) * int(j[2]) * int(j[4])
                elif j[3] == opm[3]:
                    hasil = int(j[0]) * int(j[2]) / int(j[4])

            if j[1] == opm[3]: 
                if j[3] == opm[0]:
                    hasil = int(j[0]) / int(j[2]) + int(j[4])
                elif j[3] == opm[1]:
                    hasil = int(j[0]) / int(j[2]) - int(j[4])
                elif j[3] == opm[2]:
                    hasil = int(j[0]) / int(j[2]) * int(j[4])
                elif j[3] == opm[3]:
                    hasil = int(j[0]) / int(j[2]) / int(j[4])

            if runningKR == True:
                print(j[0], j[1], j[2], j[3], j[4], '=', hasil)


        def operator(): 
            global hasil, runningKR
            if j[1] == opm[0]: 
                hasil = int(j[0]) + int(j[2])
            elif j[1] == opm[1]:
                hasil = int(j[0]) - int(j[2])
            elif j[1] == opm[2]:
                hasil = int(j[0]) * int(j[2])
            elif j[1] == opm[3]: 
                hasil = int(j[0]) / int(j[2])
            
            if runningKR == True:
                print (j[0], j[1], j[2], '=', hasil)
            
        if len(str(j[0])) > 1 | len(str(j[2])) == 1: 
            if  len(str(j[2])) > 1:
                if len(j) > 4:
                    if len(str(j[4])) > 1:
                        operatorPlus()
                    elif len(str(j[4])) == 1:
                        operatorPlus()
                else :
                    operator()

            elif len(str(j[2])) == 1:
                if len(j) > 4:
                    if len(str(j[4])) > 1:
                        operatorPlus()
                    elif len(str(j[4])) == 1:
                        operatorPlus()
                else :
                    operator()

        if len(str(j[2])) > 1 | len(str(j[0])) == 1: 
            if  len(str(j[1])) > 1:
                if len(j) > 4:
                    if len(str(j[4])) > 1:
                        operatorPlus()
                    elif len(str(j[4])) == 1:
                        operatorPlus()
                else :
                    operator()

            elif len(str(j[1])) == 1:
                if len(j) > 4:
                    if len(str(j[4])) > 1:
                        operatorPlus()
                    elif len(str(j[4])) == 1:
                        operatorPlus()
                else: 
                    operator()
        
        if len(str(j[0])) > 1 and len(str(j[2])) > 1:
            if len(j) > 4:
                if len(str(j[4])) > 1:
                    operatorPlus()
                elif len(str(j[4])) == 1:
                    operatorPlus()
            else :
                operator()

        if j[0] in ks:
            if j[1] in opm:
            
                if j[2] in ks:
                    if len(j) > 4:
                        if len(str(j[4])) > 1:
                            operatorPlus()
                        elif len(str(j[4])) == 1:
                            operatorPlus()
                    else :
                        operator()
    
    #DETECTOR 
    # JIKA ANGKA DI VALUE PERTAMA LEBIH DARI 9 ATAU BERVALUE PULUHAN ATAU RATUSAN

    global runningKR
    if j[0].isdigit() == True:
        if j[2].isdigit() == True:
            if len(j) > 4:
                if j[4].isdigit() == True:
                    pbr()
                else:
                    runningKR = False
            else:
                pbr()
        elif j[2].isdigit() == False:
            runningKR = False

    elif j[0].isdigit() == False:
        runningKR = False

def isSpace(TrueOrFalse, value) :
    global x
    x = value
    if TrueOrFalse == True :
        opSpace()
    else :
        os.system('cls')
        print ('Kata Tidak Mengandung Space')
        global tx
        op.opr()


# DIBUAT OLEH: @rtmpemulapython
# BUAT LU YANG MAU MALING GW TANDAIN MUKALU ANJING


