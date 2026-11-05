import math
radie=float(input('vad är cirkelns radie?:'))
if radie <=0:
    radie=float(input('skriv ett tal större en 0:'))
omkrets=2*radie*math.pi
area=math.pi*radie**2
print(f'cirkelns omkrets:{omkrets:5.2f}' )
print(f'cirkelns area:{area:5.2f}')
