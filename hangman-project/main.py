import os
import random
import hangman_art
import hangman_words

print(hangman_art.logo)
number_of_lives=6
#taking random word from the file contaning lists of words
chosen_word = random.choice(hangman_words.word_list)
#print(f"The chosen word is {chosen_word}")

#printing number of line of the random choose word
#if play is a word, then it will print _ _ _ _
display=[]
for i in chosen_word:
    display+="_"
print(' '.join(display))

#to run the while loop
end_of_game=False
while not end_of_game:
    #Taking a user input and convert to small letter
    guess = input("Guess a letter:").lower()
    #clear the screen for better display
    os.system('cls||clear')
    
    if guess in display:
        print(f"You already guess the letter {guess}.")
    
    #to loop to the number of words present in the chosen word (Suppose camel)
    for position in range(len(chosen_word)): #1
        letter = chosen_word[position]       # letter = chosen_word[1]
        if guess==letter:                    # guess (input) = c
            display[position]=letter         # display[1] = c _ _ _ _
    

    if guess not in chosen_word:
        number_of_lives-=1
        print(f"You guess letter {guess}, that's not the word. You lose a life.")
    
    #to print the display as words with the spaces (c _ _ _ _)
    print(' '.join(display))
    print(hangman_art.stages[number_of_lives])

    if "_" not in display:
        end_of_game=True
        print("You win")
        
    if number_of_lives==0:
        end_of_game=True
        print("You lose")
        print(f"The word is {chosen_word}")


