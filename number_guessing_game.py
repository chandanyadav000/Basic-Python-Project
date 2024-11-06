import random
b = random.randint(1,100) #generating random number

l = 1                     #for counting round
while True:             #for repeating till right number
              
    try:
      a = int(input("Guess a number between 1 and 100:"))
      
      if(a < 0 or a > 100):
        print("Number not in range.")
      elif(b > a):
        print("Guess higher number!")
      elif(b < a):
        print("Guess lower number!")
      elif( b == a):
        print(f"Congratulation.You guessed the right number.The number is {b}. You won the game in {l} round")
        break
      l += 1

         
       
    except ValueError:
      print("Invalid number.")

    

  



  