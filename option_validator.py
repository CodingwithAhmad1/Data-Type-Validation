# makes sure you only have 2 options - yes or no

def yes_no_validator(a, b, user_input):
    user_input = user_input.lower()
    while user_input != a and user_input != b:
        user_input = input("Please enter a valid option: ")
    if user_input == a:
        print("You said yes.")
    else:
        print("You said no")


message = input("Would you like  a pizza ('y' or 'n')? ")       
yes_no_validator('y', 'n', message)





















# three options

def valid_3(a, b, c, user_input):
    user_input = user_input.lower()
    while user_input != a and user_input != b and user_input != c:
        user_input = input("Please enter a valid option: ")
    if user_input == a:
        print("You chose option 1.")
    elif user_input== b:
        print("You chose option 2.")
    else:
        user_input = "b"
        print("You chose option 3")
        
        
message1 = input("Would you like  a pizza, burger or pasta ('a' or 'b' or 'c')? ")       
valid_3('a', 'b', 'c', message1)

    