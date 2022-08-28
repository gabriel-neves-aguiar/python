numero = int(input('Digite o primeiro número da Progressão aritmetica: '))
razao = int(input('Digite a razao da progressão aritmetica: '))
termo = 1
while termo < 10:
    termo += 1
    print('{} + {} = '.format(numero, razao), end='')
    numero += razao
print(numero)