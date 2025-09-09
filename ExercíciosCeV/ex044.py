## Gerenciador de Pagamentos

from time import sleep

v = float ( input (' \033[1;33;41mValor da compra:\033[m '))
print()
sleep(1)
print ('='*40)

print (' (\033[1;31m1\033[m) À vista: \033[1;33m10% de desconto\033[m           |\n (\033[1;32m2\033[m) À vista no cartão: \033[1;33m5% de desconto\033[m  |\n (\033[1;34m3\033[m) Em até 2x no cartão: \033[1;33mpreço normal\033[m  |\n (\033[1;35m4\033[m) 3x ou mais no cartão: \033[1;33m20% de juros\033[m |')
print ('='*40)
print()
sleep(1)

f = float ( input (' \033[1;33;41mEscolha uma das formas de pagamento acima:\033[m '))

print()

#Calculando as condições de pagamento:
op1 = v - (10/100 * v)
op2 = v - (5/100 * v)
op3 = v / 2


if f == 1:
      print (f' \033[32m À vista sua compra de R${v:.2f} ganha 10% de desconto e sairá por R${op1:.2f}\033[m')
     
elif f == 2:
      print(f' \033[32mSua compra à vista no cartão sairá de R${v:.2f} por R${op2:.2f} reais.\033[m')
      
elif f == 3:
      print (f' \033[32mSua compra sairá em 2x de R${op3:.2f}\033[m')
      
elif f == 4:
      p = int ( input (' Quantas parcelas? '))
      op4_= v + (20/100 * v)
      op4 = op4_ / p
      print (f' \033[32mSua compra sairá em {p}x de R${op4:.2f}. Com o juros, a sua compra de R${v:.2f} vai custar R${op4_:.2f}\033[m')

else:
      print (' \033[31mOpção inválida. Tente novamente.\033[m')