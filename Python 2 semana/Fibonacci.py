elementos = int(input('Digite o número de elementos da sequência de fibonacci que deseja exibir: '))
sequencia = 0
anterior = 0
proximo = 0
termo = 0
while termo < elementos - 1:
    if sequencia != 0:
        print('{} > '.format(sequencia), end='')
        anterior = sequencia
        sequencia = proximo
        proximo = sequencia + anterior
    elif sequencia == 0:
        print('{} > '.format(sequencia), end='')
        anterior = sequencia
        sequencia += 1
        proximo = anterior + sequencia
    termo += 1
print('{}'.format(sequencia), end='')
