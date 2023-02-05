# get first number
# get operation to be performed
# get second number
# perform operation to get result
# display result
# ask to continue operation from result
# ask to start new operation
# ask to exit program

def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return round(num1 * num2, 2)


def div(num1, num2):
    try:
        res = round(num1 / num2, 2)
    except ZeroDivisionError:
        res = "Cannot divide by zero"
    return res


def get_operation(num1):
    operations = ['+', '-', '*', '/']
    # Get operation
    while True:
        op_code = input("Select operation: '+', '-', '*', '/'\n>>").strip()[0]
        if op_code in operations:
            break
        else:
            print("Invalid input... Try again...")
    # Get second number
    num2 = 1
    while True:
        try:
            num2 = int(input("Enter second number:\n>>").strip())
        except ValueError:
            print("Invalid input... Try again...")
            continue
        break
    return [op_code, num2]


def perform_operation(num1, op_code, num2):
    operations = {'+': add, '-': sub, '*': mul, '/': div}
    res = operations[op_code](num1, num2)
    return res


if __name__ == '__main__':
    number1 = 0
    while True:
        # Get first number
        while True:
            try:
                number1 = int(input("Enter first number:\n>>").strip())
            except ValueError:
                print("Invalid input... Try again...")
                continue
            break
        while True:
            op, number2 = get_operation(number1)
            print(f"Performing the calculation for: {number1} {op} {number2}")
            result = perform_operation(number1, op, number2)
            print(f"Result: {result}")

            cont = input("\nContinue with this result?'yes' or 'no'\n>>").strip().lower()
            # Perform invalid input check
            if cont == "yes":
                print()
                number1 = result
                continue
            else:
                end = input("Close calculator?'yes' or 'no'\n>>").strip().lower()
                if end == "yes":
                    exit(0)
                else:
                    print()
                    break

