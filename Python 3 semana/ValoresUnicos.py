valores = list ()
temporario = 0
continuar = 'S'
while True:
    temporario = (int(input('Digite o valor que quer adicionar: ')))
    if temporario not in valores:
        valores.append(temporario)
        print('Valor adicionado')
    else:
        print('Valor duplicado não inserido')
    continuar = str(input('Você quer continuar? ')).strip().upper()[0]
    if continuar == 'N':
        break
print('A sua lista ficou assim: {}'.format(sorted(valores)))