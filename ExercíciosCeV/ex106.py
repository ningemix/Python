from time import sleep


def line(msg):
    print (f'=' * len(msg))
    print (msg)
    print('=' * len(msg))
    print('\033[m')


def quest():
    while True:
        print ('\033[1;97;42m', end = '')
        line('  PyHELP HELP SYSTEM  ')
        p = input ('Function ou library > ')
        if p == 'end':
            print('\033[1;97;41m', end='')
            line('ATÉ LOGO!')
            break
        print ('\033[1;97;46m', end = '')
        line (f"  Accessing the '{p}' command manual  ")
        sleep(1)
        print ('\033[1;30;107m')
        help(p)
        print ('\033[m')


quest()