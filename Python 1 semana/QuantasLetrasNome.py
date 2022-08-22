n = str(input('Digite seu nome completo: ')).strip()
print(n.upper())
print(n.lower())
print('Seu nome tem {}{}{} letras.'.format('\033[34m', len(n) - n.count(' '), '\033[m'))
print('Seu primeiro nome tem {}{}{} letras.'.format('\033[33m', n.find(' '), '\033[m'))

