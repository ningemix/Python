## Progressão Aritmética

t = int ( input (' Primeiro termo: '))
r = int (input (' Razão: '))
total = t + (r * 10)
for c in range (t, total, r):
      print (c, end= ' ')