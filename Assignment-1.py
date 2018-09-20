while True:
    num1 = input("Enter first Number: ")
    if (num1 == "q"):
        exit(0)
    else:
        try:
            num1 = int(num1)
            break
        except ValueError:
            print("Please try again: ")


while True:
    operator = input("Enter method [+,-,*,/]: ")
    if (operator == "+" or operator == "-" or operator == "*" or operator == "/"):
        break
    elif (operator == "q"):
        exit(0)
    else:
        True


while True:
    num2 = input("Enter second number: ")
    if (num2 == "q"):
        exit(0)
    else:
        try:
            num2 = int(num2)
            break
        except ValueError:
            print("Please try again: ")

def calc(num1, operator, num2):

    if (operator == "+"):
        ans = num1 + num2
    elif (operator == "-"):
        ans = num1 - num2
    elif (operator == "*"):
        ans = num1 * num2
    elif (operator == "/"):
        ans = num1 / num2

    print('Answer is ', ans)




while True:
  try:
      choice = input('Press q to stop: ')

      if (choice == "Q" or choice == "q"):
        break
  except ValueError:
      print("Try again")

print("Done")
