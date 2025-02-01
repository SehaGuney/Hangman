import random

#Saves the current state of the Hangman game into a file named "hangman_save.txt".
def save_game(word, correct_guesses, revealed_letters, used_letters, mistakes, attempts, score):
    # Open the file in 'w' (write) mode
    with open("hangman_save.txt", "w") as file:
        # Add a header to the file
        file.write("Hangman Save Data\n")
        # Add the word information to the file
        file.write("Word: " + word + "\n")       
        # Add the current correct guesses to the file
        file.write("Current Guess: " + " ".join(correct_guesses) + "\n")       
        # Add the revealed letters to the file
        file.write("Revealed Letters: " + "-".join(map(str, revealed_letters)) + "\n")
        # Add the used letters to the file
        file.write("Used Letters: " + "-".join(used_letters) + "\n") 
        # Add the number of mistakes to the file
        file.write("Mistakes: " + str(mistakes) + "\n") 
        # Add the total number of attempts to the file
        file.write("Attempts: " + str(attempts) + "\n") 
        # Add the player's score to the file
        file.write("Score: " + str(score) + "\n")

def load_game():
    try:
        # Attempt to open the "hangman_save.txt" file for reading
        with open("hangman_save.txt", "r") as file:
            # Read all lines from the file
            lines = file.readlines()
            # Extracting data from the lines and converting them to appropriate types
            word = lines[0].strip()  # The word to be guessed
            correct_guesses = lines[1].strip().split()  # List of correct guesses (initially underscores)
            revealed_letters = set(map(int, lines[2].strip().split()))  # Set of revealed letter indices
            used_letters = set(lines[3].strip().split())  # Set of used letters
            mistakes = int(lines[4].strip())  # Number of mistakes made
            attempts = int(lines[5].strip())  # Number of attempts made
            score = int(lines[6].strip())  # Current score
        # Return the extracted data as a tuple
        return word, correct_guesses, revealed_letters, used_letters, mistakes, attempts, score
    except FileNotFoundError:
        # If the file is not found, return None
        return None
    
#ASCII art representation of Hangman
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / ` | ' \ / ` | ' ` _ \ / ` | ' \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)

#user selects difficulty level
difficulty = int(input("""SELECT DIFFICULTY 1-3 
Press 1 (easy) score = 70, 
Press 2(medium) score = 85, 
Press 3(hard) score = 100: """))

# Lists of words for each difficulty level
easy = ["Canada", "Italy", "Brazil", "France", "Japan", "India", "Australia", "Mexico", "Germany",
        "Java", "Python", "JavaScript", "Developer", "Tomato", "Potato", "Apple", "Strawberry", "Aubergine",
        "Fork", "Toothbrush", "Clock", "Chair", "Carpet", "Television","Library"]

medium = ["Kazakhstan", "Azerbaijan", "Kyrgyzstan", "Bhutan", "Uzbekistan", "Senegal", "Tajikistan", "Luxembourg",
          "BackEnd", "FrontEnd", "Assembly", "Network", "Sunflower", "Cactus", "Rose", "Daisy", "Lavender",
          "Refrigerator", "Computer", "Backpack", "Umbrella", "Headphones","Rainbow","Mystery","Explore"]

hard = ["Eswatini", "Comoros", "Djibouti", "Boulevard", "Tuvalu", "Zimbabwe", "Azalea", "Geranium", "Fuchsia", "Acquaintance","Inquisitive","Ephemeral"]

#Function to choose a random word based on difficulty level
def choose_word():
    if difficulty == 1:
        return random.choice(easy).upper()
    elif difficulty == 2:
        return random.choice(medium).upper()
    elif difficulty == 3:
        return random.choice(hard).upper()
    else:
        print("This number is not between 1-3")
        return 0
    
#function that determines the initial score according to the difficulty level
def total_score(difficulty):
    if difficulty == 1:
        score = 70
    elif difficulty == 2:
        score = 85
    elif difficulty == 3:
        score = 100
    else:
        score = 0
    print("\n<YOUR STARTING SCORE IS %d>" % score)
    return score

#Function to display the current state of the word
def display_word(word, correct_guesses,revealed_letters):
    print("\nCurrent word:", end=" ")
    for i, letter in enumerate(correct_guesses):
        #If the letter has already been guessed correctly, print the letter in the corresponding position of the word.
        if i in revealed_letters:
            print(word[i], end=" ")
        # If the letter has not yet been guessed, print the character '_' on the screen.
        else:
            print(letter, end=" ")
    print()

# Function to display Hangman ASCII art based on mistakes
def hangman_pictures(mistakes):
    stages = [
      """
        ----------
        |        |
        |
        |
        |
        |
        -
        """
        ,
        """
        ------
        |    |
        |    O   
        |       
        |
        |
        -
        """
        ,
        """
        ------
        |    |
        |    O
        |    |
        |
        |
        -
        """
        ,
        """
        ------
        |    |
        |    O
        |   /|
        |
        |
        -
        """
        ,
        """
        ------
        |    |
        |    O
        |   /|\\
        |
        |
        -
        """
        ,
        """
        ------
        |    |
        |    O
        |   /|\\
        |   /
        |
        -
        """
        ,
        """
        ------
        |    |
        |    O
        |   /|\\
        |   / \\
        |
        -
        """
  ]
    print(stages[mistakes])


