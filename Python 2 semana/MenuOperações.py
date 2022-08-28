operacao = 'começar'
numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
while operacao != 0:
    soma = numero1 + numero2
    multiplica = numero1 * numero2
    operacao = int(input('''Digite a operação que deseja realizar:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Trocar números
    [0] Sair
    '''))
    if operacao == 1:
        print('O resultado de {} + {} é {}'.format(numero1, numero2, soma))
    if operacao == 2:
        print('O resultado de {} * {} é {}'.format(numero1, numero2, multiplica))
    if operacao == 3:
        if numero1 > numero2:
            print('O número {} é maior que o número {}!'.format(numero1, numero2))
        elif numero2 > numero1:
            print('O número {} é maior que o número {}!'.format(numero2, numero1))
        else:
            print('Os dois números são iguais!')
    if operacao == 4:
        numero1 = float(input('Digite o primeiro número: '))
        numero2 = float(input('Digite o segundo número: '))