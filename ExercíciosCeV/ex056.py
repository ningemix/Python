soma = 0
cont = 0
maior = 0
for c in range (1, 5):   
      print (f' === {c}° Pessoa ===')
      n = str ( input (' Nome: '))
      i = int ( input (' Idade: '))
      s = str ( input (' Sexo [M/F]: ')).upper()
      soma += i
      if s == 'F':
            if i < 20:
                  cont += 1
                  
      if s == 'M':
            if c == 1:
                  maior = i      
                  nome = n
            else:
                  if i > maior:
                        maior = i
                        nome = n    
          
média = soma / 4
print (f' A média de idade do grupo é de {média} anos.')
print (f' O homem mais velho tem {maior} anos e se chama {nome}.')
print (f' Ao todo são {cont} mulheres com menos de 20 anos.')

 
      
