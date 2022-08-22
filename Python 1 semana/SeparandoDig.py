num = int(input('Digite um número de 0 a 9999: '))

print('Unidade: {}{}{}'.format('\033[36m', num // 1 % 10, '\033[m'))
print('Dezena: {}{}{}'.format('\033[33m', num // 10 % 10, '\033[m'))
print('Centena: {}{}{}'.format('\033[31m', num // 100 % 10, '\033[m'))
print('Milhar: {}{}{}'.format('\033[35m', num // 1000 % 10, '\033[m'))