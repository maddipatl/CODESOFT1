def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero."

# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display operation choices
print("Choose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Get the user's choice
choice = input("Enter the operation number (1-4): ")

# Perform the calculation based on the user's choice
if choice == '1':
    result = add(num1, num2)
    operation = "Addition"
elif choice == '2':
    result = subtract(num1, num2)
    operation = "Subtraction"
elif choice == '3':
    result = multiply(num1, num2)
    operation = "Multiplication"
elif choice == '4':
    result = divide(num1, num2)
    operation = "Division"
else:
    result = "Invalid input"
    operation = "Unknown operation"

# Display the result
print(f"{operation} result: {result}")
