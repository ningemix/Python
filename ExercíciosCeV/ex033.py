#Maior e menor valor

'''n1 = float ( input (' Primeiro número: '))
n2 = float ( input (' Segundo número: '))
n3 = float ( input (' Terceiro número: '))
print('='*40)
if n1 > n2 > n3:
      print (f' Maior número: {n1}\n Menor número: {n3}')
if n1 > n3 > n2:
      print (f' Maior número: {n1}\n Menor número: {n2}')
if n2 > n1 > n3:
      print (f' Maior número: {n2}\n Menor número: {n3}')
if n2 > n3 > n1:
      print (f' Maior número: {n2}\n Menor número: {n1}')
if n3 > n2 > n1:
      print (f' Maior número: {n3}\n Menor número: {n1}')
if n3 > n1 > n2:
      print (f' Maior número: {n3}\n Menor número: {n2}')
if n1 == n2 == n3:
      print (f' Os números são iguais.')'''

n1 = int ( input (' 1° número: '))
n2 = int ( input (' 2° número: '))
n3 = int ( input (' 3° número: '))
#Verificando o maior
maior = n1
if n2 > n1 and n2 > n3:
      maior = n2
if n3 > n1 and n3 > n2:
      maior = n3
#Verificando o menor
menor = n1
if n2 < n1 and n2 < n3:
      menor = 2
if n3 < n1 and n3 < n2:
      menor = 3
print ('='*40)
print (f' Maior número: {maior}\n Menor número: {menor}')
      

