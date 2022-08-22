r1 = int(input('Digite o tamanho da primeira reta: '))
r2 = int(input('Digite o tamanho da segunda reta: '))
r3 = int(input('Digite o tamanho da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[35mÉ possível formar um triângulo com essas três retas\033[m')
else:
    print('\033[31mNão é possivel formar um triângulo ccom as retas informadas\033[m')