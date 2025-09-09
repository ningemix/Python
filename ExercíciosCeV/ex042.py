###Analisando Triângulo

from time import sleep
cm = float ( input (' 1° reta: '))
cm2 = float ( input (' 2° reta: '))
cm3 = float ( input (' 3° reta: '))

print (' PROCESSANDO...')
sleep(2)
print ('='*40)

#Medidas para formar um triângulo
if cm < cm2 + cm3 and cm2 < cm + cm3 and cm3 < cm + cm2:
      print (' Pode formar um triângulo')
 
##Definindo o tipo de triângulo

#Propriedades do isósceles     
      if cm == cm2 !=cm3 or cm == cm3 != cm2 or cm2 == cm3 != cm:
            print (' É um triângulo isósceles ')
                        
#Propriedades do escaleno           
      elif cm != cm2 != cm3 != cm:
            print (' É um triângulo escaleno')
             
#Propriedades do equilátero
      elif cm == cm2 == cm3:
            print (' É um triângulo equilátero')
            
      else:
            print (' Não pode formar um triângulo.')

     