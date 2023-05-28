# makes sure you only have 2 options

def valid_3(a, b, user_input):
    user_input = user_input.lower()
    while user_input != a and user_input != b:
        user_input = input("Please enter a valid option: ")
    return user_input
    

# yes/no example - can be any two option
message = input("Would you like  a pizza ('yes' or 'no')? ")       
message = valid_3('yes', 'no', message)



# three options

def valid_3(a, b, c, user_input):
    user_input = user_input.lower()
    while user_input != a and user_input != b and user_input != c:
        user_input = input("Please enter a valid option: ")
    return user_input
        
        
message1 = input("Would you like  a pizza, burger or pasta ('1' or '2' or '3')? ")       
message1 = valid_3('1', '2', '3', message1)

    
