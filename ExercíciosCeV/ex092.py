from datetime import date
data = dict ()
data ['name'] = str (input ('Type a name : '))
data ['age'] = int (input ('Type in your year of birth: '))
data ['ctps'] = int (input ('Work permit (0 has not): '))
if data ['ctps'] != 0:
    data ['hired'] = int (input ('Year hired: '))
    data ['salary'] = float (input ('Salary: '))
    data ['retirement'] = (data ['hired'] + 35) - data ['age']
    data ['age'] = date.today().year - data ['age']
print ('='*50)
print (data)
for d in data:
    print (f'{d} has the value', data[f'{d}'])
