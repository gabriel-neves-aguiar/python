from math import floor
casa = int(input('Qual o valor da casa em R$? '))
salario = float(input('Quanto você recebe de salário? '))
ano = int(input('Em quantos anos você pretende pagar? '))
parcela = salario * 30 // 100
alternativa = casa // parcela
mes = (casa // (ano * 12))
if ano <= 30:
    if mes <= parcela:
        print('\033[36mParabéns, seu empréstimo foi aprovado!\033[m')
        print('Você terá que pagar {}{}{} parcelas mensais de R$ {}{}{}.'.format('\033[7;31m', parcela, '\033[m', '\033[32m', mes, '\033[m'))
    elif alternativa <= 30 * 12:
        print('\033[31mNão podemos aprovar seu empréstimo nas condições acima\033[m.')
        print('Porém, podemos oferecer uma condição em que pagará a casa em {}{} parcelas de R$ {}{}'.format('\033[36m', floor(alternativa), parcela,'\033[m'))
        print('Desta forma, pagaria o empréstimo em {}{} anos e {} meses{}.'.format('\033[36m', floor(alternativa // 12), floor(alternativa % 12), '\033[m'))
    else:
        print('\033[31mSinto muito, seu empréstimo não foi aprovado\033[m.')
else:
    print('Não foi possível aprovar seu empréstimo,\033[31m período de pagamento muito longo\033[m.')