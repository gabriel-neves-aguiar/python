classificacao = ('Palmeiras', 'Flamengo', 'Fluminense', 'Corinthians','Athletico-PR',
                 'Internacional', 'Atlético-MG', 'Santos', 'América-MG', 'Goiás',
                 'Bragantino', 'Fortaleza', 'São Paulo', 'Botafogo', 'Ceará SC',
                 'Coritiba', 'Cuiabá', 'Avaí', 'Atlético-GO', 'Juventude')
print('Os 5 primeiros colocados são:')
print(classificacao[0:5])
print('-=' * 35)
print('Os 4 últimos colocados são:')
print(classificacao[-4:])
print('-=' * 35)
print('{}'.format(sorted(classificacao)))
print('-=' *129)
print('O santos está na {}ª colocação!'.format(classificacao.index('Santos') + 1))