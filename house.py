name = input('What is your name? ')

match name:
 case 'Harry' | 'Hermione'  | 'Ron':
  print('Gryffindor')
 case 'Drako':
  print('Slytherin')
 case _:
  print('Who?')