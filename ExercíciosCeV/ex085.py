numbers = [[], []]
cont = 0
while True:
      cont += 1
      num = int ( input (f' Type a {cont}° number: '))
      if num % 2 == 0:
            numbers[0].append (num)
      else:
            numbers[1].append (num)
      while True:
            question = str ( input (' Want to continue? ')).strip ().lower ()
            if question == 'y' or question == 'n':
                  break
      if question == 'n':
            break
print ('='*30)
print (' The even values entered were', numbers [0])
print (' The odd values entered were', numbers [1])


      
      