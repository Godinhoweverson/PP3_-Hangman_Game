# Testing

## Manual Test

The testing phase for the Hangman game focused on ensuring the correctness and robustness of various functionalities. The objective was to thoroughly assess the program's behavior in response to user inputs, ensuring that it gracefully handles different scenarios and provides a positive gaming experience. The tests covered aspects such as continent selection, word generation, letter input, correct and incorrect letter guesses, game outcomes, play again functionality, general flow, and edge cases.

###  Test the continent selection

| Test |Result  |
|--|--|
|Run the program and choose each continent option (American, Asian, European).| Pass |
|Verify that the program accepts valid inputs (1, 2, 3) and rejects invalid inputs.| Pass|
|Confirm that the program loops until a valid input is provided.|Pass|

### Test word generation

| Test |Result  |
|--|--|
|After selecting a continent, check if the program generates a random country from the chosen continent.|Pass|
|Manually verify that the selected country is indeed from the correct continent.|Pass|
|Manually verify that the number of dashes matches how many letters are in the word.|Pass|

### Test letter input

| Test |Result  |
|--|--|
|Enter valid and invalid letters during the game.|Pass|
|Verify that the program only accepts a single letter at a time.|Pass|
|Check if the program rejects inputs of more than one letter.|Pass|
|Ensure that the program does not accept non-alphabetic characters.|Pass|

### Test correct letter guesses

| Test |Result  |
|--|--|
|Guess correct letters in the word.|Pass|
|Confirm that the program updates the display with the correctly guessed letters.|Pass|
|Verify that the correct letters are added to the 'correct' string.|Pass|
|Ensure that the program counts the correct guesses correctly.|Pass|

### Test incorrect letter guesses

| Test |Result  |
|--|--|
|Guess incorrect letters in the word.|Pass|
|Confirm that the program updates the display with underscores and hangman stages.|Pass|
|Verify that the incorrect letters are added to the 'wrong' string.|Pass|
|Ensure that the program counts the incorrect guesses correctly.|Pass|

### Test game outcomes
| Test |Result  |
|--|--|
|Play the game until you win, guessing all the words.|Pass|
|Verify that the program congratulates you and prompts if you want to play again.|Pass|
|Play the game until you lose, completing the body.|Pass|
|Verify that the program informs you of the correct country and asks if you want to play again.|Pass|

### Test play again functionality

| Test |Result  |
|--|--|
|Choose to play again after winning or losing.|Pass|
|Confirm that the program resets and starts a new game.|Pass|
|Choose not to play again after winning or losing.|Pass|
|Confirm that the program exits with a farewell message.|Pass|

### General Testing

| Test |Result  |
|--|--|
|Test the overall flow of the program by going through multiple rounds with different continents.|Pass|
|Confirm that the program handles user input gracefully and provides appropriate messages.|Pass|

### Edge Cases

| Test |Result  |
|--|--|
|Try entering non-numeric values when selecting a continent.|Pass|
|Attempt to guess the same letter multiple times.|Pass|
|Try guessing all letters to win the game.|Pass|
|Try guessing incorrect letters until you lose.|Pass|


## Conclusion

The manual testing of the Hangman game revealed that the program successfully meets its intended functionality. It accurately handles user inputs, generates random words from selected continents, and effectively manages correct and incorrect guesses. The user interface was found to be clear and informative, providing appropriate feedback throughout the game. The play again functionality resets the game state as expected, and the program gracefully handles various edge cases. Overall, the testing process ensures a reliable and enjoyable gaming experience for users interacting with the Hangman program.

## Accessibility

<img src="docs/accessibility/lighthouse-desktop.jpg" alt="accessibility-test">