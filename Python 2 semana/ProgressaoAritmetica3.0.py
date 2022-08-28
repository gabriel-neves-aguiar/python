numero = int(input('Digite o primeiro número da Progressão aritmetica: '))
razao = int(input('Digite a razao da progressão aritmetica: '))
termo = 1
acrescimo = 0
while termo != 0:
    termo -= acrescimo
    while termo < 10:
        termo += 1
        print('{} + {} = '.format(numero, razao), end='')
        numero += razao
    print(numero)
    acrescimo -= acrescimo
    acrescimo = int(input('\nDigite o número de termos que quer adicionar:\n[0] Encerrar\n'))
    if acrescimo == 0:
        print('Sua Progressão aritmética terminou no número {} '.format(numero))
        termo = 0
