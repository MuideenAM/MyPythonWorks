def new_line():
  print('.')

def three_lines():
  new_line()
  new_line()
  new_line()

def nine_lines():
  three_lines()
  three_lines()
  three_lines()

def clear_screen():
  print('Calling clear_screen()')
  i = 1
  while(i <= 2):
    nine_lines()
    three_lines()
    i += 1

  new_line()

print('Printing nine lines')
nine_lines()
clear_screen()


  

