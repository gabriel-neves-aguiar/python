expressao = str(input('Digite a expressão para verificar se é válida:\n'))
validador = list()
for parentese in expressao:
    if parentese == '(':
        validador.append('(')
    elif parentese == ')':
        if len(validador) > 0:
            validador.pop()
        else:
            validador.append(')')
            break
if len(validador) == 0:
    print('A expressão é válida!')
else:
    print('A expressão é inválida!')