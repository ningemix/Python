## Números primos'
      
n = int (input (' Digite um número: '))

cont = 0
for c in range (1, n + 1): # +1 para pq o programa sempre mostra o anterior
   
      if n % c == 0: #Mostrar os números que são divisíveis por 'n'
      
            print ('\033[33m', end=' ')
            cont += 1 #contagem dos números divisíveis
            
      else: #Os que não são divisíveis
            print ('\033[31m', end= ' ')
      
      print (c, end= ' ') # Sequência de números até o 'n'

print (f' \n \033[mO número {n} foi divisível {cont} vezes.')

if cont == 2: #Se for divisível por apenas dois números é primo
      print (' É um número primo')
      
else:
      print (' Não é um número primo')




      
            