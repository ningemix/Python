'''from random import randint

print ('='*15)
print (' PAR OU ÍMPAR')
print ('='*15)
print ()
cont = 0

while True:
      n = int ( input (' Diga um valor: '))
      while True:            
            r = str ( input (' Par ou Ímpar? [P/I]: ')).upper().strip()[0]
            if r == 'P' or r == 'I':
                  break
      print ('='*51)
      sorteio = randint (0, 10)
      total = (n + sorteio) % 2
            
      if total == 0 and r == 'P' or total == 1 and r == 'I':
            if total == 0:
                  print (f' Você jogou {n} e o computador {sorteio}. Total de {n+sorteio} Deu PAR.')
            else:
                  print (f' Você jogou {n} e o computador {sorteio}. Total de {n+sorteio} Deu ÍMPAR.')
            print (' Você venceu!')
            print (' Vamos jogar novamente...')
            print ('='*51)
            cont += 1
            print ()

      elif total == 0 and r == 'I' or total == 1 and r == 'P':
            if total == 0:
                  print (f' Você jogou {n} e o computador {sorteio}. Total de {n+sorteio} Deu PAR.')
            else:
                  print (f' Você jogou {n} e o computador {sorteio}. Total de {n+sorteio} Deu ÍMPAR.')
            print (' Você perdeu :(')
            print ('='*51
            print ()
            print (f' Game over! Você venceu {cont} vezes.')
            break'''
            
from random import randint
v = 0
while True:
      jogador = int ( input (' Diga um valor: '))
      computador = randint (0, 10)
      total = jogador + computador
      tipo = ' '
      
      while tipo not in 'PI':
            tipo = str ( input (' Par ou Ímpar? [P/I] ')).upper () .strip () [0]
      print (f' Você jogou {jogador} e o computador {computador}. Total de {total}', end = '')
      print (' DEU PAR ' if total % 2 == 0 else ' DEU ÍMPAR ')
      if tipo == 'P':
            if total % 2 == 0:
                  print (' Você venceu! ')
                  v += 1
            else:
                  print (' Você perdeu :( ')
      elif tipo == 'I':
            if total % 2 == 1:
                  print (' Você venceu! ')
                  v += 1
            else:
                  print (' Você perdeu :( ')
                  break
          
      print (' Vamos jogar novamente...')

print (f' Game Over! Você venceu {v} vezes. ')
         
      
            