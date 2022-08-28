altura = float(input('Digite sua altura: '))
peso = int(input('Digite seu peso: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    resultado = str('Abaixo do peso ideal')
elif imc >= 18.5 and imc <25:
    resultado = str('Peso ideal')
elif imc >= 25 and imc < 30:
    resultado = str('Sobrepeso')
elif imc >=30 and imc < 40:
    resultado = str('Obesidade')
elif imc >= 40:
    resultado = str('Obesidade mórbida')
print('Seu status é {}'.format(resultado))