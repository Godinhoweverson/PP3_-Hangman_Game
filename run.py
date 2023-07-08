import random
"""Import the 'random' module
to use later for selecting a random country."""

# Importing the 'american_countries' module.
import american_countries

# Importing the 'asian_countries' module.
import asian_countries

# Importing the 'european_countries' module.
import european_countries

# Importing the 'hangman_stages' to use when the letter is wrong.
import hangman_stages

import hangman_art


def choice_continent():
    # Function to get the user's choice for a continent.
    while True:
        try:
            """Use 'input' to get user input and
             'int' to convert it to an integer."""
            choice_number = int(input("Please select one continent from the following options: \n\n"
                         " 1: American \n"
                         " 2: Asian \n"
                         " 3: Europe \n\n"
                         " Please enter a number between 1 and 3: "))
            # Check if the input is within the valid range (1 to 3).
            if choice_number >= 1 and choice_number <= 3:

                # Exit the loop if the input is valid.
                break

            else:
                # If the input is not valid, inform the user and prompt again.
                print('Ops! That was not a valid number. try again\n\n')
        except ValueError:
            print('Please enter a number between 1 and 3.\n\n')
    # Return the valid choice number.
    return choice_number


def generate_word(number):
    """Function to generate a random country name
    based on the selected continent number.
    If the number is 1, choose a random country from
    the 'american_countries' list and return it."""
    if number == 1:
        return random.choice(american_countries.american_countries).upper()

    elif number == 2:
        return random.choice(asian_countries.asian_countries).upper()

    elif number == 3:
        return random.choice(european_countries.european_countries).upper()


def get_single_letter(letter):
    """ This function enables the player to type only one letter at a time.
    If the player attempts to type two or more letters, they will not be able
    to proceed until they have typed a single letter.
    This function can be called within the check_letter()"""
    while True:
        try:
            letter = input('Please enter a letter: \n').upper()
            if len(letter) == 1:
                break
            else:

                print('Please enter one letter at a time. Try again!\n\n')
        except ValueError:
            print('type one letter.\n\n')
    return letter


def play_again():
    while True:
        try:
            print("Would you like to play again?\n\n")
            repeat_game = input("Y or N:  ").upper()
            if repeat_game == 'Y':
                print("Let's start!\n")
                main()
            elif repeat_game == 'N':
                print("Thank you, see you next time!\n")
                break
            # else:
            #     print('Please, Y or N.\n\n')
        except ValueError:
            print('Please, Y or N\n\n')


def check_letter(word):
    # Counter for the number of correctly guessed letters
    correct_letter_count = 0
    # Counter for the number of incorrectly guessed letters
    wrong_letter_count = 6
    # String to store correctly guessed letters
    correct = ''
    # String to store incorrectly guessed letters
    wrong = ''

    # Continue until all letters are guessed
    # correctly or 6 wrong guesses are made
    while correct_letter_count != len(word.replace(' ', '')) and wrong_letter_count != 0:
        display = ''
        for letter in word:
            if letter in correct:
                display += f'{letter}'  # Display correctly guessed letters
            else:
                display += '_ '  # Display underscores for unguessed letters
        print(display)

        letter = get_single_letter(letter)

        if letter in correct + wrong:
            print('You have attempted this letter')
            print('Please, try again!')

            continue

        if letter in word:
            # The guessed letter is in the word
            print('You got the letter right!')
            # Add the correctly guessed letter to the 'correct' string
            correct += letter
            # Display the correctly guessed letters
            print("You have entered the following letters: \n\n"
            f"{correct + wrong}\n\n")

            # Increment the count of correct guesses
            correct_letter_count += word.count(letter)
            if correct_letter_count == len(word.replace(' ', '')):
                print("You won the game! Congratulations!\n")
                print(f"The country is {word}\n\n")
                play_again()

        else:
            # The guessed letter is not in the word
            print('You got the letter wrong!')
            # Add the incorrectly guessed letter to the 'wrong' string
            wrong += letter
            print("You have entered the following letters: \n\n"
            f"{correct + wrong}\n\n")
            # Increment the count of wrong guesses
            wrong_letter_count -= 1
            print(hangman_stages.stages[wrong_letter_count])
            if wrong_letter_count == 0:
                print(f"The country was {word}\n\n")
                print("You lost the game. Better luck next time!\n\n")
                play_again()


def main():
    hangman_art.welcome()
    option_number = choice_continent()
    word = generate_word(option_number)
    check_letter(word)


main()
