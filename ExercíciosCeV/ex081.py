values = []
while True:
      values.append ( int ( input (' Type a value: ')))
      question = str ( input (' Want to continue?[Y/N] ')).strip ().upper ()
      while question not in 'YN':
            question = str ( input (' Want to continue?[Y/N] ')).strip ().upper ()
      if question == 'N':
            break 

print ('='* 30)
print (f' You type in {len (values)} elements')
values.sort (reverse = True)
print (f' The values in descending order are {values}')
if 5 in values:
      print (' Value 5 is on the list ')
else:
      print (' Value 5 is not on the list')

if 5 in values:
      print (' The value 5 is in position(s):', end = ' ')
      for pos, v in enumerate (values):
            if v == 5:
                  print (pos, end = ' > ')
      print ('End')
            