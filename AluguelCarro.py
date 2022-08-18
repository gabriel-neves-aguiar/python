p = int(input('Quantos dias você ficou com o carro? '))
d = float(input('Quantos Km você percorreu com o carro alugado? '))
print(f'Você irá pagar R${p * 60} por {p} dias com o carro e mais R${d * 0.15} por ter percorrido{d} Km!')
print(f'Totalizando {(p * 60) + (d * 0.15)}.')
