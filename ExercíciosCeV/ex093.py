data = {}
goals = []
total = 0
data ['name'] = str (input ('Type a name: '))
match = int (input (f'How many matches did {data ['name']} play? '))
for n in range (0, match):
    data ['goals'] = int (input (f'how many goals in the match {n}? '))
    total += data ['goals']
    goals.append(data['goals'])
data ['goals'] = goals
data ['total'] = total
print ('='*70)
print (data)
print ('='*70)
for d, c in data.items():
    print (f'The field {d} has the value {c}')
print ('='*70)
print (f'{data['name']} played {len (data)} matches')
for e, p in enumerate (data ['goals']):
    print (f'   => In the match {e}, scored {p} goals ')
print (f'A total of {total} goals')
