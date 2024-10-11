import random
import math
from modules import check_input_type, return_message, check_int, check_upper_lower_bound

def main():
    upper_bound = input("Enter upper bound of the range: ")
    upper_bound = check_int(upper_bound)
    lower_bound = input("Enter lower bound of the range: ")
    lower_bound = check_int(lower_bound)

    check_upper_lower_bound(upper_bound, lower_bound)

    random_number = random.randint(lower_bound, upper_bound)

    minimum_no_of_guesses = math.ceil(math.log2(upper_bound - lower_bound + 1))

    print(f"You've only {minimum_no_of_guesses} chances to guess the integer!")

    no_of_guessings = 1

    while (no_of_guessings <= minimum_no_of_guesses):

        input_number = input("Guess a number: ")
        input_number = check_input_type(input_number, upper_bound, lower_bound)

        message = return_message(input_number, random_number, upper_bound, lower_bound, no_of_guessings)
        print(message)

        if input_number == random_number:
            break
        elif minimum_no_of_guesses == no_of_guessings:
            print("Insufficient chances!")

        no_of_guessings += 1


if __name__ == "__main__":
    main()
