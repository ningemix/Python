#Primeira e última ocorrência de uma string

frase = str (input (' Digite uma frase: ')).upper() .strip()
letra= frase.count ('A')
começa = frase.find('A')+1
termina = frase.rfind('A')+1
print (f' A letra "A" aparece {letra} vez(es)\n Ela aparece pela primeira vez na posição {começa}\n Ela aparece pela última vez na posição {termina}') 

