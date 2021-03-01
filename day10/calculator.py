from calculator_art import logo

print(logo)


#Calculator

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    num1 = float(input("What's the first number?: "))

    should_continue = True
    while should_continue:
        operation_symbol = input(f"Pick an operation {operations.keys()}: ")
        num2 = float(input("What's the next number?: "))
        result = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {result}")

        additional_calc = input(f"Type 'y' to continue calculation with {result}, type 'n' to start a new calculation or exit to close the app: ")
        if additional_calc == "y":
            num1 = result
        elif additional_calc == "n":
            should_continue = False
            calculator()
        else:
            should_continue = False

calculator()            