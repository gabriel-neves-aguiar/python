jogador = dict()
numeros = list()
time = list()
total = 0
continuar = 'S'
while True:
    jogador['nome'] = str(input('Digite o nome do jogador: '))
    partidas = int(input('Quantas partidas {} jogou? '.format(jogador['nome'])))
    numeros.clear()
    for p in range(1, partidas + 1):
        numeros.append(int(input('Quantos gols ele fez na partida {}? '.format(p))))
    jogador['gols'] = numeros[:]
    jogador['total'] = sum(numeros)
    time.append(jogador.copy())
    continuar = str(input('Mais algum jogador? ')).strip().upper()[0]
    while continuar != 'S' and continuar != 'N':
        print('Inválido')
        continuar = str(input('Mais algum jogador? ')).strip().upper()[0]
    if continuar == 'N':
        break
print('=-' * 40)
for i in jogador.keys():
    print('{:<15}'.format(i),end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print('{:>3}'.format(k), end='')
    for d in v.values():
        print('{:<15}'.format(str(d)), end='')
    print()
print('-' * 40)
while True:
    codigo = int(input('De que jogador quer os dados? [999] Fechar\n'))
    if codigo == 999:
        break
    if codigo > len(time):
        print('Jogador inválido!')
    else:
        print('Dados do jogador {}'.format(time[codigo]['nome']))
        print('-' * 40)
        for i, g in enumerate(time[codigo]['gols']):
            print('No jogo {} fez {} gols'.format(i + 1, g))
        print('-' * 40)
print('Até a próxima!')
