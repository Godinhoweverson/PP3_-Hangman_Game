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
|Confirm that the program updates the display with hangman stages.|Pass|
|Verify that the incorrect letters are displayed for the users to know which letter they've typed.|Pass|
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

The manual testing of the Hangman game revealed that the program successfully meets its intended functionality. It accurately handles user inputs, generates random words from selected continents, and effectively manages correct and incorrect guesses. The user interface was found to be clear and informative, providing appropriate feedback throughout the game. The play again functionality resets the game state as expected, and the program gracefully handles various edge cases. Overall, the testing process ensures a reliable and enjoyable gaming experience for users interacting with the Hangman game.

## Accessibility

After conducting a Lighthouse test, the accessibility score was initially at 94%, with identified issues related to insufficient contrast ratios between background and foreground colors. Addressing this concern through adjustments to the background-color has led to a significant improvement, achieving a perfect accessibility score of 100. Furthermore, these modifications have positively impacted performance, ultimately contributing to an overall enhanced user experience.

### Desktop
<img src="docs/accessibility/lighthouse-desktop-error.jpg" alt="accessibility-test">

<img src="docs/accessibility/lighthouse-desktop.png" alt="accessibility-test">

### Mobile

<img src="docs/accessibility/lighthouse-mobile-error.png" alt="accessibility-test">

<img src="docs/accessibility/lighthouse-mobile.jpeg" alt="accessibility-test">

## Validation 

#### Python

##### Pep8

In the process of validating the Python code using the PEP8 validator, several issues were identified:

- Line Length Exceeded (E501):

- Line 27: The line exceeded the recommended maximum length of 79 characters.
Continuation Line Under-Indented for Visual Indent (E128):

- Lines 28-31, 133, and 147: The continuation lines were under-indented for visual clarity.

To address these issues, I have broken down the long lines into smaller, more readable segments and ensured proper indentation for continuation lines. This not only enhances code readability but also aligns with PEP8 conventions. The updated code now adheres to the recommended standards, promoting a cleaner and more consistent coding style.

<img src="docs/validator/pep8-validator-errors.png" alt="pep8-validator">

<img src="docs/validator/pep8-validator.png" alt="pep8-validator">

#### HTML
HTML has been validated with [W3C HTML5 Validator](https://validator.w3.org/)

<img src="docs/validator/html-validator.png" alt="html-validator">

#### CSS
CSS has been validated with [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

<img src="docs/validator/css-validator.png" alt="css-validator">


## Bugs

#### play_again function
- In the play_again function, a bug was identified where, upon entering 'N' to close the game, the program would erroneously prompt the user twice. This issue has been successfully addressed in the updated code snippet below:

<strong>
if repeat_game == 'Y':<br>
    print("Let's start!\n")<br>
    main()<br>
    break<br>
elif repeat_game == 'N':<br>
    print("Thank you, see you next time!\n")<br>
    break
</strong>

The introduction of the break statement ensures the resolution of the problem, preventing the program from prompting the user multiple times when opting to close the game by typing 'N'. It is crucial to verify that this code snippet is embedded within an appropriate loop structure responsible for handling user input related to game repetition or closure.

#### Application Not Functioning Properly After Deployment
- After deploying the application, it was not functioning properly. Upon inspecting the logs, I identified the presence of ERROR H14. This error indicated that the Eco Dynos were not activated. To resolve this issue, I promptly activated the dynos, and the application resumed normal operation.

#### Unable to Create New Workspace Using CodeAnywhere
- Upon attempting to create a new workspace using CodeAnywhere, the process failed, and I was unable to establish the desired workspace. After encountering this issue, I opted to switch to Gitpod, where I successfully created the workspace without any further impediments.

<img src="docs/codeanywhere.jpeg" alt="bug-codeanywhere">

## Conclusion 
The comprehensive manual testing of the Hangman game has demonstrated the robustness and accuracy of its functionalities. The game effectively handles various scenarios, such as continent selection, word generation, letter input, correct and incorrect guesses, and game outcomes. The user interface provides clear feedback, contributing to a positive gaming experience.
The play again functionality successfully resets the game state as intended, allowing users to start a new game or exit gracefully. The program exhibits reliability in handling edge cases, ensuring that it accepts valid inputs, rejects invalid inputs, and provides appropriate messages in different situations.
The accessibility testing revealed an initial score of 94%, with identified contrast ratio issues. After addressing these concerns, the accessibility score improved to a perfect 100%. The adjustments not only enhanced accessibility but also positively impacted overall performance, contributing to an improved user experience on both desktop and mobile platforms.
In the validation phase, the Python code was reviewed and validated using the PEP8 validator. Identified issues related to line length and indentation were successfully addressed, aligning the code with recommended standards. The HTML and CSS were validated using W3C validators, ensuring compliance with respective standards.
Several bugs were identified and addressed during the testing phase. Notably, the play_again function was modified to prevent double prompting when closing the game. Additionally, the application's post-deployment issue was resolved by activating the Eco Dynos. The challenge in creating a workspace using CodeAnywhere was overcome by switching to Gitpod, where the workspace creation was successful.
In summary, the Hangman game has undergone thorough testing, validation, and bug resolution, resulting in a reliable and enjoyable gaming application.




