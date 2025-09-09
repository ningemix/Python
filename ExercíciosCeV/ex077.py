palavras = ('Planta', 'Ventilador', 'Cadeira', 'Geladeira', 'Paralelepipedo', 'Altura')

'''vogais = ('a', 'e', 'i', 'o', 'u')

for cont in palavras:
      print (f' Na palavra {cont.lower()} temos', end = ' ')   
     
      if 'a' in cont:                                                 print (vogais[0], end = ' ')
                  
      if 'e' in cont:
            print (vogais[1], end = ' ')
          
      if 'i' in cont:
            print (vogais[2], end = ' ')
                 
      if 'o' in cont:
            print (vogais[3], end = ' ')
            
      if 'u' in cont:
            print (vogais[4], end = ' ')
      print ('\n')'''

for p in palavras:
      print (f' Na palavra {p} temos', end = ' ')
      for letra in p:
            if letra.lower() in 'aeiou':
                  print (letra, end = ' ')
      
      print ('\n')
      
            
      
            
            