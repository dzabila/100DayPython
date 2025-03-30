import random
import data
# GAME ASCII ART

game_logo = '''
  ___ ___ .__       .__                  
 /   |   \|__| ____ |  |__   ___________ 
/    ~    \  |/ ___\|  |  \_/ __ \_  __ \
\    Y    /  / /_/  >   Y  \  ___/|  | \/
 \___|_  /|__\___  /|___|  /\___  >__|   
       \/   /_____/      \/     \/       
.__                                      
|  |   ______  _  __ ___________         
|  |  /  _ \ \/ \/ // __ \_  __ \        
|  |_(  <_> )     /\  ___/|  | \/        
|____/\____/ \/\_/  \___  >__|           
                        \/     
'''


vs = '''   
___  ________
\  \/ /  ___/
 \   /\___ \ 
  \_//____  >
          \/ 
'''


game_over = False
option_1 = random.choice(data.data)
option_2 = random.choice(data.data)
score = 0

def compare(opt1, opt2):
  if opt1["follower_count"] > opt2["follower_count"]:
    return "a"
  else:
    return "b"
print(game_logo)
while game_over == False:
  print(f"Compare A: {option_1["name"]}, {option_1["description"]}, from {option_1["country"]}")
  print(vs)
  print(f"Against B: {option_2["name"]}, {option_2["description"]}, from {option_2["country"]}")
  choose = input("Who has more followers? Type 'A' or 'B':  ")
  print("\n" * 100)
  if choose == compare(option_1, option_2):
    score += 1
    print(f"You are right! Current Score: {score}")
    if choose == "b":
      option_1 = option_2
      option_2 = random.choice(data.data)
    else:
      option_2 = random.choice(data.data)
  else:
    print(f"Sorry, that's wrong. Final score {score}")
    game_over = True