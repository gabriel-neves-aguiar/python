jogador = dict()
numeros = list()
total = 0
jogador['nome'] = str(input('Digite o nome do jogador: '))
partidas = int(input('Quantas partidas {} jogou? '.format(jogador['nome'])))
for p in range(1, partidas + 1):
    numeros.append(int(input('Quantos gols ele fez na partida {}? '.format(p))))
jogador['gols'] = numeros[:]
jogador['total'] = sum(numeros)
print('=-' * 30)
print(jogador)
print('=-' * 30)
for k, v in jogador.items():
    print('O campo {} é {}'.format(k, v))
print('=-' * 30)
print('O jogador {} jogou {} partidas.'.format(jogador['nome'], partidas))
for k, v in enumerate(numeros):
   print('=> Na {}ª partida, fez {} gols.'.format(k + 1, v))
print('{} fez um total de {} gols!'.format(jogador['nome'], jogador['total']))
print('=-' * 30)