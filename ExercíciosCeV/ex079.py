valores = list ()
while True:      
      valor = int (input (' Digite um valor: '))
      if valor not in valores:
            valores.append (valor)
            print (' Valor adicionado com sucesso...')
      else:
            print (' Valor duplicado! Não vou adicionar...')
      while True:
            resposta = str ( input (' Quer continuar? [S/N] ')).upper ().strip ()   
            if resposta in 'SN':                  
                  break
                  
      if resposta == 'N':
            break 
valores.sort ()            
print ('='*40)            
print (' Você digitou os valores', valores)