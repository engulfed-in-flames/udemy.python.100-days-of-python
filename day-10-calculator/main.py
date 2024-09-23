import art


def should_continue(result: float) -> bool:
    # fmt: off
    answer = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
    
    if answer == "y":
        return True
    else:
        return False


def calculator(operations: dict):
    print(art.logo)
    print("\n")

    calculating = True
    operand1 = float(input("What's the first number?: "))

    while calculating:
        for operator in operations:
            print(operator)

        operator = input("Pick an operation: ")
        operand2 = float(input("What's the next number?: "))
        result = operations[operator](operand1, operand2)

        print(f"{operand1} {operator} {operand2} = {result}")

        calculating = should_continue(result)

        if calculating:
            operand1 = result


operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}


calculator(operations)
