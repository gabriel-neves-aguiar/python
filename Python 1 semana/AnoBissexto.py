from datetime import date
a = int(input('Digite o ano que deseja saber se é bissexto(0 para ano atual): '))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('O ano de {}{}{} é bissexto'.format('\033[7;34;40m', a, '\033[m'))
else:
    print('O ano de {}{}{} não é bissexto'.format('\033[7;31;40m', a, '\033[m'))