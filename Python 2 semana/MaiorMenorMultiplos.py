maior = 0
menor = 0
soma = 0
contador = 0
continuar = 'sim'
while continuar == 'sim':
    numero = float(input('Digite um valor: '))
    if contador == 0:
        maior = numero
        menor = numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    soma += numero
    contador += 1
    continuar = str(input('Você deseja continuar? ')).lower().strip()
media = float(soma // contador)
print('Você digitou {} números'.format(contador))
print('A média dos número digitados é: {} // {} = {}'.format(soma, contador, media))
print('O maior número digitado foi {} e o menor foi {}'.format(maior, menor))