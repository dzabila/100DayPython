# Number Guessing Game
import random
random_number = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

difficulity = input("Choose a difficulity. Type 'easy' or 'hard': ")
lives = 0
if difficulity == "easy":
  lives = 10
elif difficulity == "hard":
  lives = 5
else:
  print("Invalid input")
game_over = False
print(f"You have {lives} attempts remaining to guess the number.")
guess = int(input("Make a Guess:  "))
while game_over == False:
  if guess != random_number:
    lives -= 1
    if lives == 0:
      print("you lost")
      game_over = True
    elif guess < random_number:
      print("Too low.")
      print("Guess again.")
      print(f"You have {lives} attempts remaining to guess the number.")
      guess = int(input("Make a Guess:  "))
    else:
      print("Too high.")
      print("Guess again.")
      print(f"You have {lives} attempts remaining to guess the number.")
      guess = int(input("Make a Guess:  "))
   
  elif guess == random_number:
    print(f"you got it! the answer was {random_number}")
    game_over = True
