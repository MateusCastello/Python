import hangman_words, hangman_art, random

#Choosing the word and filling the awnser with _
chosen_word = random.choice(hangman_words.word_list)
display_word = []
for i in range(len(chosen_word)):
    display_word += "_"

letters_track = []
lives = 6
has_won = False

print("Welcome to the Hangman game!")
print(hangman_art.logo)
print(hangman_art.stages[lives])
print(display_word)

while lives > 0 and has_won == False:
    guess = input("Guess a letter: ").lower()    
    index = 0

    if guess in letters_track:
        print(f"You have already guessed the letter {guess}")
        print("Letters guessed to the moment", letters_track)
        continue

    if guess not in chosen_word:
        lives -= 1
        print(hangman_art.stages[lives]) 
        print(display_word)
        letters_track.append(guess)       
        print("The letter is not in the word!")
        continue

    for letter in chosen_word:
        if letter == guess:
            display_word[index] = letter
        index += 1

    print(hangman_art.stages[lives])
    print(display_word)
    letters_track.append(guess)

    if "_" not in display_word:
        has_won = True
        print("You won!! Congrats")    
    
if lives == 0:
        print(f"The word was {chosen_word}")
        print("You lose!")
