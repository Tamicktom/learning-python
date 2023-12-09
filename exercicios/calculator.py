

while True:
    print("Options:")
    print("Enter [1] to 'add' to add two numbers")
    print("Enter [2] to 'subtract' to subtract two numbers")
    print("Enter [3] to 'multiply' to multiply two numbers")
    print("Enter [4] to 'divide' to divide two numbers")
    print("Enter [5] to 'quit' to end the program")

    option = input("Enter your choice: ")
    option = option.lower()

    if option == "quit" or option == "5" or option == "q":
        break
    if option != "add" and option != "subtract" and option != "multiply" and option != "divide" and option != "1" and option != "2" and option != "3" and option != "4":
        print("Unknown input")
        continue

    num1 = input("Enter first number: ")

    if num1.isdigit() == False:
        print("Unknown input")
        continue
    else:
        num1 = float(num1)

    num2 = int(input("Enter second number: "))

    if num2.isdigit() == False:
        print("Unknown input")
        continue
    else:
        num2 = float(num2)

    if option == "add" or option == "1":
        print(num1, "+", num2, "=", num1 + num2)
    elif option == "subtract" or option == "2":
        print(num1, "-", num2, "=", num1 - num2)
    elif option == "multiply" or option == "3":
        print(num1, "*", num2, "=", num1 * num2)
    elif option == "divide" or option == "4":
        print(num1, "/", num2, "=", num1 / num2)
    else:
        print("Unknown input")
        continue

    print()
