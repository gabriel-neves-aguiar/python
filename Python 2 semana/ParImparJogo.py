from random import randint
soma = 0
vitorias = 0
while True:
    parimpar = str(input('Vamos jogar par ou ímpar?\n[P] Par\n[I] Impar\n[S] Sair\n')).lower().strip()[0]
    if parimpar == 's':
        break
    if parimpar == 'p':
        print('Você escolheu par!')
        jogador = int(input('Quantos dedos você coloca? '))
        computador = randint(1, 11)
        soma = jogador + computador
        print('Você colocou {} dedos'.format(jogador))
        print('A CPU colocou {} dedos'.format(computador))
        if soma % 2 == 0:
            print('\033[36mVocê ganhou!\033[m\n')
            vitorias += 1
        elif soma % 2 != 0:
            break
    elif parimpar == 'i':
        print('Você escolheu impar!')
        jogador = int(input('Quantos dedos você coloca? '))
        computador = randint(1, 11)
        soma = jogador + computador
        print('Você colocou {} dedos'.format(jogador))
        print('A CPU colocou {} dedos'.format(computador))
        if soma % 2 == 0:
            break
        elif soma % 2 != 0:
            print('\033[36mVocê ganhou!\033[m\n')
            vitorias += 1
print('\033[31mGAME OVER\033[m')
print('\033[32mVocê conseguiu {} vitórias consecutivas!\033[m'.format(vitorias))