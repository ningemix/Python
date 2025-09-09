números = (int ( input (' Digite um número: ')), int ( input (' Digite outro número: ')), int ( input (' Digite mais número: ')), int ( input (' Digite o último número: ')))
print ()

print (' Você digitou os valores', números)
print (f' O valor 9 apareceu {números.count(9)} vezes')
if 3 in números:
      print (f' O valor 3 apareceu na posição {números.index(3)+1}')
else:
      print (' O valor 3 não foi digitado')

print (' Os valores pares são: ', end = '')
for cont in números:
      if cont % 2 == 0:
            print (cont, end = ' ')



