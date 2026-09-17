def add():
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    print(f"Addition is {n1 + n2}")

def sub():
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    print(f"Subtraction is {n1 - n2}")

def mul():
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    print(f"Multiplication is {n1 * n2}")

def divi():
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    print(f"Division is {n1 / n2}")

while True:
    print("Select any option: + - / *:")

    op = input("Enter the operation to perform: ")
    if op == "exit":
        print("exited")
        break
    elif op == "+":
        add()
    elif op == "-":
        sub()
    elif op == "*":
        mul()
    elif op == "/":
        divi()
    else:
        print("Invalid input")