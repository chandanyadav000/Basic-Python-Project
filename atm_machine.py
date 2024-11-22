'''
Enter your pin


If incorrect

repeat
again repeat
repeat again

print(sorry, your card has been blocked due to numeroues attempt)


if correct
show options

if chosen withdraw option
take input to enter amount and subtract it from main balance

if chosen depost option
take input to enter amount and add it to main balance

if chosen check balance
print balance

'''
pin = 2345
pin_cnt = 0
while True:
  entered_pin = int(input("Enter your pin:"))

  if(entered_pin != pin and pin_cnt < 3):
    print("Invalid pin")
    print("Attempts left", 3-pin_cnt)
    pin_cnt += 1

    
  elif(entered_pin != pin and pin_cnt >= 3):
    print("You entered wrong pin several times.Please try again later.")
    exit()

  elif(entered_pin == pin):

      option = int(input('''Choose the option you want: 
      1. Withdraw
      2. Deposit
      3. Check balance
      '''))

      match option:
        case 1:
          withdraw_amt = int(input("Enter the amount you want to withdraw:"))
          print(f"The amount you want to withdraw is" , withdraw_amt)

          with open("balance.txt", "r") as f:
            balance = int(f.read())

          if (balance < withdraw_amt):
            print("Insufficient balance!")

          else:
            new_balance = balance - withdraw_amt
            print(f"New balance after withdrawal is {new_balance}")

            with open("balance.txt" , "w") as f:
              f.write(str(new_balance))

        case 2:
          deposit_amt = int(input("Enter the amount you want to deposit:"))
          print(f"The amount you want to deposit is {deposit_amt}")

          with open("balance.txt" , "r") as f:
            balance = int(f.read())

          new_balance = balance + deposit_amt

          print(f"Your current balance is {new_balance}")

          with open("balance.txt" ,"w") as f:
            f.write(str(new_balance))

          break

          

        case 3:
          with open("balance.txt" , "r") as f:
            balance = f.read()

          print(f"Your current balance is {balance}")

          

          break
                

            

          


print("Thank you for using the atm.")



    

    






    
