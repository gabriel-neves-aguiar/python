n = int(input('Digite o número desejado: '))
if n % 2 == 0:
    print(f'O número {n} é par!')
else:
    if n % 2 == 1:
        print(f'O número {n} é impar!')
    else:
        print(f'{n} inválido')