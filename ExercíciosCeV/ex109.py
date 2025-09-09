from module.m107_108_109_110_112 import m109

num = float (input ('Type a price: R$'))
print (f'Half of {m109.currency(num)} is {m109.half(num, True)}')
print (f'Double of {m109.currency(num)} is {m109.double(num, True)}')
print (f'Increasing 10% of {m109.currency(num)} we have {m109.increasing(num, 10, False)}')
print (f'by reducing 13% of 1{m109.currency(num)} we have {m109.reducing(num, 13, False)}')