from random import randint
from time import sleep
from operator import itemgetter
ranking = list()
jogadas = {'jogador1': randint(1, 6),
           'jogador2': randint(1, 6),
           'jogador3': randint(1, 6),
           'jogador4': randint(1, 6)}
for k, v in jogadas.items():
    print('{} tirou {} no dado.'.format(k, v))
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
print('=-' * 30)
for i, v in enumerate(ranking):
    print('{} lugar: {} com {}'.format(i + 1, v[0], v[1]))
    sleep(1)

