# Blackjack
import random


def deal_cards():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def check_cards(player, computer):
  if sum(computer) == 21:
    return 0
  elif sum(player) == 21:
    return 1

def blackjack():
  computer_cards = [deal_cards(), deal_cards()]
  player_cards = [deal_cards(), deal_cards()]
  print("------------Let's Play BlackJack!-------------")
  if check_cards(player_cards, computer_cards) == 0:
    print(f"Computer won with BlackJack!  {computer_cards}")
  elif check_cards(player_cards, computer_cards) == 1:
    print(f"Player won with BlackJack  {player_cards}") 
  else:
    print(f"Computer Card: {computer_cards[0]}")
    print(f"Player cards: {player_cards}")
    add_cards = input("Do you want to add Cards? Type Y / N  :").lower()
    while add_cards == "y":
      player_cards.append(deal_cards())
      if sum(player_cards) > 21:
        print(f"Player Cards {player_cards} ---> {sum(player_cards)}")
        print("Player burned, computer Won")
        return
      else:
        print(f"Player cards {player_cards} ---> {sum(player_cards)}")
        add_cards = input("Do you want to add Cards? Type Y / N  :").lower()
    while sum(computer_cards) < 17:
      computer_cards.append(deal_cards())
      if sum(computer_cards) > 21:
        print(f"Computer cards {computer_cards} ---> {sum(computer_cards)}")
        print("Computer burned, Player Wins!")
        return
      else:
        print(f"Computer cards {computer_cards} ---> {sum(computer_cards)}")
    if sum(player_cards) > sum(computer_cards):
      print(f"Player Won with {player_cards} ---> {sum(player_cards)}; Computer Cards {computer_cards} ---> {sum(computer_cards)}")
      return
    elif sum(computer_cards) > sum(player_cards):
      print(f"Computer Won with {computer_cards} ---> {sum(computer_cards)}; Player Cards {player_cards} ---? {sum(player_cards)}")
      return
    else:
      print(f"It is Draw! Computer Cards {computer_cards}; Player Cards {player_cards}")
      return
    

play = input("Do you want To play BlackJack?   Y / N    :").lower()
while play == "y":
  blackjack()
  play = input("Do You Want To Play Another Hand?  Y / N  :").lower()