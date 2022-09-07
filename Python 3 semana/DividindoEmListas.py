numeros = []
pares = list()
impares = list()
continuar = 'S'
while True:
    numeros.append(int(input('Digite o número que quer adicionar: ')))

    continuar = str(input('Quer adicionar mais um número? ')).strip().upper()[0]
    if continuar == 'N':
        break
for n in range(0, len(numeros)):
    if numeros[n] % 2 == 0:
        pares.append(numeros[n])
    else:
        impares.append(numeros[n])
print('=-' * 20)
print('Os números digitado foram:\n{}'.format(numeros))
print('=-' * 20)
print('Você digitou esses números pares:\n{}'.format(pares))
print('=-' * 20)
print('Você digitou esses números impares:\n{}'.format(impares))
print('=-' * 50)