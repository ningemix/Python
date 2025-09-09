km = float (input (' Quantos Km foi percorrido: '))
dias  = int (input (' Quantidade de dias que foi alugado: '))
preço = (dias * 60) + (km * 0.15)
print (f' O total a pagar é de R${preço:.2f}')