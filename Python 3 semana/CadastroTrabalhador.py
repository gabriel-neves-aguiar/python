from datetime import date
funcionario = dict()
funcionario['nome'] = str(input('Digite o nome do funcionário: '))
sexo = str(input('Digite o sexo do funcionario:\n[M] Masculino\n[F] Feminino\n')).strip().upper()[0]
funcionario['nascimento'] = int(input('Digite o ano que {} nasceu: '.format(funcionario['nome'])))
funcionario['carteira'] = int(input('Digite o número da carteira de trabalho ([0] Nenhum)\n'))
idade = date.today().year - funcionario['nascimento']
if funcionario['carteira'] != 0:
    funcionario['contratacao'] = int(input('Digite o ano de contratação de {}: '.format(funcionario['nome'])))
    funcionario['salario'] = float(input('Digite o salário de {}: '.format(funcionario['nome'])))
    if sexo == 'M':
        contribuicao = funcionario['contratacao'] + 20
        aposentadoria = contribuicao - funcionario['nascimento']
        if aposentadoria >= 65:
            funcionario['aposentadoria'] = aposentadoria
        else:
            funcionario['aposentadoria'] = 65
    else:
        contribuicao = funcionario['contratacao'] + 15
        aposentadoria = contribuicao - funcionario['nascimento']
        if aposentadoria >= 62:
            funcionario['aposentadoria'] = aposentadoria
        else:
            funcionario['aposentadoria'] = 62
else:
    funcionario['carteira'] = 'não cadastrado como funcionário!'
print('=-' * 30)
for k, v in funcionario.items():
    print('O campo \033[33m{}\033[m tem cadastrado \033[36m{}\033[m'.format(k, v))
