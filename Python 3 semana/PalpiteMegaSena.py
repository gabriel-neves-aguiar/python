from random import randint
from time import sleep
palpites = []
numero = 0
jogos = int(input('Quantos jogos você quer gerar? '))
print('-' * 32)
print('{:^32}'.format('PALPITES MEGA SENA'))
print('-' * 32)
for j in range(0, jogos):
    for p in range(0, 6):
        numero = randint(1, 60)
        while numero in palpites:
            numero = randint(1, 60)
        palpites.append(numero)
    palpites.sort()
    print('Jogo {}: {}'.format(j + 1, palpites))
    palpites.clear()
    sleep(1)
print('-' * 32)
print('{:^32}'.format('BOA SORTE!'))
print('-' * 32)
