from datetime import date
ano_atual = date.today().year
cont = 0
cont2 = 0
for c in range (1, 8):
      nasc = int ( input (f' Digite o ano de nascimento da {c}° pessoa: '))
      idade = ano_atual - nasc      
      if idade >= 18: 
            cont += 1
      else:
            cont2 += 1
            
print (f' Ao todo tivemos {cont} pessoas maiores de idade.')
            
print (f' E também tivemos {cont2} pessoas menores de idade')
            
            
      