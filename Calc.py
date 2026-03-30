# subtraction.py

def subtract(num1, num2):
    result = num1 - num2
    return result

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = subtract(num1, num2)
print(f"Subtraction {num1} - {num2} = {result}")
