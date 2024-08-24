def calc():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    choice = int(input("Choose between 1-4: "))

    def operator(num1, num2, operation):
        if operation == '1':
            return num1 + num2
        elif operation == '2':
            return num1 - num2
        elif operation == '3':
            return num1 * num2
        elif operation == '4':
            if num2 != 0:
                return num1 / num2
            else:
                return "Division by zero"
        else:
            return "Invalid choice"

    result = operator(num1, num2, str(choice))  # Convert choice to string to match function signature
    print(f"The result of the operation with {num1} and {num2} is: {result}")

# options to chose 1-4rr
print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

if __name__ == "__main__":
    calc()