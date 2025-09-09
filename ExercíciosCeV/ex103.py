def file():
    name = str(input('players name: ')).strip()
    if name == '':
        name = '<desconhecido>'
    goals = str (input('Goal numbers: '))
    if goals.isnumeric():
        goals = int (goals)
    else:
        goals = 0
    print(f'{name} scored {goals} goal(s) in the championship')


file()


