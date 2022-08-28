valor = int(input('Digite o valor que deseja sacar: '))
restante = valor
cedula = 50
totalcedula= 0
while True:
    if restante >= cedula:
        restante -= cedula
        totalcedula += 1
    else:
        if totalcedula > 0:
            print('{} notas de {}'.format(totalcedula, cedula))
        if restante >= 20:
            cedula = 20
        elif restante >= 10:
            cedula = 10
        elif restante >= 1:
            cedula = 1
        totalcedula = 0
        if restante == 0:
            break