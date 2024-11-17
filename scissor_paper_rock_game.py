import random
choice = {
  1 : "scissor",
  2 :"paper",
  3 : "rock"

}

rev_choice = {
  "s" : 1,
  "p" : 2, 
  "r" : 3
}

full_form = {
  "s" : "scissors",
  "p" : "paper",
  "r" : "rock"
}
sign_c = {
  1 : "✌️",
  2 : "✋",
  3 : "✊"
}
sign_a = {
  "s" : "✌️",
  "p" : "✋",
  "r" : "✊"

}


i = 0     #counting rounds of playing
w = 0     #counting wins
d = 0     #counting draws
l = 0     #counting computer wins

while True:
  c = random.randint(1,3)

  a = input("Rock, paper , scissors? (r,p,s) enter n to close the game :").lower()

  if(a  not in ["r", "p","s", "n"]):
    print("Not valid!")
  elif(a in ["r", "p" , "s" ]):
    print(f'''Pushpa choosed = {choice[c]} {sign_c[c]} 
    Chandan choosed  = {full_form[a]} {sign_a[a]}''')
    a = rev_choice[a]
    i += 1

  if(a == 1 and c == 2):                                             #1 = s  2 = p 3 = r
    print("You won! 🥳")
    w += 1
  elif(a == 1 and c == 3):
    print("You loose!🥲")
    l += 1
  elif(a == 2 and c == 1):
    print("You loose!🥲")
    l += 1
  elif(a == 2 and c == 3):
    print("You won! 🥳")
    w += 1
  elif(a == 3 and c == 1):
    print("You won! 🥳")
    w += 1
  elif(a == 3 and c == 2):
    print("You loose!🥲")
    l += 1
  elif(a == c):
    print("Draw")
    d += 1
  elif(a == "n"):
    print("Thank You for playing!❤️")
    print(f"You played {i} times.")
    print(f"You won {w} times.")
    print(f"Draw {d} times")
    print(f"Computer won {l} times.")
    break

  

  


  
