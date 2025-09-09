def notes (*values, show=False):
    """
    -> Function for analyzing students grades and situations
    :param values: Students grades
    :param show: To show the situation or not
    :return: dicionary with lots of student information
    """
    sum = 0
    for v in values:
        sum += v
    average = sum/len(values)
    if average < 5.9:
        sit = 'bad'
    elif 5.9 < average < 7:
        sit = 'reasonable'
    else:
        sit = 'good'
    tot = {'total': len(values), 'Larger': max(values), 'Smaller': min(values), 'Average': f'{average:.2f}'}
    if show:
      tot ['Situation'] = sit
    return tot


#Main Program
resp = notes (7.5, 8.5, 6.9, 9.4,)
help(notes)