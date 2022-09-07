boletim = []
aluno = []
while True:
    aluno.append(str(input('Digite o nome do aluno: ')))
    primeira = (float(input('Digite a primeira nota do aluno: ')))
    segunda = (float(input('Digite a segunda nota do aluno: ')))
    media = float((primeira + segunda) / 2)
    aluno.append(primeira)
    aluno.append(segunda)
    aluno.append(media)
    boletim.append(aluno[:])
    aluno.clear()
    continuar = str(input('Quer adicionar mais um aluno? ')).strip().upper()[0]
    if continuar == 'N':
        break
print('=-' * 30)
print('{:<4} {:<10} {:>8}'.format('No.', 'NOME', 'MÉDIA'))
print('-' * 30)
for d in range(1, len(boletim)):
    print('{:<4} {:<10} {:>8.1f}'.format(d, boletim[d][0], boletim[d][3]))
print('-' * 30)
while True:
    numero = int(input('Digite o número do aluno que quer visualizar as notas:\n[999] Fechar\n'))
    if numero == 999:
        break
    print('O aluno {} tirou {} na 1ª prova e {} na 2ª prova'.format(boletim[numero][0], boletim[numero][1], boletim[numero][2]))
    if boletim[numero][3] >= 7:
        print('\033[42mAluno aprovado\033[m com média {}'.format(boletim[numero][3]))
    else:
        print('\033[31mAluno reprovado\033[m com média {}'.format(boletim[numero][3]))
print('Até mais!')