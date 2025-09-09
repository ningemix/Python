#Verificando as primeiras letras de um texto

'''cidade = str (input (' Nome da Cidade: '))
cidade = cidade.title()
cidade = cidade.split()
print ('Santo' in cidade)'''

cidade = str (input (' Nome da cidade: ')).strip()
print (cidade[:4] .upper() == 'SANTO')
