största_tal=0
Minsta_tal=float("inf")
while True:
    tal=int(input('skriv ett tal'))
    if tal<0:
        break
    if tal>största_tal:
        största_tal=tal
    if tal<Minsta_tal:
        Minsta_tal=tal
print('minstal tal är' ,Minsta_tal , 'största tal är' ,största_tal)