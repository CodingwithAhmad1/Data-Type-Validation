# to  make sure entries are only letters, not numbers and allow re-entry
def validation(user_input) -> None:
    while not message1.isalpha():
        user_input = input("Enter a valid string: ")
    return user_input


message = input("Enter string: ")

message = validation(message)


       
       
