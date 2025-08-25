import random
import hangman_stages
List = ['furiously', 'intelligence', 'technology', 'information', 'strawberry']
# List = ['apple', 'banana', 'cherry', 'date', 'strawberry']
lives = 8
choosen_word = random.choice(List)
print(choosen_word)


display = []
# for displaying dashes "_"
for i in range(len(choosen_word)):
    display += "_"
print(display)


game_over = False
while not game_over:
    guessed_letter = (input('Guess a letter: ')).lower()
    
    for position in range(len(choosen_word)):
        letter = choosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter
    print(display)        

    if guessed_letter not in choosen_word:
        lives -= 1
        print(f"You guessed {guessed_letter}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print("You lose!!")
    if "_" not in display:
            game_over = True
            print("You win!!")
    print(f"You have {lives} lives left.")
    print(hangman_stages.stages[lives])


        
