# # # doctrin is a way of documenting python code as you along

# # calculator

def add(n1, n2):
    return n1+n2

# subracting

def sub(n1,n2):
    return n1 - n2

#multiplication

def mul(n1, n2):
    return n1*n2

# division

def div(n1, n2):
    return n1/n2


operations ={
    "+":add, 
    "-":sub,
    "*":mul, 
    "/":div
} 

def calculator():

    num1 = int(input("what is the first number?: "))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("pick an operation: ")
        num2 = int(input("what is your next number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with the answer, or 'n' to start a new process: ")== "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()
