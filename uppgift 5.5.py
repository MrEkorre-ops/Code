s = input('Skriv en text:')
i = 0
for c in s:
    if c == ' ' or c =='\t':
        break
    i = i + 1
if i < s:
    print(f'Första vita tecken finns på plats nr {i}')
else:
    print('Inget vitt tecken')