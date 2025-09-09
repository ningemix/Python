'''cont = 1
n = int ( input (' Quer ver a tabuada de qual valor? '))
print ('='*50)

while True:
      if n >= 0:
            if cont > 10:
                  break
            print (f' {n} × {cont} = {n*cont}')
            cont += 1
                        
            if cont > 10:
                  print ('='*50)
                  n = int ( input (' Quer ver a tabuada de qual valor? '))
                  print ('='*50)
                  cont = 1
      else:
            break
print (' Programa tabuada encerrado. Volte sempre!')'''

while True:
      n = int ( input (' Quer ver a tabuada de qual valor? '))
      print ('='*50)
      
      if n < 0:
            break
      
      for c in range (1, 11):
            print (f' {n} x {c} = {n*c}')
      print ('='*50)      

print (' Programa tabuada encerrado. Volte sempre! ')
      
      