import math as m

def display_operations():
    print("""
0 - close program
1 - addition
2 - subtraction
3 - multiplication
4 - division
if u want to see more advanced operations, enter 5""")

def display_advanced_operations():
    print(""" 
6 - square root          
7 - the absolute value
8 - cosinus""")
    

print("Welcome in calculator")
display_operations()

    
while(True):
    try:
        print("\n")
        operation = int(input("select operation: "))
      
        if operation in [1, 2, 3, 4]:
            number1 = int(input("put a first number: "))
            number2 = int(input("put a second number: "))
        elif operation in [6, 7, 8]:
            number = int(input("put a number: ")) 
    
        match operation:
            case 1:
                print("result of addition: ", number1 + number2)
            case 2:
                print("result of subtraction: ", number1 - number2)
            case 3:
                print("result of multiplication: ", number1 * number2)
            case 4:
                print("result of division: ", number1 / number2)
            case 5:
                display_advanced_operations()
                continue
            case 6:
                print("the square root is: ", m.sqrt(number))
            case 7:
                print("the absolute value is: ", m.fabs(number))
            case 8:
                print("the cosinus is: ", m.cos(number))
            case 9:
                display_operations()
                continue
            case 0:
                print("see you!")
                break
            case _:
                print("there is no such operation, try again")
                
        
        print("\nif u want to see a list of operations, enter 9")
        
    except ZeroDivisionError:
        print("you can't divide by zero!")
    
    except ValueError:
        print("only numbers!")

            
    
    
    
    
