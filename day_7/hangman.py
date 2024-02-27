import random
import os
import word_list
import hang_stages
import logo_hangman


# function to clear the terminal each guess
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


print(logo_hangman.logo)
chosen_word = random.choice(word_list.word_lists).lower()
lives = 6

# Create a display of empty list
display = []
for i in chosen_word:
    display.append("_")

end_of_game = False

while not end_of_game:
    clear_screen()
    guess = input("Guess a letter guys: ").lower()

    if guess in display:
        print(f"You've already guessed the {guess}, guess another letter!")
        continue

    # flag for letter found
    letter_found = False

    # check the index
    for index in range(len(chosen_word)):
        if chosen_word[index] == guess:
            display[index] = guess
            letter_found = True

    if not letter_found:
        lives -= 1
        print(f"You guessed {guess}, that's not in the words. You lose a life")

    # show the stage and display the char of words
    print(','.join(display))
    print(hang_stages.stages[lives])

    if lives == 0:
        end_of_game = True
        print("You are dead! You lose the game!")
        print(f"The answer is {chosen_word}")
    elif "_" not in display:
        end_of_game = True
        print("You win the game!")
