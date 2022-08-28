numero = 0
soma = 0
operacoes = 0
print('[999] Parar')
while numero != 999:
    numero = int(input('Digite um valor: '))
    if numero != 999:
        print('{} + {}'.format(soma, numero))
        soma += numero
        operacoes += 1
print('\33[34mNo total, você digitou {} números e o resultado da soma deles é {}!\033[m'.format(operacoes, soma))