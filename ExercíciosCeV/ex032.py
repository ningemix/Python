#Ano Bissexto
from datetime import date
print (' Digite um Ano qualquer e mostrarei se ele é bissexto ou não. Digite 0 e direi se o ano atual é bissexto')
ano = float ( input (' Digite o ano: '))
if ano == 0:
      ano = date.today().year #Para mostrar o ano atual quando digitar 0
if ano % 4 ==0 and ano % 100 !=0 or ano % 400==0:
      print(f' O ano de {ano:.0f} é bissexto')
else:
      print (f' O ano de {ano:.0f} não é bissexto')

      
