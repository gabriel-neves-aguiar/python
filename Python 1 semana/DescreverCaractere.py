a = input('Digite algo: ')
print('\033[34mÉ alpha?\033[m', a.isalpha())
print('\033[37mÉ númerico?\033[m', a.isnumeric())
print('\033[32mÉ alphanúmerico?\033[m', a.isalnum())
print('\033[36mÉ ASCII?\033[m', a.isascii())
print('\033[35mÉ um digito?\033[m', a.isdigit())
print('\033[31mÉ minusculo?\033[m', a.islower())
print('\033[30mÉ maiusculo?\033[m', a.isupper())
print('\033[4mÉ decimal?\033[m', a.isdecimal())
print('\033[7;36mÉ identificador?\033[m', a.isidentifier())
print('\033[4;35mÉ exibivel?\033[m', a.isprintable())
print('\033[34mTem espaço?\033[m', a.isspace())
print('\033[33mÉ um titulo?\033[m', a.istitle())