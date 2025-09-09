print ('='*40)
print (f' {"LISTAGEM DE PREÇOS":^36}')
print ('='*40)

'''lista = (' Lápis', '.'*25, 'R$   1.75', '\n Borracha', '.'*22, 'R$   2.00', '\n Caderno', '.'*23, 'R$  15.00', '\n Estojo', '.'*24, 'R$  25.00', '\n Transferidor', '.'*18, 'R$   4.20', '\n Compasso', '.'*22, 'R$   9.99', '\n Mochila', '.'*23, 'R$ 120.32', '\n Canetas', '.'*23, 'R$  22.30', '\n Livros','.'*24, 'R$  34.90')

for cont in lista:
      print (cont, end = '')'''

lista = (' Lápis', 1.75, ' Borracha', 2, ' Caderno', 15.90, ' Estojo', 25, ' Transferidor', 4.20, ' Compasso', 9.99, ' Mochila', 120.32, ' Canetas', 22.30, ' Livro', 34.90)

for pos in range (0, len(lista)):
      if pos % 2 == 0:
            print (f'{lista [pos]:.<30}', end = '')
      else:
            print (f' R$ {lista [pos]:>6.2f}')
                     
print ('='*40)