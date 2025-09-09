from time import sleep
valor1 = int ( input (' 1° valor: '))
valor2 = int ( input (' 2° valor: '))
print ()
resposta = 0
while resposta != 5:
      print (''' [1] somar
 [2] multiplicar
 [3] maior
 [4] novos números
 [5] sair do programa''')
      print ()
                  
      resposta = int ( input (' Escolha uma das opções acima: '))
      print ()
                            
      if resposta == 1:
             soma = valor1 + valor2
             print (f' {valor1} + {valor2} = {soma}')
                              
      elif resposta == 2:
             multiplicação = valor1 * valor2
             print (f' {valor1} × {valor2} = {multiplicação}')
                                    
      elif resposta == 3:
             if valor1 == valor2:
                   print (f' {valor1} = {valor2}')
             else:
                   maior = max (valor1, valor2)
                   menor = min (valor1, valor2)
                   print (f' {maior} > {menor}')
      
      elif resposta == 4:
            valor1 = int ( input (' 1° valor: '))
            valor2 = int ( input (' 2° valor: '))                   
                     
      elif resposta == 5:
                  print (' FIM')
       
      else:
            print (' Opção inválida. Tente novamente.')
            
      print ()      
      sleep (1)            
     
      