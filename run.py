import random           

# variables

score_correct_letter = 0
score_wrong_letter = 0
correct_letter = ''
wrong_letter = ''

def welcome():
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
    print("\nYou have three options of continents to choose from.")
    print("\nYour goal is to guess the name of a country within the chosen continent.")
    print("\nTry to guess the country before the hangman is complete. Let's begin!")

welcome()