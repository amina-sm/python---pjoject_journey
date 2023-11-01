#calculator
#add

calculation_ending= False
def add(n1,n2):
    return n1 +n2
def subtract(n1,n2):
    return n1- n2
def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/ n2


operations={"+": add,
            "-":subtract,
            "*":multiply, 
            "/":divide
            }
def calculator():
    num1= float(input("What is the first number?: "))
    for operation in operations:
        print(operation)
    while  not calculation_ending: 
        operation_symbol=input("Pick an operation : ") 
        num2=float(input("what is the next number? : ")) 
        calculator_function= operations[operation_symbol]
        answer= calculator_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2}= {answer}")
        if input(f"Type 'y' to continue calculating with  {answer} , or type 'n' to exit.: ")=="y":
            num1=answer
        else:
            calculation_ending= True   
            calculator() 
    
calculator()
    # operation_symbol=input("Pick an operation from the line above: ")    
    # num3=int(input("what is the third number? : ")) 
    # calculator_function= operations[operation_symbol]
    # second_answer= calculator_function(First_answer, num3)
    # print(f"{First_answer} {operation_symbol} {num3}= {second_answer}")


