from datetime import date
nascimento = 0
maiores = 0
menores = 0
for a in range(1, 8):
    nascimento = int(input('Digite o ano de nascimento da {}º pessoa: '.format(a)))
    if date.today().year - nascimento >= 18:
        maiores += 1
        print('Maior de idade')
    else:
        menores += 1
        print('Menor de idade')
print('Das pessoas informadas, {} são maiores de idade e {} são menores de idade'.format(maiores, menores))