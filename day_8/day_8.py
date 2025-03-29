# 
def my_function():
  print("This is my first function")

my_function()

def greet():
  for i in range(3):
    print("Hello")
greet()

# 
def greet_with_name(name):
  print(f"Hello {name}")
greet_with_name("Giorgi")

# Functions with more than 1 input

def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}")

greet_with("giorgi", "georgia")

# shegvidzlia order shevcvalot 
greet_with(location="giorgi",name="georgia")