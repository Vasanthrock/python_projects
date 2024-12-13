
import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
display = []
lives = 6
word_len = len(chosen_word)
print(hangman_art.logo)
for i in range(word_len):
    display += "-"

flag = 0

while not flag :
    guess = input("Guess a Letter: ").lower()
    if guess in display:
        print(f"You have already guessed {guess}")
    for position in range(word_len):

        letter = chosen_word[position]
        if letter in guess :
            display[position] = guess

    if guess not in chosen_word:
         print("you guessed wrong letter")
         print(hangman_art.stages[lives])
         lives-=1


    if lives == 0:
        flag =1
        print("you lose")
    print(f"{' '.join(display)}")


    if "-" not in display:
        flag = 1
        print ("you win")
