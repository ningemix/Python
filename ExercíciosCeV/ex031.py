#Custo da viagem

from time import sleep
distância = float ( input (' Distância da sua viagem em Km: '))
passagem1 = distância * 0.50 
passagem2 = distância * 0.45
print (' PROCESSANDO...')
sleep(2)
print('='*40)
if distância <= 200:
      print (f' Sua passagem custará R${passagem1:.2f}')
else:
      print (f' Sua passagem custará R${passagem2:.2f}')

      


      