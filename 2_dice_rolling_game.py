import random
print("welcome to the game.")

while True:
  #Ask for input
  a = input("Roll the dice? (y/n):").lower()
  #For invalid request
  if(a != "y" and a != "n"):
    print("Invalid Request!")
  #If the choice is YES!
  elif(a == "y"):
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    print(f"({d1},{d2})")
  #If the choice is NO!
  elif(a == "n"):
    print("Thank You For Playing!")
    break



  #End of code
    
