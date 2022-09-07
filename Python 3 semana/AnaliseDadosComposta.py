temporaria = list()
principal = list()
maior = menor = 0
leves = list()
pesadas = list()
continuar = 's'
while True:
    temporaria.append(str(input('Digite o nome da pessoa: ')))
    temporaria.append(float(input('Digite o peso da pessoa: ')))
    principal.append(temporaria[:])
    if maior == 0 and menor == 0:
            maior = menor = temporaria[1]
    else:
        if temporaria[1] > maior:
            maior = temporaria[1]
        elif temporaria[1] < menor:
            menor = temporaria[1]
    temporaria.clear()
    continuar = str(input('Deseja adicionar mais uma pessoa? ')).lower().strip()[0]
    if continuar == 'n':
        break
for p in principal:
    if p[1] == maior:
        pesadas.append(p[0])
    elif p[1] == menor:
        leves.append(p[0])
print('=-' * 25)
print('Você cadastrou {} pessoas'.format(len(principal)))
print('=-' * 25)
print('O maior peso cadastrado foi {}, as pessoas que tem esse peso são: '.format(maior))
print('{}'.format(pesadas))
print('=-' * 25)
print('O menor peso cadastrado foi {}, as pessoas que tem esse peso são: '.format(menor))
print('{}'.format(leves))
print('=-' * 25)