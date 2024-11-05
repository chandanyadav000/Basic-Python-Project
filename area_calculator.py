import math
while (True):

  x = '''
Press 1 to get the area of square 🟨.
Press 2 to get the area of rectangle 🟩.
press 3 to get the area of circle.
press 4 to get the area of triangle
press 5 to close.
'''
  print(x)
  while True:

    try:
      y = int(input("Enter a number between 1 -5 :"))
      break

    except ValueError:
      print("Enter valid value.")

  #for valid number check
  if(y != 1 and y != 2 and y != 3 and y != 4 and y != 5):
      print("Enter valid number.")

  # for square 🟨
  elif(y == 1):
      while True:
        try:
          l = int(input("Enter length of square 🟨:"))
          break 
        except ValueError:
          print("Please enter a valid length. 🟨")

      s_a = l ** 2
      print(f"The area of square 🟨 having length {l} is {s_a}")

  #for rectangle 🟩
  elif(y == 2):
    while True:
      try:
        l = int(input("Enter length of rectangle🟩:"))
        b = int(input("Enter breadth of rectangle🟩:"))
        break
      except ValueError:
        print("Print valid length 🟩")
    r_a = l * b
    print(f"The area of rectangle 🟩 having length {l} and breadth {b} is {r_a}")  

  #for circle 🔵
  elif(y == 3):
    while True:
      try:
        r = int(input("Enter radius of circle🔵:"))
        break
      except ValueError:
        print("Enter valid radius 🔵")
    c_a = (math.pi) * (r ** 2)
    print(f"The area of circle 🔵 having radius {r} is {c_a}")

  #for triangle 📐
  elif(y == 4):
    while True:
      try:
        a = int(input("Enter first side of triangle📐:"))
        b = int(input("Enter second side of a triangle📐:"))
        c = int(input("Enter third side of a triangle📐:"))
        break
      except ValueError:
        print("Enter valid sides of triangle📐.")
    s = (a + b + c)/2
    t_c = (s * (s-a) * (s-b) * (s-c))**(1/2)
    print(f"The area of traingle📐 having sides {a} , {b} , {c} is { t_c}")

        

  

  #for closing
  elif(y == 5):
    print("Thank You!")
    break



