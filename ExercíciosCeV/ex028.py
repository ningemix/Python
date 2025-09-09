#Jogo da Adivinhação

from random import randint
from time import sleep
print (' Estou pensando em um número entre 0 e 10. Advinhe   qual é...')
número = randint(0, 10) #Faz o computador sortear um número inteiro de 0 a 10
resposta = int (input(' Resposta: ')) #Jogador tenta adivinhar
print (' PROCESSANDO...')
print ('='*40)
sleep(2) #Faz o computador esperar 2 segundos
if número == resposta:
      print(' PARABÉNS!! Você acertou!')
else:
      print(' Você errou, tente novamente :(')
print()
print (f' Eu pensei no {número}')# O computador mostra a resposta correta