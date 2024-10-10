import random
import math
from modules import check_input_type, return_message

upper_bound = 100
lower_bound = 1

random_number = random.randint(lower_bound, upper_bound)

minimum_no_of_guesses = math.ceil(math.log2(upper_bound - lower_bound + 1))

no_of_guessings = 1

while (no_of_guessings <= minimum_no_of_guesses):

    print(random_number)

    input_number = input("Guess a number: ")
    input_number = check_input_type(input_number, upper_bound, lower_bound)

    message = return_message(input_number, random_number, upper_bound, lower_bound, no_of_guessings)
    print(message)

    if input_number == random_number:
        break