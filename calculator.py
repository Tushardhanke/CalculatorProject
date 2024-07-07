def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def calculator():
    print("Basic Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")

    while True:
        choice = input("Enter your choice (1-5): ")
        if choice == "5":
            break
        elif choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please try again.")
            continue

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == "1":
            result = add(num1, num2)
        elif choice == "2":
            result = sub(num1, num2)
        elif choice == "3":
            result = mul(num1, num2)
        elif choice == "4":
            result = div(num1, num2)

        print(f"Result: {result:.2f}")

if __name__ == "__main__":
    calculator()