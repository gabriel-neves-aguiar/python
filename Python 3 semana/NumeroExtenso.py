numero = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
          'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
          'Dez', 'Onze', 'Doze', 'Treze', 'Catorze',
          'Quinze,', 'Dezesseis', 'Dezessete', 'Dezoito',
          'Dezenove', 'Vinte')
while True:
    escolha = int(input('Digite um número de 0 a 20 que deseja exibir por extenso: '))
    if escolha > 20 or escolha < 0:
        print('Número inválido')
        break
    else:
        print(numero[escolha])