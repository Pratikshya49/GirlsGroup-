def multiply(num1, num2):
    return num1 * num2

def subtract(num1, num2):
    result = num1 - num2
    return result

def divide(num1, num2):
    if num2 == 0:
        return "Error: Cannot divide by zero!"
    return num1 / num2

# Main program
print("Calculator Operations:")
print("1. Multiply")
print("2. Subtract")
print("3. Divide")

choice = input("Choose operation (1-3): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    result = multiply(num1, num2)
    print(f"{num1} × {num2} = {result}")
elif choice == '2':
    result = subtract(num1, num2)
    print(f"{num1} - {num2} = {result}")
elif choice == '3':
    result = divide(num1, num2)
    print(f"{num1} ÷ {num2} = {result}")
else:
    print("Invalid choice")