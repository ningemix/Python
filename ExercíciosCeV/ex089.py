full = []
students = []
grades = []

while True:
    students.append (str (input ('Name: ')))
    grades.append (float (input ('Grade 1: ')))
    grades.append (float (input ('Grade 2: ')))
    students.append (grades[:])
    grades.clear ()
    full.append (students[:])
    students.clear ()
    question = str (input ('Want to continue? '))
    if question == 'n':
        break
print ()
print ('Nº  Name    Average')
print ('='*25)
n = 0
for m in range (0, len (full)):
    print (f'{n:<4}', end = '')
    print (f'{full [n][0]:<12}', end = '')
    print (f'{(full [n][1][0] + full [n][1][1]) / 2:.1f}')
    n += 1
print ('='*25)

while True:
    quest = int (input ('Show grades of which student? (999 interrupt): '))
    if quest == 999:
        break
    print (f'{full [quest][0]} grades are', full [quest][1])
    print ('='*46)
    




