expression = str ( input (' Type a expression: '))
pile = []

for exp in expression:
      if exp == '(':
            pile.append ('(')
      elif exp == ')':
            if len (pile) > 0:
                  pile.pop ()
            else:
                  pile.append (')')
                  
if len (pile) == 0:
      print (' The expression is correct')
else:
      print (' The expression is not correct')