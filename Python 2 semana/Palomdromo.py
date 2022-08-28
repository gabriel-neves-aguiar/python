frase = str(input('Digite uma frase: ')).lower().strip()
palavras = frase.split()
juntas = ''.join(palavras)
inversa = ''
for f in range(len(juntas) -1, -1, -1):
    inversa += juntas[f]
print(juntas, inversa)
if inversa == juntas:
    print('A frase digitada é um palíndromo!')
else:
    print('\033[31m\nA frase digitada não é um palíndromo!\033[m')