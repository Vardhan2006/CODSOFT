def calculator():
    print("********** Simple Calculator **********")
    print("Operations: +, -, *, /, %, **")
    print("***************************************")

    try:
        a = float(input("Enter value 1: "))
        b = float(input("Enter value 2: "))
        c = input("Enter an operator: ")

        match c:
            case "+":
                result = a + b
                operation = "Addition"
            case "-":
                result = a - b
                operation = "Subtraction"
            case "*":
                result = a * b
                operation = "Multiplication"
            case "/":
                if b == 0:
                    raise ValueError("Division by zero is not allowed.")
                result = a / b
                operation = "Division"
            case "%":
                if b == 0:
                    raise ValueError("Modulo by zero is not allowed.")
                result = a % b
                operation = "Modulo"
            case "**":
                result = a ** b
                operation = "Exponentiation"
            case _:
                raise ValueError("Invalid operator.")
        
        print("***************************************")
        print(f" {a} {c} {b} = {result} ")
        print("***************************************")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Invalid input: {e}")

# Run the calculator
calculator()