#main game function
def hangman_game():
    word = choose_word()
    length = len(word)
    correct_guesses = ['_' for _ in word]
    used_letters = set()
    mistakes = 0
    found = False
    tries = 6
    attempts = 0
    score = total_score(difficulty)
    revealed_letters=set()



    #The while loop continues as long as the right to try is greater than zero and the condition is true.
    while tries > 0 and not found:
        display_word(word, correct_guesses,revealed_letters)
        print("Used letters:", used_letters)
        print("YOU ARE ALLOWED %d MISTAKES" % tries)
        print("Your current score is:", score)
        print("HINT:If you want a letter, press '?' (each press reduces the score by 15 )")

        print("\n///////////////////////////////////////////")
        guess = input("\nTRY TO GUESS A LETTER OR THE WORD: ").upper()

        #The score decreases by five for each attempt.
        score -= 5

        #The user gets a letter for each press of the question mark, but the total score is reduced by 15.
        if guess == "?":
            score-=10
            #Find the indices of unrevealed letters (positions with '_').
            unrevealed_letters = [i for i, letter in enumerate(correct_guesses) if letter == '_']
            #If there are unrevealed letters, randomly choose one to reveal.
            if unrevealed_letters:
                # If there are still unrevealed letters:
                # Choose a random unrevealed letter
                revealed_letter_index = random.choice(unrevealed_letters)
                # Add the chosen letter to the set of revealed letters
                revealed_letters.add(revealed_letter_index)
                # Update the game state and display the revealed letter
                display_word(word, correct_guesses, revealed_letters)
                # Continue to the next iteration of the loop
                continue
            else:
                #If there are no unrevealed letters, inform the player.
                print("There are no unrevealed letters.")
                continue
    
        if len(guess) == 1:
            #It works if the length of the guess is one and the letter has been used before.
            if guess in used_letters:
                mistakes +=1
                tries-=1
                print("\nYOU HAVE USED THIS LETTER")
                attempts += 1

            #It works if the length of the guess is one and the guess is a number.
            elif guess.isdigit():
                mistakes += 1
                tries-=1
                print("\nNUMBERS ARE NOT ALLOWED")
                attempts += 1

            #It works if the length of the guess is one and the guess is not inside the word.
            elif guess not in word and type(guess) != int:
                mistakes += 1
                tries-=1
                print("\n%s IS NOT IN THE ANSWER" % guess)
                used_letters.add(guess)
                attempts += 1

            # Loop through each index (i) and letter in the randomly chosen word    
            else:
                for i, letter in enumerate(word):
                    if letter == guess:
                        correct_guesses[i] = guess
                        used_letters.add(guess)
                        attempts += 1

                #If there is no other '_' in correct_guesses, the word is completely predicted.
                if '_' not in correct_guesses:
                    found = True
                    print(word)
                    print("\nCONGRATULATIONS, YOU FOUND THE WORD 🎉, IN %d TRIES. YOUR SCORE IS %d\n" % (attempts, score))

        #If the length of the guess is equal to the length of the word and the guess is the word, the guess is correct.
        elif len(guess) == len(word) and guess == word:
            found = True
            print(word)
            print("\nCONGRATULATIONS, YOU FOUND THE WORD 🎉, IN %d TRIES. YOUR SCORE IS %d\n" % (attempts, score))

        #If the length of the guess is equal to the length of the word but the guess is not the word, the guess is not correct.
        elif len(guess) == len(word) and guess != word:
            print("\n%s IS NOT THE CORRECT WORD" % guess)
            mistakes += 1
            tries-=1
            attempts += 1

        #If the user's input does not meet the valid conditions, prompt them to enter a valid character, a single letter, or a word of length %d.
        else:
            print("\nENTER VALID CHARACTER OR 1 LETTER OR %d LETTER WORD" % length)

        #Display the Hangman pictures based on the number of mistakes
        hangman_pictures(mistakes)
        #Update the remaining tries based on the number of mistakes

    if not found:
        #If the word is not found within the allowed number of attempts, display a message indicating that the player has run out of attempts.
        print("\nSorry, you ran out of attempts. The correct word was:", word)
        # Display the game over message with ASCII art
        


    save_game(word, correct_guesses, revealed_letters, used_letters, mistakes, attempts, score)
    return score

#unction asking whether to continue the game
def continue_game():
    while True:
        # Get the player's decision (input)
        decision = input("Do you want to continue? ('y' for Yes / 'n' for No):").lower()
        # Check the decision and return the corresponding boolean value
        if decision == 'y':
            return True
        elif decision == 'n':
            return False
        # If the input is invalid, prompt the player to enter 'y' or 'n'
        else:
            print("Invalid login. Please enter 'y' or 'n'.")

total=0

