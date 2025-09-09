from module.m107_108_109_110_112 import m107_108

num = float (input ('Type a price: R$'))
print (f'Half of R${num} is R${m107_108.half(num)}')
print (f'Double of R${num} is R${m107_108.double(num)}')
print (f'Increasing 10% of R${num} we have R${m107_108.increasing(num, 10)}')
print (f'by reducing 13% of {num} we have R${m107_108.reducing(num, 13)}')