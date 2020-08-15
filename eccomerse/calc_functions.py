def calculater(n1, n2, op):

    if op == "+":
        print(n1 + n2)

    elif op == "*":
        print(n1 * n2)

    elif op == "-":
        print(n1 - n2)

    elif op == "/":
        print(n1 / n2)

    return n1, n2


if __name__ == "__main__":
    op = input("Enter an operator: ") # command line
    """
        Gets the operator from an input on awebpage and also the two numbers
    """

    print(calculater(n1, n2, web_op))
