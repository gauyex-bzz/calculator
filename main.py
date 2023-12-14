num1 = float(input("1st number: "))
op = input("Operator: ")

while op not in ["+", "-", "*", "/"]:
    print("Operator must be either +, -, * or /")
    op = input("Operator: ")

num2 = float(input("2nd number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    while num2 == 0:
        print("Number must not be 0!")
        num2 = float(input("2nd number: "))
    print(num1 / num2)

if __name__ == "__main__":
    True
