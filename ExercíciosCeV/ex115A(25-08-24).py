from time import sleep
from module.m115A.lib.archiver import *

arc = 'Outubro'
if not arcexist (arc):
    createfile(arc)

while True:
    resp = menu (['See registered Peaple.', 'Register a new person.', 'Log out.'])
    if resp == 1:
        readfile (arc)
    elif resp == 2:
        writefile (arc)
    elif resp == 3:
        header(f'{colors(2)}Out of the system... see your later!{colors()}')
        break
    else:
        print (f'{colors(3)}Enter a valid option.{colors()}')
    sleep(1)
