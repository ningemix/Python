data = {}
data ['Name'] = str (input ('Type a name: '))
data ['Average'] = float (input (f'Type the average of {data ['Name']}: '))
if data ['Average'] >= 7:
    data ['Situation'] = 'approved :)'
elif 5 <= data ['Average'] < 7:
    data ['Situation'] = 'recovery :|'
else:
    data ['Situation'] = 'failed :('
print ('='*18)
for k, c in data.items():
    print (k, 'equals', c)