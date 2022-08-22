n = str(input('Digite o seu nome: ')).strip()
l = n.lower()
print(n[:l.find(' ')])
print(n[l.rfind(' ') + 1:])