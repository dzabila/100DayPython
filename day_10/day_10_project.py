calculator = '''
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''
# Tu gvinda funqciis mnishvneloba shevinaxot cvladshi frchxilebi ar unda davuwerot: variable = my_function
def add(n1, n2):
  return n1 + n2
def substract(n1, n2):
  return n1 - n2
def multiply(n1, n2):
  return n1 * n2
def division(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": division,
}
answer = "n"
while answer == "n":
  print("\n" * 100)
  print(calculator)

  first_number = input("What's the first number?:   ")
  print("+\n-\n*\n/")
  operation = input("Pick an operation: ")
  second_number = input("What's the next number?:   ")
  result = operations[operation](float(first_number), float(second_number))
  text = f"{float(first_number)} {operation} {float(second_number)} = {result}"
  print(text)
  answer = input(f"Type 'y' to continue calculationg with {result}, or type 'n' to start a new calculation")
while answer == "y":
  print("+\n-\n*\n/")
  operation = input("Pick an operation: ")
  second_number = input("What's the next number?:   ")
  first_number = result
  result = operations[operation](result, float(second_number))
  text = f"{float(first_number)} {operation} {float(second_number)} = {result}"
  print(text)
  answer = input(f"Type 'y' to continue calculationg with {result}, or type 'n' to start a new calculation")


# aq vamatebt frchxilebs, ase shegvidzlia funqciis gamoyeneba
# print(operations["*"](2,4))