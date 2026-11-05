min=int(input('Hur många minuter ringer du per månad?'))
if min <=33:
    print ('du bör ta kontant abonnemang')
elif min <=66:
    print ('du bör ta normal abonnemang')
else:
    print('du bör ta plus abonnemang')