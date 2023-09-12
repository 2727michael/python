# program that creates the file
print("If u want to stop entering text, use Ctrl+c")

# asking about file name
file_name = input("Input your file name: ")     


try: 
    # creating and opening a new file in append mode
    with open(file_name, "a") as file:
        print("Input text:")
        
        # if user hit enter program won't stop 
        while True:
            string = input()
            file.write(string + '\n')
# ending program in a safe way
except KeyboardInterrupt:           
    pass