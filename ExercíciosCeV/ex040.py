## Aquele clássico da média

n1 = float ( input (' 1° nota: '))
n2 = float ( input (' 2° nota: '))

m = (n1 + n2) / 2
print (f' Sua média foi de {m}')
print ('='*13)

if m < 5.0:
      print (' \033[31mReprovado :(\033[m ') 

elif m >= 5.0 and m < 7:
      print (' \033[33mRecuperação\033[m')
      
elif m >= 7 and m <= 10:
      print (' \033[32mAprovado :)\033[m ')
      
      