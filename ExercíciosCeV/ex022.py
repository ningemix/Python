#Analizador de Textos

'''nome = str (input (' Nome completo: '))
print ('='*40)
maiusculo = nome.upper()
minúsculo = nome.lower()
junção2 = nome.split()
junção3 = ''.join(junção2)
junção4 = len(junção3)
letras = (nome.split()[0])
letras = len(letras)
print (f' Maiusculo: {maiusculo} \n Minúsculo: {minúsculo}\n Todas as letras: {junção4}\n Letras no primeiro nome: {letras}')
print ('='*40)'''

nome = str (input (' Digite seu nome completo: ')).strip()
print (' Analisando seus dados...')
print ('='*40)
print (f''' Seu nome em maiusculas é {nome.upper()}
 Seu nome em minúsculas é {nome.lower()}
 Seu nome tem ao todo {len(nome) - nome.count(' ')} letras
 Seu primeiro nome tem {nome.find(' ')} letras''')
