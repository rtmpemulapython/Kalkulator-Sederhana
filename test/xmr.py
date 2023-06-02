numberStr = ['1', '2', '3']

x = input('Masukan Nomor 1 - 3: ')

y = x.split(' ')

if y[0] in numberStr: 
    print (y[0], ' TRUE')
else :
    print (y[0], 'FALSE')