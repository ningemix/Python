'''n = int ( input (' Digite um número: '))
print (f' {n}! = ', end = '')
multi = 1
for c in range (n, 0, -1):
      print (f' {c} x', end = '')
      multi *= c
print (f' = {multi}')'''


'''n = int ( input (' Digite um número: '))
print ()
print (f' {n}! =', end = '')
multi = 1
cont = 1

if n <= 1:
     print (f' 1')
      
while n >= 2:
      print (f' {n} x', end = '')
      multi *= n
      n -= cont
      
print (f' 1 = {multi}', end = '')
print ()'''

'''from math import factorial
n = int ( input (' Digite um número e veja o seu fatorial: '))
f = factorial (n)
print ()
print (f' {n}! = {f}')'''
           
n = int ( input (' Digite um número: '))
c = n
f = 1

print (f' {n}! =', end = '')
while c > 0:
      print (f' {c}', end = '')
      print (' x' if c > 1 else ' =', end = '')
      f *= c
      c -= 1
     
print (f' {f}')





      