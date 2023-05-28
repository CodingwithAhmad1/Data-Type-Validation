# to  make sure entries are only letters, not numbers
def validation(user_input) -> None:
    message1 = user_input.replace(" ", "")  
    while not message1.isalpha():
        user_input = input("Enter a valid string: ")
        message1 = user_input.replace(" ", "")  


message = input("Enter string: ")

validation(message)


       
       