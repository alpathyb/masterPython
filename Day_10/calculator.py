import logo

print(logo.logo)


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

start_calculator = True
while start_calculator:
    num1 = int(input("Input your first number: "))
    num2 = int(input("Input your second number: "))

    for operators in operations:
        print(operators)

    operators_symbol = input("Pick one of the operation above: ")


    def check_operation(answer_n1):
        temp_answer = 0
        for action in operations:
            if operators_symbol == action:
                function = operations[operators_symbol]
                temp_answer = function(answer_n1, num2)
                break
        else:
            print("You put the wrong operators!")

        return temp_answer


    answer = check_operation(answer_n1=num1)
    if answer != 0:
        print(f"{num1} {operators_symbol} {num2} = {answer}")

    is_continue = True
    while is_continue:
        continue_calculate = input(f"Type Y to continue calculation with {answer} or type N to start over: ").lower()
        if continue_calculate == 'n':
            is_continue = False
            break
        operators_symbol = input("Pick again one of the operation above: ")
        num2 = int(input("Input your second number: "))
        temp2_answer = answer
        answer = check_operation(answer_n1=answer)
        print(f"{temp2_answer} {operators_symbol} {num2} = {answer}")

    continue_calculator = input(f"Do you want to use calculator? type y to continue use or type n to exit: ").lower()
    if continue_calculator == "n":
        print("Thank you for using this Calculator!")
        start_calculator = False

