from random import choice
print('Dificuldades:\n[F] \033[36mFácil (1-3)\033[m\n[M] \033[33mMédio (1-5)\033[m\n[D] \033[31mDifícil (1-10)\033[m')
dificuldade = str(input('Digite a dificuldade desejada: ')).strip().upper()[0]
while dificuldade != 'F' and dificuldade != 'M' and dificuldade != 'D':
    dificuldade = str(input('Digite uma dificuldade válida: '))
continuar = 'S'
if dificuldade == 'F':
    print('\033[36mVocê escolheu a dificuldade fácil!\033[m')
    while continuar == 'S':
        disponiveis = [1, 2, 3]
        escolha = choice(disponiveis)
        numero = int(input('Escolha um número de 1 a 3: '))
        if numero == escolha:
            print('\033[32mO número escolhido foi {}.Você acertou!\033[m'.format(escolha))
            continuar = str(input('Quer continuar jogando?\n[S] Sim\n[N] Não\n ')).upper().strip()[0]
        elif numero != escolha:
            print('\033[31mVocê errou! O número escolhido foi {}\033[m'.format(escolha))
            continuar = str(input('Quer tentar de novo? \n[S] Sim\n[N] Não\n')).strip().upper()[0]
if dificuldade == 'M':
    print('\033[33mVocê escolheu a dificuldade média!\033[m')
    while continuar == 'S':
        disponiveis = [1, 2, 3, 4, 5]
        escolha = choice(disponiveis)
        numero = int(input('Escolha um número de 1 a 5: '))
        if numero == escolha:
            print('\033[32mO número escolhido foi {}.Você acertou!\033[m'.format(escolha))
            continuar = str(input('Quer continuar jogando?\n[S] Sim\n[N] Não\n ')).upper().strip()[0]
        elif numero != escolha:
            print('\033[31mVocê errou! O número escolhido foi {}\033[m'.format(escolha))
            continuar = str(input('Quer tentar de novo? \n[S] Sim\n[N] Não\n')).strip().upper()[0]
if dificuldade == 'D':
    print('\033[31mVocê escolheu a dificuldade difícil!\033[m')
    while continuar == 'S':
        disponiveis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        escolha = choice(disponiveis)
        numero = int(input('Escolha um número de 1 a 10: '))
        if numero == escolha:
            print('\033[32mO número escolhido foi {}.Você acertou!\033[m'.format(escolha))
            continuar = str(input('Quer continuar jogando?\n[S] Sim\n[N] Não\n ')).upper().strip()[0]
        elif numero != escolha:
            print('\033[31mVocê errou! O número escolhido foi {}\033[m'.format(escolha))
            continuar = str(input('Quer tentar de novo? \n[S] Sim\n[N] Não\n')).strip().upper()[0]
print('Obrigado por jogar!!!!!')
