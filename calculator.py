def display_operations():
    print("""
0 - close program
1 - addition
2 - subtraction
3 - multiplication
4 - division""")

print("Welcome in calculator")
display_operations()

    
while(True):
    try:
        print("\n")
    
        operation = int(input("select operation: "))
        if operation == 9:
            display_operations()
            continue
        elif operation == 0:
            print("see you!")
            break
        
        number1 = int(input("put a first number: "))
        number2 = int(input("put a second number: "))
    
        match operation:
            case 1:
                print("result of addition: ", number1 + number2)
            case 2:
                print("result of subtraction: ", number1 - number2)
            case 3:
                print("result of multiplication: ", number1 * number2)
            case 4:
                print("result of division: ", number1 / number2)
            case _:
                print("there is no such operation, try again")
        
        print("\nif u want to see a list of operations, enter 9")
        
    except ZeroDivisionError:
        print("you can't divide by zero!")

            
    
    
    
    