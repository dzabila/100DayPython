# Dictionaries
# dictionarishi informacia inaxeba key:value principit
colours = {
  "apple" : "red",
  "pear" : "green",
  "banana":  "yellow",
  1: "giorgi"
}
# itemis wamogeba dictionaridan

print(colours["pear"])


colours["peach"] = "pink"


colours["apple"] = "green"
print(colours)
# marto key ebs daabrunebs
for thing in colours:
  print(thing)



# student_scores = {
#     'Harry': 88,
#     'Ron': 78, 
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }

# student_grades = {}

# for thing in student_scores:
#     if 91 <= student_scores[thing]<= 100:
#          student_grades[thing]= "Outstanding"
#     elif 81 <= student_scores[thing]<= 90:
#         student_grades[thing] = "Exceeds Expectations"
#     elif 71 <= student_scores[thing]<= 80:
#         student_grades[thing] = "Acceptable"
#     else:
#         student_grades[thing] = "fail"
    

# print(student_grades)



# Nesting
capitals = {
  "France" : "Paris",
  "Germany" : "Berlin"
}

# travel_log = {
#   "France": ["pariz", "Lille", "Dijon"],
#   "Germany": ["Stuttgart", "Berlin"]
# }
# print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])


travel_log = {
  "France": {
    "num_times_visited": 8,
    "cities_visited": ["pariz", "Lille", "Dijon"],
  },
  
  "Germany": {
    "numb_times_visited": 5,
    "cities_visited": ["Stuttgart", "Berlin"],
  }
}
print(travel_log["Germany"]["cities_visited"][0])