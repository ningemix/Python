from random import randint
from time import sleep
games = []
full = []
print ('='*40)
print ('PLAY MEGA SENA'.center(37))
print ('='*40)
quest = int (input ('How many games do you want me to draw? '))
cont = n = 0
print ('='*10, f'Drawing {quest} games', '='*10)

while True:
    sleep (1)
    for n in range (0, 6):
        num = (randint(1, 60))
        while True:
            if num not in games:
                games.append (num)
                full.append (games)
                break
            else:
                num = (randint(1, 60))
    cont += 1
    print (f'\033[36mGame {cont}:\033[m {full [n]}')
    n += 11
    games.clear ()
    if cont == quest:
        break
print ('='*10, 'Good Luck!', '='*10)
