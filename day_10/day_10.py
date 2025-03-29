# Functions with output
def my_function():
  result = 3 * 2
  return result


def format_name(f_name, l_name):
  formated_f_name = (f_name.title())
  formated_l_name = (l_name.title())


  return (f"{formated_f_name} {formated_l_name}")

print(format_name("giorgi", "dzabilashvili"))


def function_1(text):
  return text + text

def  function_2(text):
  return text.title()

output = function_2(function_1("hello"))
print(output) 

# Docstrings
"""Take a first and last name and format it to 
   return title case version of the name"""