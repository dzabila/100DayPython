# Control Flow
# > < >= <= == !=
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?  "))

# bill = 0
# if height > 120:
#   print("You can sit on the rollecoaster!")
#   age = int(input("Enter your age here:  "))
#   if age < 12:
#     bill = 5
#     print("Child tickets are 5$")
#   elif age > 18:
#     if(age >= 45 and age <= 55):
#       bill = 0
#       print("middle crysis people for free")
#     else:

#       bill = 12
#       print("Adult tickets are  12$")
#   else:
#     bill = 7
#     print("Youth tickets are 7$")

#   wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No.")
#   if wants_photo == "y":
#     bill += 3
#   print(f"Total charge will be {bill}")

# else:
#   print("You can not ride rollercoaster!")
                     
# # modulo operator % 
# print(10 % 3) 

# number = int(input("Enter your number here: "))
# if number % 2 == 0:
#   print("This number is Even")
# else:
#   print("This number is Odd")


# small pizza $15
# medium pizze $20
# large pizza $25
# pepperoni for small $2
# pepperoni for medium or large $3
# extra cheese 1$
# print("Welcome to Pytohone Pizza Deliveries!")
# size = input("What size pizza do you want? S, M or L: ").lower()
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
# extra_cheese = input("Do you want extra cheese? Y or N:").lower()

# bill = 0

# # todo: work out how much they need to pay based on their size choice
# if size == "s":
#   bill += 15
#   if pepperoni == "y":
#     bill += 2
#   if extra_cheese == "y":
#     bill += 1
#   print(f"Total: {bill}")
# elif size == "m":
#   bill += 20
#   if pepperoni == "y":
#     bill += 3
#   if extra_cheese == "y":
#     bill += 1
#   print(f"Total: {bill}")
# elif size == "l":
#   bill += 25
#   if pepperoni == "y":
#     bill += 3
#   if extra_cheese == "y":
#     bill += 1
#   print(f"Total: {bill}")

# else:
#   print("You typed wrong inputs")
# # todo: work out how much to add to their bill based on their pepperoni choice.


# # todo: work out their final amound based on wether if they want extra cheese.


# logical operators 
# and, or, not
# and aris true roca orivbe aris true
# or aris true roca erti mainc aris true
# not aris shebruneba not true aris false
# print(3 > 2 and 4 > 3)
# print(3> 2 or 2> 1)
# print(not True)