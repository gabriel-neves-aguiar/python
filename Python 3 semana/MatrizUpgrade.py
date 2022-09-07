matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
temporario = pares = terceira = segunda = 0
for c in range(0, 3):
    for l in range(0, 3):
        temporario = int(input('Digite o número desejado em [{}], [{}]: '.format(c + 1, l + 1)))
        if temporario % 2 == 0:
            pares += temporario
        if l == 2:
            terceira += temporario
        if c == 1:
            if segunda == 0:
                segunda = temporario
            elif temporario > segunda:
                segunda = temporario
        matriz[c][l] = temporario
print('_' * 21)
for c in range(0, 3):
    for l in range(0, 3):
        print('|{:^5}|'.format(matriz[c][l]), end='')
    print()
    print('_' * 21)
print('A soma de todos os valores pares digitados vale {}'.format(pares))
print('A soma de todos os valores na terceira coluna vale {}'.format(terceira))
print('O maior valor na segunda linha é {}'.format(segunda))