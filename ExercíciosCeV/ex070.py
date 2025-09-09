print ('========== LOJA DO JOÃO ==========')
print ()
total = maisdemil = cont = menor = 0
nome = ''

while True:
      produto = str ( input (' Nome do produto: '))
      preço = float ( input (' Preço: R$'))
      cont += 1
      total += preço
      
      if cont == 1 or preço < menor:
            menor = preço
            nome = produto
     
      if preço > 1000:
            maisdemil += 1
            
      while True:
            resposta = str ( input (' Quer continuar? [S/N] ')) .upper () .strip ()
            if resposta == 'S' or resposta == 'N':
                  break
      print ('='*40)
      print ()
      
      if resposta == 'N':
            break

print ('========== FIM DO PROGRAMA ==========')
print (f''' O total da compra foi R${total:.2f}
 Temos {maisdemil} produto(s) custando mais de R$1000.00
 O produto mais barato foi {nome} que custa R${menor:.2f}''')
          