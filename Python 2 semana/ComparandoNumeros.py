numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
if numero1 > numero2:
    print('O número {} é maior que o número {}'.format(numero1, numero2))
elif numero2 > numero1:
    print('O número {} é maior que o número {}'.format(numero2, numero1))
elif numero1 == numero2:
    print('O número {} é igual ao número {}'.format(numero1, numero2))