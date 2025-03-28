HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Hangman Project
import random
word_list = ["aardvark", "baboon", "camel"]
lives = 6
game_over = False

# random word
random_word = random.choice(word_list)
print(random_word)
# Print underscores as many as random_word length
placeholder = ""
for i in range(len(random_word)):
  placeholder += "_"
print(f"Guess the word: {placeholder}")
letters = []
# guess
while game_over != True:
  display = ""
  print(f"Your lives {lives}")
  print(HANGMANPICS[6 - lives])
  guess = input("Guess the letter: ").lower()
  for letter in random_word:
    if guess == letter:
      display += guess
      letters.append(guess)
      if display == random_word:
        print("You Win!")
        game_over = True
    elif letter in letters:
      display += letter
    else:
      display += "_"
  if guess not in random_word:
    lives -= 1
    if lives == 0:
      print(HANGMANPICS[-1])
      print("You Lose")
      print(f"Word was {random_word}")
      game_over = True

  print(display)
