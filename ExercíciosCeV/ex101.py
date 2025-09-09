from datetime import date


def vote (year):
    current_year = date.today().year
    i = current_year - year
    if i < 16:
        return f'{i} years old: no vote.'
    elif i > 70 or 15 < i < 18:
        return f'{i} years old: optional vote.'
    elif 17 < i < 71:
        return f'{i} years old: compulsory voting.'


year = int (input ('What year were your born? '))
print (vote (year))