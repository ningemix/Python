from random import randint


def ruffle(num):
    print('Drawing 5 values from the list: ', end='')
    for a in range(0, 5):
        n = randint(0, 9)
        num.append(n)
        print(n, end=' ')
    print('READY!')


def total():
    sum = 0
    for c in values:
        if c % 2 == 0:
            sum += c
    print('Adding the even values of', values, end='')
    print(', we have', sum)


values = []
ruffle(values)
total()
