from random import randint
v = float(randint(30.0, 200.0))
if v > 80.0:
    print('Seu carro foi multado! Você estava a {}{}{} Km/h'.format('\033[4;31m', v, '\033[m'))
    m = (v - 80) * 7
    print('Terá que pagar o valor de R$ {}{}{}'.format('\033[32m', m, '\033[m'))