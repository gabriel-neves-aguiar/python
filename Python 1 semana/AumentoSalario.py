s = float(input('Digite o sálario do funcionario: '))
if s <= 1250.00:
    s = s + (s * (15 / 100))
    print('O novo salario do funcionario é R$ {}{}{}'.format('\033[1;32m', s, '\033[m]'))
else:
    s = s + (s * (10 / 100))
    print('O novo salario do funcionario é R$ {}{}{}'.format('\033[1;32m', s, '\033[m'))