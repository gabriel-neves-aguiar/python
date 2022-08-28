print('Para encerrar, digite qualquer valor negativo!')
contador = tabuada = numero = 0
while True:
    numero = int(input('Digite o número que deseja visualizar a tabuada: '))
    if numero < 0:
        break
    while contador < 11:
        tabuada = numero * contador
        print('{} x {} = {}'.format(numero, contador, tabuada))
        contador += 1
    contador = 0
print('Até mais!')