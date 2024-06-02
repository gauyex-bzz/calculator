from main import op


def get_operator(operator):
    while operator not in ["+", "-", "*", "/"]:
        print("Operator must be either +, -, * or /")
        operator = input("Operator: ")
        return operator


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    while num2 == 0:
        print("Number must not be 0!")
        num2 = float(input("2nd number: "))
    return num1 / num2


if __name__ == "__main__":
    if op == "+":
        add
    elif op == "-":
        subtract
    elif op == "*":
        multiply
    elif op == "/":
        divide
    else:
        print("Invalid operator")

