num1 = float(input("Number 1: "))
op = input("Operator: ")

while op not in ["+", "-", "*", "/"]:
    print("Operator must be either +, -, * or /")
    op = input("Operator: ")

num2 = float(input("Number 2: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    while num2 == 0:
        print("Number must not be 0!")
        num2 = float(input("Number 2: "))
    print(num1 / num2)


