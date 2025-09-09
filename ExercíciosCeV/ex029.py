#Radar eletrônico
from time import sleep
velocidade = int ( input (' Velocidade do carro: '))
limite = 80
multa= (velocidade - 80)*7 #Subtração para pegar a sobra do limite. Agora sei quantos km foram ultrapassados. Multipliquei pelo valor da multa.
print (' PROCESSANDO...')
sleep(2)
print('='*40)
if velocidade > limite:
      print (f' Você foi multado por ultrapassar o limite de {limite}km/h.\n Sua multa sairá por R${multa:.2f}.')
else:
      print (' Não levará multa')
print('='*40)
print (' Tenha um bom dia! Dirija com segurança!')


