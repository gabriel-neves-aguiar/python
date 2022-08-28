soma = 0
for n in range(1, 7):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        print('{} + {}'.format(soma, numero))
        soma = soma + numero
print('O resultado da soma de todos os pares que digitou é: {}'.format(soma))