numero = int(input('Digite o número que quer converter: '))
print('[1] \033[34mBinário \033[m\n[2] \033[33mOctal \033[m\n[3] \033[35mHexadecimal \033[m')
converter = int(input('Digite uma das opções acima: '))
if converter == 1:
    print('\033[34mO número {} em binário é: {}\033[m'.format(numero, bin(numero)[2:]))
elif converter == 2:
    print('\033[33mO número {} em octal é: {}\033[m'.format(numero, oct(numero)[2:]))
elif converter == 3:
    print('\033[35mO número {} em hexadecimal é: {}\033[m'.format(numero, hex(numero)[2:]))
else:
    print('\033[31mOpção inválida\033[m')