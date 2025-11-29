#Calculator Program in Python

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def power(a, b):
    return a ** b

def fraction(a, b):
    if b == 0:
        return "Error: Denominator cannot be zero."
    return a / b

print("Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Power ")
print("6. Fraction)")

choice = input("Enter your choice (1/2/3/4/5/6): ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", subtract(num1, num2))
elif choice == '3':
    print("Result:", multiply(num1, num2))
elif choice == '4':
    print("Result:", divide(num1, num2))
elif choice == '5':
    print("Result:", power(num1, num2))
elif choice == '6':
    print("Result:", fraction(num1, num2))
else:
    print("Invalid choice. Please select a valid operation.")
