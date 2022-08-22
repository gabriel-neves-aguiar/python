r = float(input('Quantos reais você tem na carteira? '))
print('Você pode comprar {}{:.1f}{} dólares'.format('\033[1;32m', r // 3.27, '\033[m'))
