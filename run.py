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

def single_letter(letter):
"This function enables the player to type only one letter at a time. If the player attempts to type two or more letters, they will not be able to proceed until they have typed a single letter. This function can be called within the check_letter()
      while True:
        try:
            letter = input('Please enter a letter: ').upper()
            if len(letter) == 1:
                break 
            else:
               
                print('Please enter one letter at a time. Try again!\n\n')     
        except ValueError:
            print('type one letter.\n\n')
    
    
      return letter

def check_letter(word):
    correct_letter = 0  # Counter for the number of correctly guessed letters
    wrong_letter = 0  # Counter for the number of incorrectly guessed letters
    correct = ''  # String to store correctly guessed letters
    wrong = ''  # String to store incorrectly guessed letters

    while correct_letter != len(word) and wrong_letter != 6:  # Continue until all letters are guessed correctly or 6 wrong guesses are made
        display = ''
        for letter in word:
            if letter in correct:
                display += f'{letter}'  # Display correctly guessed letters
            else:
                display += '_ '  # Display underscores for unguessed letters
        print(display)
       
        letter = single_letter(letter)
        if letter in word:
            print('You got the letter right!')  # The guessed letter is in the word
            correct += letter  # Add the correctly guessed letter to the 'correct' string
            print(correct)  # Display the correctly guessed letters
            correct_letter += 1  # Increment the count of correct guesses
        else:
            print('You got the letter wrong!')  # The guessed letter is not in the word
            wrong += letter  # Add the incorrectly guessed letter to the 'wrong' string
            wrong_letter += 1  # Increment the count of wrong guesses

check_letter(word)  # To call the function, the parameter "word" is used. The word is a randomly selected country defined by the generate_word function.


                  

            

def win_game():
    pass

def lost_game():
    pass
