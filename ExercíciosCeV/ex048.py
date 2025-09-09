## Soma ímpares múltiplos de três

'''soma = 0
for c in range (3, 501, 6):
      soma = soma + c
      
total = int (c / 6) + 1
print (f' O resultado da soma dos {total} valores é de {soma}')'''

soma = 0
cont = 0
for c in range (1, 501, 2):
      if c % 3 == 0:
            soma += c
            cont += 1

print (f' A soma de todos os {cont} valores solicitados é {soma}')


      
      
      