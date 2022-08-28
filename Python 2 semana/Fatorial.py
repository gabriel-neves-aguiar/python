print('*****Calculador de fatorial*****')
numero = int(input('Digite um número: '))
fatorial = numero
while fatorial - 1 > 0:
    fatorial -= 1
    print('{} x {} = {}'.format(numero, fatorial, numero * fatorial), end='')
    numero *= fatorial

