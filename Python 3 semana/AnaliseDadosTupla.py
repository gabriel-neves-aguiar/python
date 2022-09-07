numeros = (int(input('Digite o primeiro valor: ')), int(input('Digite o segundo valor: ')),
           int(input('Digite o terceiro valor: ')), int(input('Digite o quarto valor: ')))
print('Os números digitados foram: ')
print('\nO valor 9 apareceu {} vezes'.format(numeros.count(9)))
if 3 in numeros:
    print('O primeiro número três aparece como {}º número'.format(numeros.index(3) + 1))
print('O números números pares são: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')