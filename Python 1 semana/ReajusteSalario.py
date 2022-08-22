s = float(input('Digite o salário do funcionário: '))
print('O salário após o reajuste será de: {}{}{}'.format('\033[32m', s + (s * 15/100), '\033[m'))