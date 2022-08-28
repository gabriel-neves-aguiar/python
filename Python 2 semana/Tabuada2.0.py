tabuada = int(input('Digite o número que deseja ver a tabuada: '))
for t in range(0, 11):
    print('\033[36m{} x {:2} = {:2}\033[m'.format(tabuada, t, tabuada * t))