def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def main():
    num1 = 10
    num2 = 5
    print("Addition result:", add(num1, num2))
    print("Subtraction result:", subtract(num1, num2))
    print("Multiplication result:", multiply(num1, num2))
    print("Division result:", divide(num1, num2))

if __name__ == "__main__":
    main()
