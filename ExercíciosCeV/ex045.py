## GAME: Pedra, Papel e Tesoura

from random import choice
from time import sleep

while True:
      print ('\033[1;32;44m                 J O K E N P Ô ! !                 \033[m')
      
      print ('='*51)
      r = str ( input (' Vamos jogar Jokenpô? (\033[32mSim\033[m ou \033[31mNão\033[m):')).upper()
      print ()
      
      if r == 'SIM':
            print (' Ótimo! Vou passar as regras a seguir...')
            sleep(1)
      
      elif r == 'NÃO' or r == 'NAO':
            print (' Que pena :(')
            
      else:
            print (' Desculpa, não entendi...')
      print ()
      
      if r == 'SIM':
            print ('\033[33m='*39)
            print ('\033[33;41m Regras do Jokenpô:                    \033[m\033[33m|\n\033[33;41m Escolha entre: Pedra, Papel e Tesoura \033[m\033[33m|\033[m')
            print ('\033[33m=\033[m'*39)
            sleep(1)
      
      else:
            ()
            
      print ()
      
      ppt = ('pedra', 'papel', 'tesoura')
      sorteio = choice(ppt)
      
      if r == 'SIM':
            resp = str ( input (' Digite sua jogada: ')).lower()
            
            print()
            print (' PREPARAR...')
            sleep(2)
            print (' JÁÁÁ!!! ')
            print ()
            sleep(1)
                  
            if resp == 'pedra' or resp == 'papel' or resp == 'tesoura':
                  print (f' Você jogou {resp} e eu joguei {sorteio}.')
                  
                  if resp == sorteio:
                        sleep(2)
                        print()
                        print (' \033[33mEmpatamos :)\033[m')
                  
                  elif resp == 'pedra' and sorteio == 'tesoura' or resp == 'papel' and sorteio == 'pedra' or resp == 'tesoura' and sorteio == 'papel':
                        sleep (1)
                        print()
                        print (' \033[32mVocê me venceu. Parabéns!!\033[m')
                  
                  else:
                        sleep (1)
                        print()
                        print (' \033[31mEu venci você!! HAHAHAHA!!\033[m')
            
            else:
                   print (' Desculpa, não entendi...')
      print ()                  
      respostaa = str (input (' Quer continuar? '))
      print ()
      if respostaa == 'NAO':
            break

       