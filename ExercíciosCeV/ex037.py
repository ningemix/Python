## Conversor de Bases Numéricas

from time import sleep
print (' \033[1;33;44mConvertendo números inteiros\033[m ')
print ('='*40)
n = int (input (' Digite um número: '))
print ()

print (' Agora escolha uma das bases de conversão abaixo:\n \033[1;31m1\033[m para \033[1;32mbinário\033[m\n \033[1;33m2\033[m para \033[1;32moctal\033[m\n \033[1;36m3\033[m para \033[1;32mhexadecimal\033[m')
print ('='*40)
base = int ( input (' Escolha sua base: '))

if base == 1:
      print (' CONVERTENDO PARA BINÁRIO ...')

elif base == 2:
      print (' CONVERTENDO PARA OCTAL ...')

elif base == 3:
      print (' CONVERTENDO PARA HEXADECIMAL ...')

else:
      print()

print ('='*40)
sleep(3)
print()

#Conversão para binário:
if base == 1:
      binário = bin(n)
      print (f' \033[1;32mO {n} em binário fica: {binário [2:]}\033[m')

#Conversão para octal:
elif base == 2:
      oct = oct(n)
      print(f' \033[1;32mO {n} em octal fica: {oct [2:]}\033[m') 

#Conversão para hexadecimal:
elif base == 3:
      hex = hex(n)
      print (f' \033[1;32mO {n} em hexadecimal fica: {hex [2:]}\033[m')
     
else:
      print (' \033[1;31mVocê escolheu uma base inexistente. Tente novamente. \033[m')