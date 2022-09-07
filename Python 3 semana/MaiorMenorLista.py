numeros = []
maior = menor = 0
for n in range(0, 5):
    numeros.append(int(input('Digite o número que quer adicionar na {}ª posição: '.format(n + 1))))
    if n == 0:
        maior = menor = numeros[n]
    else:
        if numeros[n] > maior:
            maior = numeros[n]
        if numeros[n] < menor:
            menor = numeros[n]
print('Você digitou os valores: {}'.format(numeros))
print('O maior valor é {} e está na posição '.format(maior),end='')
for i, v in enumerate(numeros):
    if v == maior:
        print(i + 1, end='...')
print('\nO menor valor é {} e está na posição '.format(menor), end='')
for i, v in enumerate(numeros):
    if v == menor:
        print(i + 1, end='...')
