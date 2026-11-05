lön=0.01
dagar=0
summa=0
while lön<10**7:
    lön=lön*2
    summa=summa+lön
    dagar+=1
    if lön>10**7:
        break
print('Det tar',dagar,'dagar att jobba för att komma till 10 miljoner')