data = dict ()
full = list ()
female = list ()
tot_age = 0
while True:
    data [f'name'] = str (input ('Type a name: '))
    while True:
        data [f'sex'] = str (input ('Enter the gender [F/M]: ')).upper()[0]
        if data ['sex'] in 'FM':
            break
        else:
            print ('Error! Please, type only M ou F.')
    if data [f'sex'] == 'F':
        female.append(data [f'name'])
    data [f'age'] = int (input ('Type a age: '))
    tot_age += data [f'age']
    full.append (data.copy())
    data.clear()
    while True:
        quest = str (input ('Want to continue? [Y/N]: ')).upper()[0]
        if quest in 'YN':
            break
        else:
            print ('Error! Please, type only Y ou N.')
    if quest == 'N':
        average = tot_age / len (full)
        break
print ('='*40)
print (f'-The group has {len (full)} people')
print (f'-The average age is {average:.2f}')
print ('-The women registered were:', *female, sep = ' ')
print ('-List of people who are above average:')
for c in full:
    if (c['age']) > average:
        print (f'Name = {c ['name']}; Sex = {c['sex']}; Age = {c['age']};')
