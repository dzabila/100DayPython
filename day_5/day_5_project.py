import random
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9" ]
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password? \n"))
nr_symbols = int(input("How many symbols woluld you like? \n"))
nr_numbers = int(input("How many numbers would you like? \n"))

# # For easy level
# password = ""

# for letter in range(0, nr_letters):
#   random_number = random.randrange(0, len(letters))
#   password += letters[random_number]
# for symbol in range(0, nr_symbols):
#   random_number = random.randrange(0, len(symbols))
#   password += symbols[random_number]
# for number in range(0, nr_numbers):
#   random_number = random.randrange(0, len(numbers))
#   password += str(numbers[random_number])

# print(password)

# For random places
password = []

for letter in range(0, nr_letters):
  password.append(random.choice(letters))
for symbol in range(0, nr_symbols):
  password.append(random.choice(symbols))
for number in range(0, nr_numbers):
  password.append(random.choice(numbers))
# me am logikit gavakete metodis codnis gareshe rac imas nishnavs rom dzerski var
# new_password = ""
# for i in range(0, len(password)):
#   random_choice = random.choice(password)
#   new_password += random_choice
#   password.remove(random_choice)

random.shuffle(password)
# join it shegvidzlia vaqciot stringad listi
password = "".join(password)
print(password)