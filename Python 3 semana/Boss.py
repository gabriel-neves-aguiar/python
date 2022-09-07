pessoas = list()
mulheres = list()
velhas = list()
cadastro = dict()
contagem = 0
soma = 0
while True:
    cadastro['nome'] = str(input('Nome: '))
    sexo = str(input('Sexo [M / F]: ')).strip().upper()[0]
    while sexo != 'M' and sexo != 'F':
        print('Sexo inválido!')
        sexo = str(input('Sexo [M / F]: ')).strip().upper()[0]
    cadastro['sexo'] = sexo
    cadastro['idade'] = int(input('Idade: '))
    pessoas.append(cadastro.copy())
    contagem += 1
    soma += cadastro['idade']
    continuar = str(input('Deseja adicionar mais alguém? [S / N]: ')).strip().upper()[0]
    if sexo == 'F':
        mulheres.append(cadastro.copy())
    while continuar != 'S' and continuar != 'N':
        print('Inválido')
        continuar = str(input('Deseja adicionar mais alguém? [S / N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
media = soma / contagem
print('A) Ao todo, {} pessoas foram cadastradas;'.format(contagem))
print('B) A média de idade das pessoas cadastradas é {:.1f} anos;'.format(media))
print('C) As mulheres cadastradas são: ', end='')
for p in range(0, len(mulheres)):
    print('{} '.format(mulheres[p]['nome']), end='')
for p in range(0, len(pessoas)):
    if pessoas[p]['idade'] > media:
        velhas.append(pessoas.copy()[p])
print('\nD) As pessoas mais velhas que a média de idade são: ')
for v in range(0, len(velhas)):
    print(' => nome = {}; sexo = {}; idade = {};'.format(velhas[v]['nome'], velhas[v]['sexo'], velhas[v]['idade']))
