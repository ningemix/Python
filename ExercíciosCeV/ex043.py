## Índice de Massa Corporal

peso = float ( input (' Digite o seu peso (kg): '))
altura = float ( input (' Digite sua altura (m): '))
print ()

# Calculando o IMC:
imc = peso / altura**2


print (f' O IMC dessa pessoa é de {imc:.1f}')

if imc < 18.5:
      print (' Abaixo do peso')
      
elif imc < 25:
      print (' Peso ideal ')
      
elif imc < 30:
      print (' Sobrepeso ')
      
elif imc < 40:
      print (' Obesidade ')

else:
      print (' Obesidade mórbida, cuidado!')
 