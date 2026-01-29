def dynamic_calculator():
    print("===== Dynamic Calculator =====")
    print("You can use +, -, *, / and parentheses ()")
    print("Example: 1+2*3*(4-5/4)-(3/5)")
    print("Type 'exit' to quit\n")

    while True:
        expression = input("Enter expression: ")

        if expression.lower() == "exit":
            print("Calculator closed.")
            break

        try:
            expression = expression.replace("×", "*").replace("÷", "/")

            result = eval(expression)
            print("Result:", result)
        except Exception:
            print("Invalid expression! Please try again.")
dynamic_calculator()