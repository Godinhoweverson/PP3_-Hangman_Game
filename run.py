# Import the 'random' module to use later for selecting a random country.
import random           


# Importing the 'american_countries' module.
import american_countries

# Importing the 'asian_countries' module.
import asian_countries

# Importing the 'european_countries' module.
import european_countries



# variables

correct_letter = ''
wrong_letter = ''

# Function to display the welcome message and instructions for the Hangman game.
def welcome():
     # ASCII art for the word "Hangman".
    hangman_art = '''
     _    _                                         
    | |  | |                                        
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
    |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                         __/ |                      
                        |___/    
    Welcome to Hangman!
    '''

    print(hangman_art)
    # Display the game instructions for the player.
    print("\nYou have three options of continents to choose from.")
    print("\nYour goal is to guess the name of a country within the chosen continent.")
    print("\nTry to guess the country before the hangman is complete. Let's begin!")

# Call the 'welcome()' function to start the game.
welcome()

def choice_continent():
   # Function to get the user's choice for a continent.
    while True:
        try:
             # Use 'input' to get user input and 'int' to convert it to an integer.
            choice_number = int(input("Please select one continent from the following options: \n\n 1: American \n 2: Asian \n 3: Europe \n\n Please enter a number between 1 and 3: "))
            
             # Check if the input is within the valid range (1 to 3).
            if choice_number >= 1 and choice_number <= 3:
                break # Exit the loop if the input is valid.
            else:
                 # If the input is not valid, inform the user and prompt again.
                print('Ops! That was not a valid number. try again\n\n')     
        except ValueError:
            print('Please enter a number between 1 and 3.\n\n')
    
    # Return the valid choice number.
    return choice_number
               
 # Call the function to get the user's choice and store it in 'option_number'.   
option_number = choice_continent()

def generate_word(number):
     # Function to generate a random country name based on the selected continent number.
           
    # If the number is 1, choose a random country from the 'american_countries' list and return it.
    if number == 1:
          return random.choice(american_countries.american_countries).upper()
       
     # If the number is 2, choose a random country from the 'asian_countries' list and return it.
    elif number == 2:
        return random.choice(asian_countries.asian_countries).upper()
    
     # If the number is 3, choose a random country from the 'european_countries' list and return it.
    elif number == 3:
        return random.choice(european_countries.european_countries).upper()

# Call the 'generate_word' function that will return random country.
word = generate_word(option_number)
print(word)

def generate_blank_space(item):
     # Function to generate a string of blank spaces based on the length of generate word.

    letter_blank = '- ' * len(item)  # Create a string of '-' characters repeated for the length of the item.
    print(letter_blank)  # Print the generated string of blank spaces.

# Call the function and pass the 'word' variable that is the return of generate_word's function.
generate_blank_space(word)

def check_letter(word):
    score_correct_letter = 0
    score_wrong_letter = 6

    while score_correct_letter != 7 and score_wrong_letter != 0:
        letter = input('Please enter a letter: ').upper()
        if letter in word:
            print('voce acertou')
            print(letter)
            score_correct_letter =+ 1
            print(score_correct_letter)
        else:
            print('voce errou')
            score_wrong_letter -= 1


check_letter(word)

def win_game():
    pass

def lost_game():
    pass
