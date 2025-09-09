from module.m107_108_109_110_112 import m107_108

num = float (input ('Type a price: R$'))
print (f'Half of {m107_108.currency(num)} is {m107_108.currency(m107_108.half(num))}')
print (f'Double of {m107_108.currency(num)} is {m107_108.currency(m107_108.double(num))}')
print (f'Increasing 10% of {m107_108.currency(num)} we have {m107_108.currency(m107_108.increasing(num, 10))}')
print (f'by reducing 13% of {m107_108.currency(num)} we have {m107_108.currency(m107_108.reducing(num, 13))}')