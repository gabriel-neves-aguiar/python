from random import randint
numeros = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
print(numeros)
ordenados = sorted(numeros)
print('Menor: {}'.format(ordenados[0]))
print('Maior: {}'.format(ordenados[4]))