from random import choice
escolhap = str(input('Digite pedra, papel ou tesoura para começar: ')).lower().strip()
opcoes = ('pedra', 'papel', 'tesoura')
escolhac = choice(opcoes)
print('\033[34mVocê escolheu {}!\033[m'.format(escolhap))
if escolhap == 'pedra':
    if escolhac == 'pedra':
        resultado = str('O computador escolheu {}.\033[33m\nEmpate, jogue novamente!\033[m'.format(escolhac))
    elif escolhac == 'tesoura':
        resultado = str('O computador escolheu {}. \033[32m\nVocê venceu!\033[m'.format(escolhac))
    elif escolhac == 'papel':
        resultado = str('O computador escolheu {}. \033[31m\nVocê perdeu!\033[m'.format(escolhac))
    print('{}'.format(resultado))
elif escolhap == 'papel':
    if escolhac == 'papel':
        resultado = str('O computador escolheu {}.\033[33m\nEmpate, jogue novamente!\033[m'.format(escolhac))
    elif escolhac == 'pedra':
        resultado = str('O computador escolheu {}. \033[32m\nVocê venceu!\033[m'.format(escolhac))
    elif escolhac == 'tesoura':
        resultado = str('O computador escolheu {}. \033[31m\nVocê perdeu!\033[m'.format(escolhac))
    print('{}'.format(resultado))
elif escolhap == 'tesoura':
    if escolhac == 'tesoura':
        resultado = str('O computador escolheu {}.\033[33m\nEmpate, jogue novamente!\033[m'.format(escolhac))
    elif escolhac == 'papel':
        resultado = str('O computador escolheu {}. \033[32m\nVocê venceu!\033[m'.format(escolhac))
    elif escolhac == 'pedra':
        resultado = str('O computador escolheu {}. \033[31m\nVocê perdeu!\033[m'.format(escolhac))
    print('{}'.format(resultado))