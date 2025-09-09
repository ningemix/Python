# Seno, Cosseno e Tangente:
print ('='*40)
from math import radians, sin, cos, tan
ângulo = float ( input (' Digite o ângulo que você deseja: '))
seno = sin (radians(ângulo))
cosseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))
print (f' O ângulo de {ângulo} tem o SENO de {seno:.2f}\n O ângulo de {ângulo} tem o COSSENO De {cosseno:.2f}\n O ângulo {ângulo} tem a TANGENTE {tangente:.2f}')
print ('='*40)