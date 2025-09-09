numbers = []
while True:
      numbers.append ( int (input (' Type a number: ')))
      question = str ( input (' Want to continue?[Y/N] ')).strip ().upper ()
      while question not in 'YN':
            question = str ( input (' Want to continue?[Y/N] ')).strip ().upper ()
      if question == 'N':
            break
pos = 0
pairs = []
odd = []
for n in range (0, len (numbers)):
      num = numbers [pos] % 2       
      if num == 0:
            pairs.append (numbers [pos])    
      else:
            odd.append (numbers [pos])            
      pos += 1          

print ('='*30)
print (f' The complete list is {numbers}')     
print (f' The list of pairs is {pairs}')   
print (f' The list of odd numbers is {odd}')    

