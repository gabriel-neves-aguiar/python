total = 0
caros = 0 #produtos que custam mais de 1000 reais
continuar = 's'
barato = 'nenhum' #produto mais barato
baratinho = 0
while True:
    if continuar == 'n':
        break
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
    total += preco
    if preco > 1000:
        caros += 1
    if barato == 'nenhum':
        baratinho = preco
        barato = nome
    if preco < baratinho:
        baratinho = preco
        barato = nome
    continuar = str(input('Você comprará algo mais? ')).lower().strip()[0]
print('Você terá que pagar: \033[32mR$ {:.2f}\033[m'.format(total))
print('Você comprou {} produtos acima de 1000 reais'.format(caros))
print('O produto mais barato que você comprou foi: {}'.format(barato))