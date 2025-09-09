n = soma = cont = maior = menor = 0
p = 'S'
while n >= 0 and p == 'S':
      n = int ( input (' Digite um número: '))
      soma += n
      cont += 1
      p = str ( input (' Quer continuar? [S/N] ')).upper() .strip () [0]
      
      if cont == 1:
            menor = n
            maior = n
      else:
            if n < menor:
                  menor = n
            if n > maior:
                  maior = n
     
      if p != 'S' and p != 'N':      
            while p != 'S' and p != 'N':
             print (' Resposta inválida. Tente novamente')
             p = str ( input (' Quer continuar? [S/N] ')).upper() .strip () [0]
             
      if p == 'N':
            média = soma / cont
            print ()
            print (f' Você digitou {cont} número(s) e a média foi {média:.2f}')
            print (f' O maior valor foi {maior} e o menor foi {menor}')    
            