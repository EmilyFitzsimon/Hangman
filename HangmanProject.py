import random
import WordArt

chosen_word = random.choice(WordArt.word_list)
lives = 6
display = []
word_length = len(chosen_word)
complete_word = list(chosen_word)
end_of_game = False

#Testing code
# print(f"The word is {chosen_word}")

print("Hangman")
print(WordArt.stages[6])


for char in range(word_length):
    display += "_"
print(display)

while not end_of_game:
    input_guess = input("Guess a letter\n")
    guess = input_guess.lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        char = chosen_word[position]
        # print(f"Current position: {position} \n Current letter: {char}\n Guessed letter: {guess}")
        if char == guess:
            display[position] = char

    if guess not in chosen_word:
        lives -= 1
        print("This letter is not in the word.")
        print(f"You have {lives} lives remaining")
        print(WordArt.stages[lives])
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win.")
    if lives == 0:
        end_of_game = True
        print(f"The word was {chosen_word}. You have lost all your lives, try again.")
