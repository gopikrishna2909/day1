


def add(a,b):
    return a+b
def sub(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a/b

operations = {
    "+" : add,
    "-" : sub,
    "*" : multiply,
    "/" : divide
}
#print(operations["*"](2,4))

def calculator():
    num1 = float(input("What is the first number?: "))
    run = True
    while run:
        for i in operations:
            print(i)
        user_selected_operation = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        output = operations[user_selected_operation](num1,num2)
        user_choice = input(f"Typy 'y' to continue calculating with {output} or n to start with new number")
        if user_choice == "y":
            num1 = output
        else:
            run = False
            calculator()


calculator()





































































# num = True
# while num:
#     num1 = float(input("What is the first number?: "))
#     run = True
#     while run:
#         operation = input("+\n-\n*\n/\nPick an operation: ")
#         num2 = float(input("What is the next number?: "))
#         if operation == "+":
#             output = add(num1,num2)
#             print(f"{num1} + {num2} = {output}")
#             user_choice = input(f"Typy 'y' to continue calculating with {output} or n to start with new number")
#             if user_choice == "y":
#                 num1 =  output
#             else:
#                 run = False
#                 print("\n")
#         elif operation == "-":
#             output = sub(num1, num2)
#             print(f"{num1} - {num2} = {output}")
#             user_choice = input(f"Typy 'y' to continue calculating with {output} or n to start with new number")
#             if user_choice == "y":
#                 num1 = output
#             else:
#                 run = False
#         elif operation == "*":
#             output = multiply(num1, num2)
#             print(f"{num1} * {num2} = {output}")
#             user_choice = input(f"Typy 'y' to continue calculating with {output} or n to start with new number")
#             if user_choice == "y":
#                 num1 = output
#             else:
#                 run = False
#         elif operation == "/":
#             output = divide(num1, num2)
#             print(f"{num1} / {num2} = {output}")
#             user_choice = input(f"Typy 'y' to continue calculating with {output} or n to start with new number")
#             if user_choice == "y":
#                 num1 = output
#             else:
#                 run = False
#         else:
#             output = 0.0
#             print(f"{num1} Undefined {num2} = {output}")
#             user_choice = input(f"Typy 'y' to continue calculating with {output} or n to start with new number")
#             if user_choice == "y":
#                 num1 = output
#             else:
#                 run = False
#
#
