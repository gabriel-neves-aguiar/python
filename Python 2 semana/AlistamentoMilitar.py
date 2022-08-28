from datetime import date
atual = date.today().year
nascimento = int(input('Digite o ano do nascimento: '))
idade = atual - nascimento
sexo = str(input('Digite o seu sexo: ')).lower().strip()
if sexo == 'masculino':
    if idade < 18:
        print('\033[36mAinda não está na hora de se alistar.\033[m')
        print('Seu alistamento será em {} anos'.format(18 - idade))
    elif idade == 18:
        print('\033[33mChegou a hora de se alistar!\033[m')
    elif idade > 18:
        alistamento = int(input('[1]\033[34mSim\n\033[m[2]\033[34mNão\033[m\nVocê já realizou o alistamento? ' ))
        if alistamento == 1:
            print('Você já se alistou!')
        elif alistamento == 2:
            print('\033[31mAtenção! Você deveria ter se alistado há {} anos!\033[m'.format(idade - 18))
else:
    print('Você não precisa se alistar!')