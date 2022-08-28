restante = 0
resto = 0
operacao = 's'
while True:
    if operacao == 'n':
        break
    valor = int(input('Digite o valor que deseja sacar: '))
    restante = valor
    cinquenta = valor // 50
    restante = valor % 50
    vinte = restante // 20
    restante = ((valor % 50) % 20)
    dez = restante // 10
    restante = (((valor % 50) % 20) % 10)
    um = restante // 1
    print('Você receberá:')
    print('{} notas de 50 reais\n{} notas de 20 reais\n{} notas de 10 reais\n{} moedas de 1 real'.format(cinquenta, vinte, dez, um))
    operacao = str(input('Está em horário de funcionamento? ')).lower().strip()[0]