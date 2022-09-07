alunos = dict()
boletim = []
continuar = 'S'
while True:
    alunos['nome'] = str(input('Digite o nome do aluno: '))
    primeira = float(input('Digite a primeira nota do aluno: '))
    while primeira > 10 or primeira < 0:
        print('Número inválido!')
        primeira = float(input('Digite a primeira nota do aluno: '))
    segunda = float(input('Digite a segunda nota do aluno: '))
    while segunda > 10 or segunda < 0:
        print('Número inválido!')
        segunda = float(input('Digite a segunda nota do aluno: '))
    alunos['media'] = float(primeira + segunda) / 2
    if alunos['media'] >= 7:
        alunos['situacao'] = str('\033[32maprovado\033[m')
    elif 7 > alunos['media'] > 4:
        alunos['situacao'] = str('\033[33mem recuperação\033[m')
    else:
        alunos['situacao'] = str('\033[31mreprovado\033[m')
    boletim.append(alunos.copy())
    continuar = str(input('Deseja adicionar mais um aluno?')).strip().upper()[0]
    if continuar == 'N':
        break
print('=-' * 40)
for b in range(0, len(boletim)):
    print('O aluno {} teve como média {} e por isso ficou {}!'.format(boletim[b]['nome'], boletim[b]['media'], boletim[b]['situacao']))
print('=-' * 40)
