
# Creates the "arithmetic_arranger" function that takes two arguments: 
# problems and val, where val is automatically set to be false.
def arithmetic_arranger(problems, val=False):
  # Setup variable - arranged_problems to be an empty string.
  arranged_problems = ''
  # Initial test. If there are more than 5 elements in the argument 
  # 'problems', the program will return the error. 
  if len(problems) > 5:
    return "Error: Too many problems."

  # Creating the operations variable, which will list the operators from '1 + 2'
  # type statements. lambda x is for small throwaway functions and map takes functions
  # as the first argument. x.split()[1] takes the second item from a list. 
  operations = list(map(lambda x: x.split()[1], problems))
  # if-statement for another test. if the set of operations from the above statmement
  # does not contain '+' or '-' and the length of the set of operations does not = 2, 
  # the function will return an error. 
  if set(operations) != {'+','-'} and len(set(operations)) != 2:
    arranged_problems = "Error: Operator must be '+' or '-'."
    return arranged_problems
    
  # Creating an empty list for the numbers in the problems.
  numbers = []
  # For-loop for each element in the given 'problems' argument
  for i in problems:
    # Creating the 'p' variable that splits the individual elements given from 'problems'
    p = i.split()
    # Adds the 1st and 3rd variable from each split to the 'numbers' list
    numbers.extend([p[0], p[2]])

  # if-statement for testing if the numbers are digits or not. 
  # lambda x goes through each variable in 'numbers and creates a map (list) of True/False
  # based on if the numbers are digits or not.
  if not all(map(lambda x: x.isdigit(), numbers)):
    arranged_problems = "Error: Numbers must only contain digits."
    return arranged_problems

  # if-statement for testing if the length of the numbers exceed 10
  # map (list) is created from iterating through each element in 'numbers' and checking if 
  # the length is < 5. List of True/False. 
  if not all(map(lambda x: len(x) < 5, numbers)):
    arranged_problems = "Error: Numbers cannot be more than four digits."
    return arranged_problems

  print(numbers)
  # creating 'top_row' string variable
  top_row = ''
  # 'dashes' string variable
  dashes = ''
  # 'values' variable that contains a list of the solved problems from each element of 'problems'
  values = list(map(lambda x: eval(x), problems))
  # 'solutions' string variable
  solutions = ''
  # for-loop that goes through the range 0-length of 'numbers' and steps to every other element
  for i in range(0, len(numbers), 2):
    space_width = max(len(numbers[i]), len(numbers[i + 1])) + 2
    top_row += numbers[i].rjust(space_width)
    dashes += '-' * space_width
    solutions += str(values[i // 2]).rjust(space_width)
    if i != len(numbers) - 2:
      top_row += ' ' * 4
      dashes += ' ' * 4
      solutions += ' ' * 4

  bottom_row = ''
  for i in range(1, len(numbers), 2):
    space_width = max(len(numbers[i - 1]), len(numbers[i])) + 1
    bottom_row += operations[i // 2]
    bottom_row += numbers[i].rjust(space_width)
    if i != len(numbers) - 1:
      bottom_row += ' ' * 4

  if val:
    arranged_problems = '\n'.join((top_row, bottom_row, dashes, solutions))
  else:
    arranged_problems = '\n'.join((top_row, bottom_row, dashes))
  return arranged_problems

print(arithmetic_arranger(['3 + 855', '988 + 40', '99 - 22'], True))
