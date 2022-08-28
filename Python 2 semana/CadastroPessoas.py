continuar = 's'
maiores= 0 #pessoas acima de 18
homens = 0 #homens cadastrados
mulheres = 0 #Mulheres abaixo de 20
while True:
    if continuar == 'n':
        break
    sexo = str(input('Digite o sexo da pessoa: \n[M] Masculino\n[F] Feminino\n')).lower().strip()[0]
    idade = int(input('Digite a idade da pessoa: '))
    if idade > 18 and idade < 130:
        maiores += 1
    if sexo == 'm' and idade < 130:
        homens += 1
    if sexo == 'f' and idade < 20:
        mulheres += 1
    continuar = str(input('Você deseja continuar? ')).strip().lower()[0]
print('\nNo total, {} pessoas têm mais de 18 anos!'.format(maiores))
print('Ao todo, {} homens foram cadastrados!'.format(homens))
print('{} mulheres com menos de 20 anos foram cadastrados!'.format(mulheres))