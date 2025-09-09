from random import randint
numbers = []


def raffle (*raf):
    print ('='*30)
    print ('Analyzing past values...')
    cont = high = 0
    for d in raf:
        print (d, end =' ')
        if cont == 0:
            high = d
        else:
            if d > high:
                high = d
        cont += 1
    print (f'({len(raf)} Values have been entered for all)')
    print(f'The highest value reported was {high}')


for c in range (0, 6):
    numbers.append(randint (0, 9))
raffle (*numbers)
numbers.clear()
for c in range (0, 3):
    numbers.append(randint (0, 9))
raffle (*numbers)
numbers.clear()
for c in range (0, 2):
    numbers.append(randint (0, 9))
raffle (*numbers)
numbers.clear()
for c in range (0, 1):
    numbers.append(randint (0, 9))
raffle (*numbers)
numbers.clear()
raffle ()
