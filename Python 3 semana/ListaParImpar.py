numeros = [[], []]
num = 0
pares = list()
impares = list()
for n in range(1, 8):
    num = (int(input('Digite o número que quer adicionar: ')))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
    print('Número adicionado com sucesso!')
print(numeros)
print('Os números pares digitados foram:\n{}'.format(sorted(numeros[0])))
print('Os números impares digitados foram:\n{}'.format(sorted(numeros[1])))