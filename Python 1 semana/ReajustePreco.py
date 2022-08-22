p = float(input('Digite o preço do produto: '))
print('O preço do produto após o reajuste será: {}{}{}'.format('\033[32m', p - (5/100 * p), '\033[m'))