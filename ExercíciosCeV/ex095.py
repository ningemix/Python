dic = {}
goal = []
goals = []
data = []
while True:
    total = 0
    print ('='*40)
    dic ['name'] = str (input ('Type a name: '))
    dic ['matches'] = int (input (f'How many matches did {dic ['name']} play? '))
    for c in range (0, dic ['matches']):
        goal.append (int (input (f'How many goals in the match {c}? ')))
    for c in goal:
        total += c
    dic ['total'] = total
    goals.append (goal[:])
    goal.clear()
    data.append (dic.copy())
    quest = str (input ('Want to continue? [Y/N]: ')).lower()
    if quest == 'n':
        break
print ('=-'*40)
print ('Cod name      Goals                Total')
print ('='*40)
for c in range (0, len (data)):
    print (f'{c:<3} {data [c]['name']:<9} {str (goals[c]):<20} {data [c]['total']}')
while True:
    while True:
        print('=' * 40)
        quest = int (input ('Show which players data? [999 to close]: '))
        if quest < len (data) or quest == 999:
            break
        else:
            print (f'Error! There is no player with code {quest}! Try again')
    if quest == 999:
        break
    print (f'-- PLAYER SURVEY {data [quest]['name']}:')
    for c in range (0, len (goals[quest])):
        print (f'   In game {c} he score {goals [quest][c]} goals')
