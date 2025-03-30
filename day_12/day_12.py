# Scope

enemies = 1


def increase_enemies():
  # gareta enemies rom shevcvalot unda shemovitanot rogorc globaluri cvladi
  global enemies
  enemies = 2
  print(f"enemies inside function: {enemies}")


increase_enemies()

print(f"enemies outside function: {enemies}")



# local scope

def drink_poision():
  potion_strength = 2
  print(potion_strength)

drink_poision()
# print(potion_strength) gamoitans name errors, radgan es cvladi localurs scoupshi aris da garedan ver vxedavt da ver vigebt mnishvnelobas
# magalitad tu garet ganvsazgvravdit cvlads, imas ukve globaluri skoupi eqneboda

# global scope

player_health = 10

def drink_potion():
  potion_strength = 2
  # amas ukve daprintavs radgan shignidan shegvidzlia mivwvdet garet, magram garedan shignit ver mivwvdebit
  print(player_health)

# block scoupi ar aris pitonshi
game_level = 3
enemies = ["enemie1", "enemie2", "enemie3"]
# aq chveulebriv vwvdebit cvlads magram rogorc ki funqciashi chavsvamt am logikas vegar mivwvdebit
if game_level < 5:
  new_enemy = enemies[0]

print(new_enemy)


# Global Constants

PI = 3.14159