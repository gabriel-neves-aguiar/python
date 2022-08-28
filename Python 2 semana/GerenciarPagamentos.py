valor = float(input('Digite o valor do produto: '))
print('''[1] \033[32mÀ vista dinheiro/cheque: 10% de desconto\033[m
[2] \033[35mÀ vista no cartão: 5% de desconto\033[m
[3] \033[36mEm até 2x no cartão: preço formal\033[m 
[4] \033[33m3x ou mais no cartão: 20% de juros\033[m''')
pagamento = int(input('Digite o número correspondente a forma de pagamento desejada: '))
if pagamento == 1:
    preco = valor - (valor * 10 / 100)
elif pagamento == 2:
    preco = valor - (valor * 5 / 100)
elif pagamento == 3:
    preco = valor
elif pagamento == 4:
    preco = valor + (valor * 20 /100)
    vezes = int(input('Em quantas vezes quer parcelar? '))
    parcela = preco / vezes
print('O valor a ser pago é de R$ {}{:.2f}{} em {} parcelas de R$ {}{:.2f}{}!'.format('\033[32m', preco, '\033[m', vezes, '\033[32m', parcela, '\033[m'))