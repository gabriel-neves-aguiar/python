matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(0, 3):
    for l in range(0, 3):
        matriz[c][l] = int(input('Digite o número desejado em [{}], [{}]: '.format(c + 1, l + 1)))
print('_' * 21)
for c in range(0, 3):
    for l in range(0, 3):
        print('|{:^5}|'.format(matriz[c][l]), end='')
    print()
    print('_' * 21)