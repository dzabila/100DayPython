# Blind auction program
# this is for claning screen
# print("\n" * 100)
hammer = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                   jgs/_______________\
'''
print(hammer)
print("Welcom to Auction!!!")
auction_participants = {}

name = input("What is your name?:  ")
bid = int(input("What is your bid?:  $"))
auction_participants[name] = bid
answer = input("Are there any participiants?: Yes/No   ").lower()
print("\n" * 100)
while answer != "no":
  name = input("What is your name?:  ")
  bid = int(input("What is your bid?:  $"))
  auction_participants[name] = bid
  answer = input("Are there any participiants?: Yes/No   ").lower()
  print("\n" * 100)


max_value = 0
max_name = ""
for item in  auction_participants:
  if auction_participants[item] > max_value:
    max_value = auction_participants[item]
    max_name = item

print(f"Auction winner is {max_name} with {max_value} dollars!")