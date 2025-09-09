# Separando dígitos de um número

##Só funciona com 4 dígitos
'''número = int (input(' Digite um número de 1000 até 9999: '))
n = str (número)
n1 = (n[:5])
print (f' Unidade: {n1[3:4]}\n Dezena: {n1[2:3]}\n Centena: {n1[1:2]}\n Milhar: {n1[:1]}')'''

##De 0 a 9999
'''num = int (input (' Digite um número '))
u = num // 1 % 10
d = num // 10 %10
c = num // 100 % 10
m = num // 1000 % 10
print (f' Unidade: {u}\n Dezena: {d}\n Centena: {c}\n Milhar: {m}')'''

