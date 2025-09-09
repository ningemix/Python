
'''i = ''
while i != 'F' and i != 'M':
      i = str ( input (' Digite seu sexo [M/F]: ')).upper()
      if i != 'F' and i != 'M':
            while not i == 'F' and not i == 'M':
                  i = str ( input (' Dados inválidos. Por favor, informe seu sexo: ')).upper()

print ()
print (f' Sexo {i} registrado com sucesso ')'''
            
sexo = str ( input (' Digite seu sexo [F/M]: ')).strip() .upper() [0]

while sexo not in 'MF':
      sexo = str ( input (' Dados inválidos. Tente novamente: ')).strip() .upper() [0]

print (f' Sexo {sexo} registrado com sucesso. ')