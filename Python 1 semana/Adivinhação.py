from random import choice
print('Dificuldades: (Facil (1-3), Normal (1-5), Dificil (1-10).')
d = str(input('Digite a dificuldade desejada: ')).strip().lower()
n = int(input('Tente adivinhar o número: '))
if d == 'facil':
    o = (1, 2, 3)
    e = choice(o)
    if n == e:
        print('\033[1;32mParabéns, você ganhou!\033[m')
    else:
        print(f'\033[1;31mNão foi dessa vez, o número escolhido foi {e}!\033[mfa')
else:
    if d == 'normal':
        o = (1, 2, 3, 4, 5)
        e = choice(o)
        if n == e:
            print('\033[1;32mParabéns, você ganhou!\033[m')
        else:
            print(f'\033[1;31mNão foi dessa vez, o número escolhido foi {e}!\033[m')
    else:
        if d == 'dificil':
            o = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
            e = choice(o)
            if n == e:
                print('\033[0;32mParabéns, você ganhou!\033[m')
            else:
                print(f'\033[0;31mNão foi dessa vez, o número escolhido foi {e}!\033[m')
