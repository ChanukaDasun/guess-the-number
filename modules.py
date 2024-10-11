

def check_input_type(input_value, upper_limit, lower_limit):
    try:
        input_value = int(input_value)
        if not(input_value >= lower_limit and input_value <= upper_limit):
            print("Guessed number out of range!")
            exit(0)
    except Exception as e:
        print(f"Invalid input type: Error:{e}")

    return input_value

def return_message(user_value, random_value, upper_limit, lower_limit, no_of_guessings):

    message = ""
    
    if user_value >= lower_limit and user_value < random_value:
        message += "You Guessed too small!"
    elif user_value > random_value and user_value <= upper_limit:
        message += "You Guessed too high!"
    elif user_value == random_value:
        message += f"Congratulations you did it in {no_of_guessings} try!"

    return message