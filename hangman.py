import random

import imghangman


word_list = ["baboon", "rainbow", "icebarg"]

chosen_word = random.choice(word_list)

display= []
word_length = len(chosen_word)

lives = 6

for _ in range (word_length):
        display += "_"

end_of_game = False
while not end_of_game:
    guess = input("Guess the letter:  ").lower()
     

    if guess in display:
         print(f"You have already guessed {guess}")

   #Check guessed letter   
    for position in range (word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
         print(f"You guessed {guess} not in the word. You lose a life.")

         lives -= 1
         if lives == 0:
              end_of_game = True
              print("You lose")


    print(display)

    print(f"{''.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(imghangman.stages[lives]) 

