# makes sure you only have 2 options

def yes_no_validator(a, b, user_input):
    user_input = user_input.lower()
    while user_input != a and user_input != b:
        user_input = input("Please enter a valid option: ")
    if user_input == a:
        print(f"You said {a}.")
    else:
        print(f"You said {b}")

# yes/no example - can be any two option
message = input("Would you like  a pizza ('yes' or 'no')? ")       
yes_no_validator('yes', 'no', message)



# three options

def valid_3(a, b, c, user_input):
    user_input = user_input.lower()
    while user_input != a and user_input != b and user_input != c:
        user_input = input("Please enter a valid option: ")
    if user_input == a:
        print(f"You chose {a}.")
    elif user_input== b:
        print(f"You chose option {b}.")
    else:
        user_input = "b"
        print(f"You chose option {c}")
        
        
message1 = input("Would you like  a pizza, burger or pasta ('1' or '2' or '3')? ")       
valid_3('1', '2', '3', message1)

    
