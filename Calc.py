def multiply(num1, num2):
    return num1 * num2

def subtract(num1, num2):
    result = num1 - num2
    return result

# Main program
print("Calculator Operations:")
print("1. Multiply")
print("2. Subtract")

choice = input("Choose operation (1-2): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    result = multiply(num1, num2)
    print(f"{num1} × {num2} = {result}")
elif choice == '2':
    result = subtract(num1, num2)
    print(f"{num1} - {num2} = {result}")
else:
    print("Invalid choice")