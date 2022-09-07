produtos = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00,
            "Transferidor", 4.20,"Compasso", 9.99, "Mochila", 120.32, "Canetas",
            22.30, "Livro", 34.90)
print('-' * 39)
print('{:^38}'.format('lISTAGEM DE PRODUTOS'))
print('-' * 39)
for p in range(0, len(produtos)):
    if p % 2 == 0:
        print('{:.<30}'.format(produtos[p]), end='')
    else:
        print('R$ {:>5.2f}'.format(produtos[p]))
print('-' * 39)