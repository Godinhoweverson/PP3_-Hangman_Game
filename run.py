# Import the 'random' module to use later for selecting a random country.
import random           


# Importing the 'american_countries' module.
import american_countries

# Importing the 'asian_countries' module.
import asian_countries

# Importing the 'european_countries' module.
import european_countries



# variables
score_correct_letter = 0
score_wrong_letter = 0
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

    while True:
        try:
            choice_number = int(input("Please select one continent from the following options: \n\n 1: American \n 2: Asian \n 3: Europe \n\n Please enter a number between 1 and 3: "))
            if choice_number >= 1 and choice_number <= 3:
                break
            else:
                print('Ops! That was not a valid number. try again\n\n')     
        except ValueError:
            print('Please enter a number between 1 and 3.\n\n')
    
    if choice_number == 1:
          return random.choice(american_countries.american_countries)

    elif choice_number == 2:
        return random.choice(asian_countries.asian_countries)
    

    elif choice_number == 3:
        return random.choice(european_countries.european_countries)
               
    
choice_continent()

def generate_word():
    pass

def generate_blank_space():
    pass

def check_letter():
    pass

def win_game():
    pass

def lost_game():
    pass
