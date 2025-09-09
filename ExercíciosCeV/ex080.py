'''values = []
for v in range (0, 5):
      value = int ( input (' Type a value: '))
      if v == 0 or value > values [-1]:
            values.append (value)
            print (' The value has been added to the end of the list')
      else:
            pos = 0
            while pos < len (values):
                  if value <= values [pos]:
                        values.insert (pos, value)
                        print (f' The value was added in position {pos}')
                        break
                  pos += 1
print (values)'''

import bisect
values = []
for v in range (0, 5):
      value = int ( input (' Type a value: '))
      bisect.insort (values, value)
      print (f' The value was added in position {values.index (value)}')
print (values)