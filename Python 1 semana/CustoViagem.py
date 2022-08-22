d = float(input('Digite a distância até o destino da sua viagem em Km: '))
if d <= 200:
    p = d * 0.50
else:
    if d > 200:
        p = d * 0.45
print('O valor da sua viagem será: R$ {}{}{}'.format('\033[1;32;40m', p, '\033[m'))