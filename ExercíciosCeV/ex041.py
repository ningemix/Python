##Classificando atletas

pano = int ( input (' Ano de nascimento (ex: 2002): '))
ano_atual = int (input (' Digite o ano atual: '))
idade = ano_atual - ano #A sobra é equivalente a idade da pessoa

print()
if idade <= 9:
      print (f' O atleta tem {idade} anos')
      print (' Categoria mirim ')

elif idade <= 14:
      print (f' O atleta tem {idade} anos')
      print (' Categoria Infantil ')
      
elif idade <= 19:
      print (f' O atleta tem {idade} anos')
      print (' Categoria Junior ')
      
elif idade <= 25:
      print (f' O atleta tem {idade} anos')
      print (' Categoria Sênior ')
      
else:
      print (f' O atleta tem {idade} anos')
      print (' Categoria Master ')
      
      
