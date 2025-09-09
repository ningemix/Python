from random import randint
from time import sleep
players = {}
print ('Values drawn: ')
for n in range (1, 11):
#sorteando números inteiros e adicionando na variável 'raffle'
    raffle = randint(1, 6)
#adicionando a variável dentro do dicionário 'players'
    players ['player' + str (n)] = raffle
    print (f"The player {n} took", raffle)
    sleep (1)
print ('='*20)
print ('Ranking of players: ')
#organizando os valores de 'players' em ordem decrescente
players = dict (sorted(players.items(), key=lambda item: item[1], reverse=True))
c = 1
for k, v in players.items():
    print(f'{c}º lugar: {k} com {v}.')
    sleep (1)
    c += 1
