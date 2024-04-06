import logo


def add(n1, n2):
    return n1 + n2


def multiple(n1, n2):
    return n1 * n2


def subtract(n1, n2):
    return n1 - n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiple,
    "/": divide
}


def calculator():
    print(logo.logo)
    while True:
        try:
            num1 = int(input("Input your first number please: "))
            break  # break the loop if the conversion to integer successful
        except ValueError:
            print("Input number only!")

    is_continue = True
    operation_symbol = ''
    num2 = 0

    # Looping for check the operators
    while is_continue:
        for symbols in operations:
            print(symbols)
        check_operators = True
        while check_operators:
            operation_symbol = input("Pick one of the operators above: ")
            if operation_symbol in operations:
                while True:
                    try:
                        num2 = int(input("Input your second number please: "))
                        break  # break the loop
                    except ValueError:
                        print("Input number only!")
                check_operators = False
            else:
                print("Input again the operators!")

        # call the function first
        function = operations[operation_symbol]
        answer = function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        decision = input(f"Type 'y' to continue with {answer} or 'n' if you want to start with new number or 'x' to "
                         f"exit: ").lower()
        if decision == "y":
            num1 = answer
        elif decision == "n":
            is_continue = False
            calculator()
        elif decision == "x":
            print("Exiting the program, Thank you!")
            return
        else:
            print("You input wrong keyword")
            calculator()


calculator()
