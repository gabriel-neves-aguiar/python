primeiro = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite a razão da P.A.: '))
for p in range(primeiro, (primeiro + (razao * 10)), razao):
    print(p, end=' > ')