c = str(input('Digite o nome da cidade: ')).strip()
print('\033[1;34m', c[:5].lower() == 'santo', '\033[m')