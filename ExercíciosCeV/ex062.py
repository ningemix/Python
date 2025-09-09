
'''print (' Gerador de PA')
print ('='*50)

t = int ( input (' Primeiro termo: '))
r = int ( input (' Razão: '))
cont = 1
print ()
p = ''
while cont >= 1 and p == '':
      print (f' \033[32m{t} ', end = '')
      print ('>' if cont < 10 else '> Pausa\033[m', end = '')
      cont += 1
      t += r
      if cont > 10:
            p = 1
            cont2 = 0
            while p > 0:
                  print ('\n')
                  print ('='*50)
                  p = int ( input (' \033[mQuantos termos você quer mostrar a mais? '))
                  cont2 += p
                  print ()
                  cont3 = 1
                  while cont3 <= p:  
                        print (f' \033[32m{t} ', end = '')
                        print ('>' if cont3 < p else '> Pausa\033[m', end = '')      
                        cont3 += 1
                        t += r
                     
print (f'\033[33m Progressão finalizada com {cont + cont2 - 1} termos mostrados. \033[m')'''

print (' Gerador de PA')
print ('=' * 50)

primeiro = int ( input (' Primeiro termo: '))
razão = int ( input (' Razão: '))

termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
      total = total + mais
      while cont <= total:
            print (f' {termo} >', end = '')
            termo += razão
            cont += 1
      print (' Pausa')
      mais = int ( input (' Quantos termos você quer mostrar a mais? '))

print (f' Progressão finalizada com {total} termos mostrados.')
            
      