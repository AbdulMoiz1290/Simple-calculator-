
# Simple Calculator in Python

def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice (1/2/3/4) or 'exit' to quit: ")

        if choice == 'exit':
            print("Exiting the calculator.")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"{num1} + {num2} = {num1 + num2}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {num1 - num2}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {num1 * num2}")
                elif choice == '4':
                    if num2 == 0:
                        print("Error: Division by zero.")
                    else:
                        print(f"{num1} / {num2} = {num1 / num2}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        else:
            print("Invalid choice. Please select a valid operation.")

calculator()