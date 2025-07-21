# Simple Calculator

# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Select operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

choice = input("Enter operation (+, -, *, /): ")

# Perform calculation
if choice == '+':
    result = num1 + num2
    print("Result:", result)
elif choice == '-':
    result = num1 - num2
    print("Result:", result)
elif choice == '*':
    result = num1 * num2
    print("Result:", result)
elif choice == '/':
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero!")
else:
    print("Invalid operation")
