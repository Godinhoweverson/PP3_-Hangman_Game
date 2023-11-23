import random
import american_countries
import asian_countries
import european_countries
import hangman_stages
import hangman_art


def choice_continent():
    while True:
        try:
            choice_number = int(input(
                "Please select one continent from the following options:\n\n"
                " 1: American\n"
                " 2: Asian\n"
                " 3: Europe\n\n"
                " Please enter a number between 1 and 3: "))
            if 1 <= choice_number <= 3:
                break
            else:
                print('Ops! That was not a valid number. Try again\n\n')
        except ValueError:
            print('Please enter a number between 1 and 3.\n\n')
    return choice_number


def generate_word(number):
    if number == 1:
        return random.choice(american_countries.american_countries).upper()
    elif number == 2:
        return random.choice(asian_countries.asian_countries).upper()
    elif number == 3:
        return random.choice(european_countries.european_countries).upper()


def get_single_letter():
    while True:
        try:
            letter = input('Please enter a letter: \n').upper()
            if len(letter) == 1 and letter.isalpha():
                break
            else:
                print('Please enter one letter at a time. Try again!\n\n')
        except ValueError:
            print('Type one letter.\n\n')
    return letter


def play_again():
    while True:
        try:
            print("Would you like to play again?\n\n")
            repeat_game = input("Y or N: ").upper()
            if repeat_game == 'Y':
                print("Let's start!\n")
                main()
                break
            elif repeat_game == 'N':
                print("Thank you, see you next time!\n")
                break
        except ValueError:
            print('Please, Y or N\n\n')


def check_letter(word):
    correct_count = 0
    wrong_count = 6
    correct = ''
    wrong = ''

    while correct_count != len(word.replace(' ', '')) and wrong_count != 0:
        display = ''
        for letter in word:
            if letter in correct:
                display += f'{letter}'
            else:
                display += '_ '
        print(display)

        letter = get_single_letter()

        if letter in correct + wrong:
            print('You have attempted this letter')
            print('Please, try again!')
            continue

        if letter in word:
            print('You got the letter right!')
            correct += letter
            print("You have entered the following letters: \n\n"
                  f"{correct + wrong}\n\n")
            correct_count += word.count(letter)
            if correct_count == len(word.replace(' ', '')):
                print("You won the game! Congratulations!\n")
                print(f"The country is {word}\n\n")
                play_again()
        else:
            print('You got the letter wrong!')
            wrong += letter
            print("You have entered the following letters: \n\n"
                  f"{correct + wrong}\n\n")
            wrong_count -= 1
            print(hangman_stages.stages[wrong_count])
            if wrong_count == 0:
                print(f"The country was {word}\n\n")
                print("You lost the game. Better luck next time!\n\n")
                play_again()


def main():
    hangman_art.welcome()
    option_number = choice_continent()
    word = generate_word(option_number)
    check_letter(word)


main()
