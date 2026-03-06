# Simple Calculator Application

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


def main():
    print("===== SIMPLE CALCULATOR =====")

    while True:
        try:
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        print("\nSelect Operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")
        
        if choice == "5":
            print("Calculator closed. Goodbye!")
            break
    
        elif choice == "1":
            result = add(num1, num2)

        elif choice == "2":
            result = subtract(num1, num2)

        elif choice == "3":
            result = multiply(num1, num2)

        elif choice == "4":
            result = divide(num1, num2)

        elif choice == "5":
            print("Calculator closed. Goodbye!")
            break    

        else:
            print("Invalid choice. Please select a valid option.")
            continue

        print(f"\nResult: {result}")

        # Ask if user wants to claculate again
        again = input("\nDo you want another calculation? (y/n): ")
        if again.lower() != "y":
            print("Calculator Closed.")
            break


if __name__ == "__main__":
    main()