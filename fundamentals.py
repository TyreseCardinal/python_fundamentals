number = 0
is_true = False


if (number > 10):
  print('Number is larger than 10')
else:
  print('Number is smaller than 10')

  if (number < 0 and is_true == True):
    print('Negative and True')
  elif (number > 0 and is_true == False):
    print('Positive and False')
  elif (number > 100 or is_true == True):
    print('Large or True')
  else:
    print('I do not know')