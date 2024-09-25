def evaluate(expression):
    def operator_precedence(operator):
        if operator in ["+", "-"]:
            return 1  # lower precedence
        elif operator in ["*", "/"]:
            return 2  # higher precedence
        return 0  # default no precedence

    def calculate(operators, values):
        if len(values) < 2:
            raise ValueError("Niewystarczająca liczba elementów na stosie wartości")
        if not operators:
            raise ValueError("Nie podano operatora")
        right = values.pop()  # get right operand
        left = values.pop()  #  get left operand
        operator = operators.pop()  # get operator
        if operator == "+":
            values.append(left + right)
        elif operator == "-":
            values.append(left - right)
        elif operator == "*":
            values.append(left * right)
        elif operator == "/":
            if right == 0:
                raise ValueError("Dzielenie przez zero")
            values.append(left / right)
        else:
            return None

    values = []  # temporary storage for operands
    operators = []  # temporary storage for operators
    i = 0

    while i < len(expression):
        if expression[i] == " ":  # in case char is blank space - skip blank spaces
            i += 1
            continue

        if expression[i].isdigit():  # in case char is number (with one or more digits)
            num = 0
            while i < len(expression) and expression[i].isdigit():  # evaluates number with multiple digits
                num = num * 10 + int(expression[i])
                i += 1
            values.append(num)  # adds number to values
            i -= 1  # returns 1 step back, so iteration does not skip next char after number

        elif expression[i] in ["+", "-", "*", "/"]:  # in case char is operator
            while operators and operator_precedence(operators[-1]) >= operator_precedence(expression[i]):
                #  check if operator has higher precedence than top of stack
                calculate(operators, values)  # calculate expression if it has higher precedence
            operators.append(expression[i])  # adds new operator to stack

        i += 1

    while operators:  # calculate remaining expression
        calculate(operators, values)

    return values[0]  # return result (only one value in stack)

if __name__ == "__main__":
    while True:
        expression = input("Podaj wyrażenie do obliczenia: ")
        result = evaluate(expression)
        print(f"Wynik wyrażenia {expression} to: ", result)
        repeat = input("Czy chcesz wykonać kolejne obliczenie? (t/n): ")
        if repeat in ['t', 'T', 'y', 'Y']:
            continue
        else:
            print("Dziśkuje za użycie kalkulatora. Do zobaczenia")
            break

