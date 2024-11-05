import random

#Ask the user for input
a = input("Roll the dice? (y/n):")
a = a.lower()

#For invalid request
while(a != "y" and a != "n"):
  print("Invalid choice!")
  a = input("Roll the dice? (y/n):")

#If the choice is YES!
while(a == "y"):
  print(f" ( {random.randint(1,6)} , {random.randint(1,6)})")
  a = input("Roll the dice? (y/n):")

#If the choice is NO!
if(a == "n"):
  print("Thanks for playing.")
