maior = 0
menor = 0
for p in range(1, 6):
    peso = int(input('Digite o peso da {}º pessoa: '.format(p)))
    if peso >= maior:
        maior = peso
    if menor == 0:
        menor = peso
    elif peso <= menor:
        menor = peso
    print('O maior peso é {} kg e o menor é {} kg'.format(maior, menor))