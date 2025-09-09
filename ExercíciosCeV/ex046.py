## Contagem regressiva

from time import sleep
from emoji import emojize

r = str ( input (' Digite start: ')).lower()

if r == 'start':
      for c in range (10, -1, -1):
            print ('',c)
            sleep(1)
      print ()
      print (emojize (' FOGOS!! :fireworks:'))
      
else:
      print (' Desculpa, não entendi. Tente novamente.')
