por_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
      número = int ( input (' Digite um número entre 0 e 20: '))

      while número < 0 or número > 20:
            número = int ( input (' Tente novamente. Digite um número entre 0 e 20: '))            

      print (' Você digitou o número', por_extenso[número])
      print ()
      
      resp = str ( input (' Quer continuar?[S/N] ')).upper().strip()
      print ()
      
      if resp != 'S' and resp != 'N':
            while True:
                  resp = str ( input (' Não entendi. Responda novamente [S/N]:' )).upper().strip()
                  if resp == 'S' or resp == 'N':
                        break

      if resp == 'N':
            break