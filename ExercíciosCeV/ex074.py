print (' Os valores sorteados foram: ', end = '')
from random import randint
for cont in range (0, 5):
      valores = (randint(0, 10))
      print (valores, end = ' ')
      if cont == 0:
            menor = valores
            maior = valores
      else:
            if valores < menor:
                  menor = valores
            if valores > maior:
                  maior = valores

print ('\n')                  
print (' O maior valor sorteado foi', maior)
print (' O menor valor sorteado foi', menor)
      
