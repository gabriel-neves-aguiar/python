contagem = 0
soma = 0
print('\033[31mDigite 999 a qualquer momento para parar!\033[m')
while True:
    numero = int(input('Digite o número que deseja adicionar a soma: '))
    if numero == 999:
        break
    soma += numero
    contagem += 1
print('A soma de todos os {} valores digitados é: {}'.format(contagem, soma))