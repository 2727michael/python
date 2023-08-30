#declaration of functions
def display_operations():
    print("0 - close program")
    print("1 - add task")
    print("2 - delete task")
    print("3 - show tasks")
    print("4 - show operations")

def show_tasks(tasks):
    print("your tasks:\n")
    for i in range(len(tasks)):
        print(i, tasks[i])
    
def add_task(tasks, i):
    tasks.append([])
    task_name = input("enter the name of the task: ")
    tasks[i].append(task_name)
    execution_date = input("enter the execution date DD/MM/YYYY: ")
    tasks[i].append(execution_date)
    execution_hour = input("enter the execution hour: ")
    tasks[i].append(execution_hour)

def del_task(tasks):
    show_tasks(tasks)
    delete = int(input("which one task u wanna delete: "))
    del tasks[delete]
    print(delete, " task has been removed!")

#declaration of variables
tasks = []
i = 0

#program
print("********** SIMPLE TO-DO LIST **********")
display_operations()

while(True):
    try:
        operation = int(input("select operation: "))

        match operation:
            case 1:
                add_task(tasks, i)
                i += 1
            case 2:
                del_task(tasks)
            case 3:
                show_tasks(tasks)
            case 4:
                display_operations()
            case 0:
                print("see you!")
                break
            case _:
                print("there is no such operation, try again")
        print("\n")
    except ValueError:
        print("Invalid value. Check that the entered data is correct.")
    except:
        print("An error occured, please try again")
        
        
