s = input('Skriv en text:')
i = len(s)-1
while i >= 0:
    if s[i]==' ' or s[i] =='\t':
        break
    i=i-1

if i < len(s):
    print(f'Sista vita tecken finns på plats nr {i}')
else:
    print('Inget vitt tecken')