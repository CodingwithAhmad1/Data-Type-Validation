# to  make sure entries are only numbers

def validation(user_input):
    while True:
        message1 = user_input.replace("+", "").replace("-", "").replace(" ", "")

        if message1.isnumeric(): # to make sure input is only letters
            break
        else:
            user_input = input("Enter a valid number: ")


message = input("Enter number: ")
 
             
validation(message)



       
