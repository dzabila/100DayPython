import random
import for_import
rps = [for_import.rock, for_import.paper, for_import.scissors]
random_number = random.randint(0, 2)

user_choose = input("Choose :  Rock / Paper / Scissors  ").lower()

if user_choose == "rock" and rps[random_number] == for_import.rock:
  print(f"You Choose : \n {for_import.rock}")
  print(f"Computer Choose: \n {for_import.rock}")
  print("Tie")
elif user_choose == "rock" and rps[random_number] == for_import.paper:
  print(f"You Choose : \n {for_import.rock}")
  print(f"Computer Choose: \n {for_import.paper}")
  print("You lose")
elif user_choose == "rock" and rps[random_number] == for_import.scissors:
  print(f"You Choose : \n {for_import.rock}")
  print(f"Computer Choose: \n {for_import.scissors}")
  print("You win")
else:
  print("Invalid input")
if user_choose == "paper" and rps[random_number] == for_import.rock:
  print(f"You Choose : \n {for_import.paper}")
  print(f"Computer Choose: \n {for_import.rock}")
  print("You win")
elif user_choose == "paper" and rps[random_number] == for_import.paper:
  print(f"You Choose : \n {for_import.paper}")
  print(f"Computer Choose: \n {for_import.paper}")
  print("Tie")
elif user_choose == "paper" and rps[random_number] == for_import.scissors:
  print(f"You Choose : \n {for_import.paper}")
  print(f"Computer Choose: \n {for_import.scissors}")
  print("You lose")
else:
  print("Invalid input")
if user_choose == "scissors" and rps[random_number] == for_import.rock:
  print(f"You Choose : \n {for_import.scissors}")
  print(f"Computer Choose: \n {for_import.rock}")
  print("You lose")
elif user_choose == "scissors" and rps[random_number] == for_import.paper:
  print(f"You Choose : \n {for_import.scissors}")
  print(f"Computer Choose: \n {for_import.paper}")
  print("You win")
elif user_choose == "scissors" and rps[random_number] == for_import.scissors:
  print(f"You Choose : \n {for_import.scissors}")
  print(f"Computer Choose: \n {for_import.scissors}")
  print("Tie")
else:
  print("Invalid input")


# variant 2

if user_choose == "rock":
  if rps[random_number] == for_import.rock:
    print(f"You Choose : \n {for_import.rock}")
    print(f"Computer Choose: \n {for_import.rock}")
    print("Tie")
  elif rps[random_number] == for_import.paper:
    print(f"You Choose : \n {for_import.rock}")
    print(f"Computer Choose: \n {for_import.paper}")
    print("You lose")
  elif rps[random_number] == for_import.scissors:
    print(f"You Choose : \n {for_import.rock}")
    print(f"Computer Choose: \n {for_import.scissors}")
    print("You win")
  else:
    print("Invalid Input")
elif user_choose == "paper":
  if rps[random_number] == for_import.rock:
    print(f"You Choose : \n {for_import.paper}")
    print(f"Computer Choose: \n {for_import.rock}")
    print("You win")
  elif rps[random_number] == for_import.paper:
    print(f"You Choose : \n {for_import.paper}")
    print(f"Computer Choose: \n {for_import.paper}")
    print("Tie")
  elif rps[random_number] == for_import.scissors:
    print(f"You Choose : \n {for_import.paper}")
    print(f"Computer Choose: \n {for_import.scissors}")
    print("You lose")
  else:
    print("Invalid Input")
elif user_choose == "scissors":
  if rps[random_number] == for_import.rock:
    print(f"You Choose : \n {for_import.scissors}")
    print(f"Computer Choose: \n {for_import.rock}")
    print("You lose")
  elif rps[random_number] == for_import.paper:
    print(f"You Choose : \n {for_import.scissors}")
    print(f"Computer Choose: \n {for_import.paper}")
    print("You win")
  elif rps[random_number] == for_import.scissors:
    print(f"You Choose : \n {for_import.scissors}")
    print(f"Computer Choose: \n {for_import.scissors}")
    print("Tie")
  else: 
    print("Invalid Input")
else:
  print("Invalid Input")