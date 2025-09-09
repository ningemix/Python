'''maior = homem = menosde20 =  0
while True:
      print ('='*30)
      print (' CADASTRAR UMA PESSOA')
      print ('='*30)
      
      while True:
            idade = int ( input (' Idade: '))
            if idade > 0:   
                  if idade >= 18:
                        maior += 1      
                  break
      while True:      
            sexo = str ( input (' Sexo [M/F]: ')).upper().strip()
            if sexo == 'M' or sexo == 'F':
                  if sexo == 'M':
                        homem += 1
                  if sexo == 'F' and idade < 20:
                        menosde20 += 1      
                  break                              
      print ('='*30)
      while True:
            resposta = str ( input (' Quer continuar? [S/N]: ')).upper().strip()
            if resposta == 'S' or resposta == 'N':
                  break
                       
      if resposta == 'N':
            break
print ()
print ('========== FIM DO PROGRAMA ==========')'''
#print (f''' Pessoas maiores de 18 anos: {maior}
# Homens cadastrados: {homem}
# Mulheres com menos de 20 anos: {menosde20}''')

tot18 = totH = totM20 = 0
while True:
      idade = int ( input (' Idade: '))
      sexo = ' '
      
      while sexo not in 'MF':
            sexo = str ( input (' Sexo: ')).strip () .upper () [0]
            
      if idade >= 18:
            tot18 += 1
            
      if sexo == 'M':
            totH += 1
            
      if sexo == 'F' and idade < 20:
            totM20 += 1
      resp = ' '
      
      while resp not in 'SN':
            resp = str ( input (' Quer continuar? [S/N]')) .strip() .upper() [0]
      if resp == 'N':
            break
print ()
print (f' Total de pessoas com 18 anos ou mais: {tot18}')
print (f' Homens cadastrados: {totH}')
print (f' Mulheres com menos de 20 anos: {totM20}')
            
            
            
      
      