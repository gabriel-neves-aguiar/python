c = float(input('Digite a temperatura em ºC: '))
print('A temperatura de {}{}{} Celsius, corresponde a {}{}{} Fahrenheit'.format('\033[1;34m', c, '\033[m', '\033[1;36m', (c * 9 / 5) + 32, '\033[m'))