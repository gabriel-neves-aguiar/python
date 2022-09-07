numeros = list()
temporario = 0
for n in range(0, 5):
    temporario = int(input('Digite o valor que quer adicionar: '))
    if n == 0:
        numeros.append(temporario)
    else:
        if temporario not in numeros:
            if temporario > numeros[- 1]:
                numeros.append(temporario)
            else:
                p = 0
                while p < len(numeros):
                    if temporario < numeros[p]:
                        numeros.insert(p, temporario)
                        break
                    p += 1
print(numeros)