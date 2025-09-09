def factorial(n, show=False):
    """
    -> Calculate the factorial of a number
    :param n: Number to be calculated
    :param show: Show the process or not
    :return: The value of the factorial of a number
    """
    f = 1
    for c in range (n, 0, -1):
        if show:
            print (c, end = ' ')
            if c > 1:
                print ('x', end = ' ')
            else:
                print ('= ', end = '')
        f *= c
    return f


n = int (input('Number factorial: '))
quest = str (input('Show calculation process? '))
if quest == 'yes':
    print (factorial(n, show=True))
else:
    print(factorial(n))
quest2 = str (input ('Show help? '))
if quest2 == 'yes':
    help(factorial)
