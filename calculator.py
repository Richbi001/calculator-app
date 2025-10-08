def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def main():
    print("Welcome to the Calculator!")
    print("1. Add")
    print("2. Subtract")
    choice = input("Enter choice (1/2): ")

    if choice in ['1', '2']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print("Result:", add(num1, num2))
        else:
            print("Result:", subtract(num1, num2))
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
