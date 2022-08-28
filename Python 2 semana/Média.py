nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segundo nota: '))
media = (nota1 + nota2) / 2
if media >= 7.0:
    print('Sua média foi {}. \033[32mParabéns, você foi aprovado!\033[m'.format(media))
elif media < 7.0 and media >= 5.0:
    print('Sua média foi {}. \033[33mVocê está de recuperação.\033[m'.format(media))
elif media < 5.0:
    print('Sua média foi {}. \033[31mVocê foi reprovado.\033[m'.format(media))