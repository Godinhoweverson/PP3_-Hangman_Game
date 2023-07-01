# Import the 'random' module to use later for selecting a random country.
import random           

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
    pass

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
