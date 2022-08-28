numero = int(input('Digite um número: '))
contador = 0
for n in range(1, numero + 1):
    if numero % n == 0:
        contador += 1
        print('\033[32m', end='')
    else:
        print('\033[m', end='')
    print('{} '.format(n), end='',)
if contador == 2:
    print('\033[34m\nO número {} é primo!\033[m'.format(numero))
elif contador == 1:
    print('\033[34m\nO número {} é primo!\033[m'.format(numero))
else:
    print('\033[31m\nO número {} não é primo, pois foi divisível por {} números!\033[m'.format(numero, contador))