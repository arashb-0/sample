def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y


def main():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    print("Type 'quit' to exit\n")

    while True:
        num1_input = input("Enter first number (or 'quit'): ")
        if num1_input.lower() == "quit":
            break

        operator = input("Enter operator (+, -, *, /): ")
        num2_input = input("Enter second number: ")

        try:
            num1 = float(num1_input)
            num2 = float(num2_input)
        except ValueError:
            print("Invalid number. Try again.\n")
            continue

        if operator == "+":
            result = add(num1, num2)
        elif operator == "-":
            result = subtract(num1, num2)
        elif operator == "*":
            result = multiply(num1, num2)
        elif operator == "/":
            result = divide(num1, num2)
        else:
            print("Invalid operator. Try again.\n")
            continue

        print(f"Result: {result}\n")

    print("Goodbye!")


if __name__ == "__main__":
    main()