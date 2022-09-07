numeros = list()
contagem = 0
continuar = 'S'
while True:
    numeros.append(int(input('Digite o número que quer adicionar: ')))
    continuar = str(input('Quer adicionar mais um valor? ')).upper().strip()[0]
    if continuar == 'N':
        break
print('Você digitou {} números!'.format(len(numeros)))
numeros.sort(reverse=True)
print(numeros)
if 5 in numeros:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não está na lista!')