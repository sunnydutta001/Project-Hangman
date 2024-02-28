import random
from stages import stages
from logo import logo
from words import word_list

chosen_word = random.choice(word_list)
print(f"psst! the word is {chosen_word}")
lives = 6

display = []
for _ in chosen_word:
    display += "_"

should_continue = True
print(logo)
print(f"You have {lives} lives. ")
while should_continue:
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
        print(f"You have already guessed {guess}")
    
    #Check guessed letter
    for index in range(len(chosen_word)):
        letter = chosen_word[index]
        if letter == guess:
            display[index] = letter
    
    #Check if the user is correct
    if guess not in chosen_word:
        print(f"You have guessed {guess}, that's not in the word. You lose a life!")
        lives = lives - 1
        print(f"You have {lives} lives remaining!")
        if lives == 0:
            should_continue = False
            print('You lose')
    
    
    if "_" not in display:
            should_continue = False
            print("You won!")
    
    
    
    
    
    print(f"{' '.join(display)}")
    print(stages[lives])
    