while True:
    score=hangman_game()
    total=total+score #calculates total points

    print(f"Total score: {total}")
    # Ask the player if they want to continue

    if not continue_game():
            game_over =("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣶⣶⠀⠀⠀⠀⣠⣾⣿⣿⡇⠀⣿⣿⣿⣿⠿⠛⠉⠉⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⠀⠀⠀⠀⠀⢀⣿⣿⣶⡀⠀⠀⠀⠀⠀⣾⣿⣿⣿⡄⠀⢀⣴⣿⣿⣿⣿⠁⢸⣿⣿⣿⣀⣤⡀⠀⠀⠀
                ⠀⠀⠀⠀⠀⣠⣴⣶⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⣼⣿⣿⣿⣧⠀⠀⠀⠀⢰⣿⣿⣿⣿⣇⣠⣿⣿⣿⣿⣿⡏⢠⣿⣿⣿⣿⣿⡿⠗⠂⠀⠀
                ⠀⠀⠀⣰⣾⣿⣿⠟⠛⠉⠉⠉⠉⠋⠀⠀⠀⣰⣿⣿⣿⣿⣿⣇⣠⣤⣤⣿⣿⣿⢿⣿⣿⣿⣿⢿⣿⣿⡿⠀⣼⣿⣿⡟⠉⠁⢀⣀⡄⠀⠀
                ⠀⢀⣾⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣴⣿⣿⣿⣿⡿⣿⣿⣿⡏⠈⢿⣿⣿⠏⣾⣿⣿⠃⢠⣿⣿⣿⣶⣶⣿⣿⣿⡷⠦⠀
                ⢠⣾⣿⡿⠀⠀⠀⣀⣠⣴⣶⣿⣿⡷⠀⣠⣿⣿⣿⣿⡿⠟⣿⣿⣿⣠⣿⣿⣿⠀⠀⠀⠀⠁⢸⣿⣿⡏⠀⣼⣿⣿⣿⠿⠛⠛⠉⠀⠀⠀⠀
                ⢸⣿⣿⠣⣴⣾⣿⣿⣿⣿⣿⣿⡿⠃⣰⣿⣿⣿⠋⠁⠀⠀⠸⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠸⠿⠿⠀⠀⠛⠛⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠸⣿⣿⣆⣉⣻⣭⣿⣿⣿⡿⠋⠀⠀⢿⣿⡿⠁⠀⠀⠀⠀⠀⠹⠟⠛⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠙⠿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣶⣶⣶⣶⣦⣄⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣷⠄⣤⣤⣤⣤⣶⣾⣷⣴⣿⣿⣿⣿⠿⠿⠛⣻⣿⣿⣷⡄
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣄⠀⣶⣶⣤⡀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠋⢠⣿⣿⣿⠿⠛⠋⠉⠛⣿⣿⣿⠏⢀⣤⣾⣿⣿⡿⠋⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⠓⢹⣿⣿⣷⠀⠀⠀⠀⢀⣶⣿⡿⠁⠀⣾⣿⣿⣟⣠⣤⠀⠀⢸⣿⣿⣿⣾⣿⣿⣿⡟⠋⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⡿⠛⠉⠸⣿⣦⡈⣿⣿⣿⡇⠀⠀⣰⣿⣿⡿⠁⠀⢸⣿⣿⣿⣿⣿⠿⠷⢀⣿⣿⣿⣿⡿⠛⣿⣿⣿⡀⠀⠀⠀
                ⠀⠀⠀⠀⢀⣼⣿⣿⡿⠋⠀⠀⠀⠀⣿⣿⣧⠘⣿⣿⣿⡀⣼⣿⣿⡟⠀⠀⢀⣿⣿⣿⠋⠁⠀⣀⣀⣼⣿⣿⡟⠁⠀⠀⠘⣿⣿⣧⠀⠀⠀
                ⠀⠀⠀⠀⣼⣿⣿⡟⠀⠀⠀⠀⠀⣠⣿⣿⣿⠀⢹⣿⣿⣿⣿⣿⡟⠀⠀⠀⣼⣿⣿⣷⣶⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠸⣿⣿⡆⠀⠀
                ⠀⠀⠀⠀⢹⣿⣿⣇⠀⠀⢀⣠⣴⣿⣿⣿⡿⠀⠈⣿⣿⣿⣿⡟⠀⠀⠀⢰⣿⣿⣿⠿⠟⠛⠉⠁⠸⢿⡟⠀⠀⠀⠀⠀⠀⠀⠘⠋⠁⠀⠀
                ⠀⠀⠀⠀⠈⢻⣿⣿⣿⣾⣿⣿⣿⣿⣿⠟⠁⠀⠀⠸⣿⣿⡿⠁⠀⠀⠀⠈⠙⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠉⠛⠿⠿⠿⠿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
            print(game_over)
            break
    
    else:
        # Get the difficulty level from the user
     difficulty = int(input("""SELECT DIFFICULTY 1-3 
Press 1 (easy) score = 70, 
Press 2 (medium) score = 85, 
Press 3 (hard) score = 100: """))