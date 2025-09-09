## Detector de palíndromo

'''frase = str ( input (' Digite uma frase ou palavra: ')).strip().upper()
splitado = frase.split()
junto = ''.join (splitado)
inverso = ''
for letra in range (len (junto) -1, -1, -1):
      inverso += junto[letra]

if inverso == junto:
      print (' É um palíndromo')   
else:
      print (' Não é um palíndromo ')
      
print (f' O inverso de {junto} é {inverso}.')'''

frase = str ( input (' Digite uma frase ou palavra: ')).strip().upper()
splitado = frase.split()
junto = ''.join (splitado)
inverso = junto [::-1]

if inverso == junto:
      print (' É um palíndromo')   
else:
      print (' Não é um palíndromo ')

print (f' O inverso de {junto} é {inverso}.')