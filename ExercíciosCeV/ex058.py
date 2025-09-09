'''from random import randint
sorteio = randint (0, 10)

resposta = 11
cont = 0

print (' Estou pensando em um número entre 0 e 10. Dúvido   você Advinhar qual é...')
print ()

while resposta != sorteio:
      resposta = int ( input (' Dê seu palpite: '))
      print ()
      cont += 1
      
      if resposta < sorteio:
            print (f' Mais... Tente novamente.')       
            print ()
      if resposta > sorteio:
            print (' Menos... Tente novamente.')
            print ()

print (f' Parabéns!! Eu pensei no {sorteio}')
print (f' Você acertou depois de {cont} tentativa(s)')'''

from random import randint

sorteio = randint (0, 10)
print (' Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print (' Será que você consegue adivinhar qual foi?')
acertou = False
cont = 0
while not acertou:
      resposta = int ( input (' Qual é seu palpite? '))
      cont += 1
      if resposta == sorteio:
            acertou = True
      else:
            if resposta < sorteio:
                  print (' Mais... Tente novamente.')
            else:
                  print (' Menos... Tente novamente.')
            
print (f' Acertou com {cont} tentativas. Parabéns!')
