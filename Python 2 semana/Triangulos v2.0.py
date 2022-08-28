lado1 = float(input('Digite o comprimento do primeiro lado: '))
lado2 = float(input('Digite o comprimento do segundo lado '))
lado3 = float(input('Digite o comprimento do terceiro lado: '))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    if lado1 == lado2 == lado3:
        triangulo = str('Equilátero')
    elif lado1 != lado2 != lado3 != lado1:
        triangulo = str('Escaleno')
    else:
        triangulo = str('Isósceles')
    print('O triangulo formado é um {}{}{}'.format('\33[36m', triangulo, '\033[m'))
else:
    print('\033[31mOs lados informados não formam um triângulo.\033[m')