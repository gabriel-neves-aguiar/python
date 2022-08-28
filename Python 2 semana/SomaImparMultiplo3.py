soma = 0
contador = 0
for impar in range(1, 501, 2):
    if impar % 3 == 0:
        contador = contador + 1
        soma = soma + impar
print('A soma de todos os números múltiplos de 3 impares de 1 a 500 é: {}'.format(soma))
print('Total de números somados: {}'.format(contador))