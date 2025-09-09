t = int ( input (' Primeiro termo: '))
r = int ( input (' Razão: '))
n = int (input (' Qntd. de termos: '))
print ()

cont = 1
while cont <= n:
      print (f' {t} >', end = '')
      t += r
      cont += 1
print (' Fim')
      