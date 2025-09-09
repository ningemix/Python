data = []
data_full = []
while True:
      print ('='*30)
      question = ' '
      data.append ( str ( input ('Type a name: ')))
      data.append ( float ( input ('Type a weight: ')))
      if len (data_full) == 0:
            high = small = data [1]
      else:
            if data [1] > high:
                  high = data [1]
            if data [1] < small:
                  small = data [1]
      data_full.append (data [:])
      data.clear ()
      while question != 'yes' and question != 'no':
            question = str ( input ('Want to continue? ')).lower ().strip ()
      if question == 'no':
            break

print ('='*20)
print (f'In all, you have registered {len (data_full)} person(s)')
print (f'The highest weight was {high}kg. Weight of ', end = '')
for p in data_full:
      if p [1] == high:
            print (f'[{p [0]}]', end = ' ')
print (f'\nThe lowest weight was {small}kg. Weight of ', end = '')
for p in data_full:
      if p [1] == small:
            print (f'[{p [0]}]',end = ' ')


