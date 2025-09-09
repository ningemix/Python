#Aumentos múltiplos

from time import sleep
salário = float ( input (' Digite seu salário: '))
print (' PROCESSANDO...')
sleep(2)
print ('='*40)
#Salário com aumento de 10%
aumento10 = salário + (10/100 * salário)
#Salário com aumento de 15% quando é menor que R$1250.00
aumento15 = salário + (15/100 * salário)
if salário > 1250.00:
      print (f' O salário aumenta para o valor de R${aumento10:.2f}')
else:
      print (f' O salário aumenta para o valor de R${aumento15:.2f}')