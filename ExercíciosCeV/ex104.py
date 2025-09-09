def leiaint(f):
    while True:
        valor = str(input(f))
        if valor.isnumeric():
            return int (valor)
        else:
            print ('\033[31mError! Type a valid integer.\033[m')


#Main Program
n = leiaint ('Type a number: ')
print (f'You have just typed the number', n)