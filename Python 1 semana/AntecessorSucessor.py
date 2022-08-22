n = int(input('Digite um número: '))
s = n + 1
a = n - 1
print ('O número {}{}{} tem como sucessor {}{}{} e como antecessor {}{}{}' .format('\033[1;33m', n, '\033[m', '\033[0;32m', s,'\033[m','\033[0;36m', a,'\033[m'))