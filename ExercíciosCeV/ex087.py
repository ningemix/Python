matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sum_even = sum_last = 0
for l in range (0, 3):
    for c in range (0, 3):
        matriz [l][c] = int (input (f'Type a value for [{l}, {c}]: '))
        if matriz [l][c] % 2 == 0:
            sum_even += matriz [l][c]

for l in range (0, 3):
    for c in range (0, 3):
        print (f'[{matriz [l][c]:^5}]', end = '')
    print ()

print ('='*30)
print ('The sum of even values is', sum_even)

# The 1º way:
'''cont = 0
for n in range (0, 3):
    for v in matriz [n]:
        cont += 1
        if cont == 3 or cont == 6 or cont == 9:
            sum_last += v
        if cont == 4:
            high = v
        else:
            if cont == 5 or cont == 6:
                if v > high:
                    high = v
print ('The sum of the values of third column is', sum_last)
print ('The largest value in the second line is', high)'''


# The 2º way:
sum = high = 0
for l in range (0,3):
    sum += matriz [l][2]
print ('The sum of the values of third column is', sum)

for c in range (0, 3):
    if c == 0:
        high = matriz [1][c]
    elif matriz [1][c] > high:
        high = matriz [1][c]
print ('The largest value in the second line is', high)






