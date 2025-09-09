def area (a, b):
    r = a * b
    print (f'The area of a plot {a}x{b} is {r}m²')


#Programa principal
print ('Land Control'.center (30))
print ('='*30)

width = float (input ('Width: '))
length = float (input ('Length: '))
area (width, length)
