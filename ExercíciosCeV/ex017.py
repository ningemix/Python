# Catetos e Hipotenusa:
	
from math import sqrt
from emoji import emojize
print (emojize('Calculando o comprimento da hipotenusa :triangular_ruler:'))
print ('--'*19)
oposto = float ( input (' Comprimento do cateto oposto: '))
adjacente = float ( input (' Comprimento do cateto adjacente: '))
hipotenusa = oposto**2 + adjacente**2
print (f' O comprimento da hipotenusa é {sqrt(hipotenusa):.2f}')
print ('--'*19)

