from time import sleep


def counting (i, f, p):
    print ('='*30)
    if p < 0:
        p = abs(p)
    print(f'Counting from {i} to {f} from {p} in {p}')
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print (cont, end = ' ')
            cont += p
        print ('End!')
    else:
        cont = i
        while cont >= f:
            print (cont, end = ' ')
            cont -= p
        print ('End!')


counting (1, 10, 1)
counting (10, 0, 2)
i = int (input ('Start: '))
f = int (input ('End: '))
p = int (input ('Step: '))
counting (i, f, p)