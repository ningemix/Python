## Alistamento Militar

from time import sleep

sexo = str ( input (' Você é homem ou mulher?: ')).upper()

if sexo == 'MULHER':
      print()
      print (' OBS: O alistamento não é obrigatório para você.')
      print()

else:
      print()

ano = int ( input (' Digite seu ano de nascimento (\033[37mEx: 2002\033[m): '))
atual = int ( input (' Digite o ano atual: '))

alistamento = ano + 18
idade = atual - ano

print (' PROCESSANDO...')
sleep(2)
print('='*40)

if atual < alistamento:
      a = alistamento - atual
      print (f''' Quem nasceu em {ano} tem {idade} ano(s) em {atual}.
 Falta(m) {a} ano(s) para você se alistar.
 Seu alistamento será em {alistamento}.''')
      
elif atual == alistamento:
      print (f''' Quem nasceu em {ano} tem 18 anos em {atual}.
 Está na hora de se alistar! ''')
  
elif atual > alistamento:
      a = atual - alistamento
      print (f''' Quem nasceu em {ano} tem {idade} anos em {atual}.
 Você já deveria ter se alistado há {a} anos.
 Seu alistamento foi em {alistamento}.''')
 
else:
       print (' Algo de errado não está certo. Tente novamente :) ')

      
      
