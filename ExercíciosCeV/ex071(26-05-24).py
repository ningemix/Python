'''print ('========== BANCO JP ==========')
print ()

valor = int ( input (' Qual valor você quer sacar? R$'))
total = valor
cont = 1

while True:      
      if cont == 1:      
            total = total // 50
            cédula = total
            if cédula > 0:
                  print (f' Total de {cédula} cédula(s) de R$50')
      cont += 1

      if cont == 2:      
            total = cédula * 50
            total = valor - total
            cédula = total // 20
            if cédula > 0:
                  print (f' Total de {cédula} cédula(s) de R$20')

      if cont == 3:
            total = total - (cédula * 20)
            cédula = total // 10
            if cédula > 0:
                  print (f' Total de {cédula} cédula(s) de R$10')

      if cont == 4:
            total = total - (cédula * 10)
            cédula = total // 1
            if cédula > 0:
                  print (f' Total de {cédula} cédula(s) de R$1')
            break
print ()
print ('='*30)
print (' Volte sempre ao BANCO JP! Tenha um bom dia!')'''

print ('========== BANCO CEV ==========')
valor = int ( input (' Qual valor você quer sacar? R$'))
total = valor
céd = 50
totcéd = 0

while True:
      if total >= céd:
            total -= céd
            totcéd += 1
      
      else:
            if totcéd > 0:
                  print (f' Total de {totcéd} cédula(s) de R${céd}')
                  
            if céd == 50:
                  céd = 20
                  
            elif céd == 20:
                  céd = 10
             
            elif céd == 10:
                  céd = 1
            totcéd = 0
             
            if total == 0:
                  break

print ('='*30)
print (' Volte sempre ao BANCO CEV! Tenha um bom dia!')


   