palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print('\nNa palavra {}, temos como vogais '.format(p), end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')