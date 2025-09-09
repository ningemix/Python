valores = []

for v in range (0, 5):
      valores.append (int ( input (f'Digite um valor para a posição {v}: ')))
      
print ('='*40)      
print (f'Você digitou os valores {valores}')
maior = max (valores)
menor = min (valores)

print (f'O maior valor digitado foi {maior} nas posições', end = ' ')
for i, v in enumerate (valores):
      if v == maior:
            print (i, end = '... ')
            
print (f'\nO menor valor digitado foi {menor} nas posições', end = ' ')
for i, v in enumerate (valores):
      if v == menor:
            print (i, end = '... ')