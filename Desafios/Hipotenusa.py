from math import hypot
o = float(input('Digite o comprimento do cateto oposto: '))
a = float(input('Digite o comprimento do cateto adjacente: '))
h = hypot(o,a)
print('A hipotenusa do triângulo mencionado é: {}'.format(h))