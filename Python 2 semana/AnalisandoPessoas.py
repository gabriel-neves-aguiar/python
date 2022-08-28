comparador = 0
soma = 0
contador = 0
for p in range(1, 5):
    nome = str(input('Qual o nome da {}º pessoa? '.format(p)))
    idade = int(input('Qual a idade da {}º pessoa? '.format(p)))
    print('Digite abaixo o sexo da {}º pessoa\n\033[36m[M] Masculino\033[m\n\033[35m[F] Feminino\033[m'.format(p))
    sexo = str(input()).strip().lower()
    soma += idade
    if idade == 0 and sexo == 'm':
        comparador = idade
        velho = str(nome)
    elif idade > comparador and sexo == 'm':
        comparador = idade
        velho = nome
    if sexo == 'f' and idade < 20:
        contador += 1
media = soma / p
print('\033[33mA média da idade do grupo é: {} anos\033[m'.format(media))
print('\033[36mO nome do homem mais velho é: {}\033[m'.format(velho))
print('\033[35m{} mulher(es) tem  menos de 20 anos!\033[m'.format(contador))