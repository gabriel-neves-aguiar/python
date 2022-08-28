print('[M] \033[34mMasculino\033[m\n[F] \033[35mFeminino\033[m')
sexo = str(input('Digite o sexo da pessoa: ')).strip().upper()[0]
while sexo != 'M' and sexo != 'F':
    sexo = str(input('O sexo foi digitado incorretamente, por favor digite novamente: ')).strip().upper()[0]
if sexo == 'M':
    print('\033[34mSexo masculino cadastrado com sucesso\033[m')
elif sexo == 'F':
    print('\033[35mSexo feminino cadastrado com sucesso\033[m')