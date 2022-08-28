from datetime import date
nascimento = int(input('Digite o ano em que o atleta nasceu: '))
idade = date.today().year - nascimento
if idade < 2:
    categoria = str('inapto')
elif idade <= 9:
    categoria = str('Mirim')
elif idade <= 14:
    categoria = str('Infantil')
elif idade <= 19:
    categoria = str('Junior')
elif idade <= 25:
    categoria = str('Sênior')
elif idade > 25:
    categoria = str('Master')
print('O atleta pertence a categoria {}{}{}'.format('\033[34m', categoria, '\033[m'))