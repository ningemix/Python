## Aprovando empréstimo

from time import sleep
print (' \033[33;41mCONSULTA  DE EMPRÉSTIMO\033[m ')
print(
)
print('='*40)
casa = float ( input (' \033[36mValor da casa: R$\033[m'))
salário = float ( input (' \033[36mSeu salário: R$\033[m'))
anos = int ( input (' \033[36mEm quantos anos vai pagar: \033[m'))

print()
print(' ANALISANDO SEU PERFIL...')
print()
sleep(2)
print ('='*40)

prest = casa / 12 / anos
porcentagem = 30/100 * salário

frase = (f'Para pagar uma casa de R${casa:.2f} em {anos} anos a prestação será de R${prest:.2f} por mês')

if prest <= porcentagem:
      print(f' {frase}. \033[32mSeu empréstimo foi aceito :)\033[m')
else:
      print (f' {frase}. \033[31mSeu empréstimo foi negado :(\033[m ')
print()
print (' Tenha um bom dia!')

