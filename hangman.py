import random
from words import wordlist

def get_Word():
    word = random.choice(wordlist)
    return word.upper()

def play(word):
    word_completion = "_"*len(word)
    guessed = False
    guessed_letter = []
    guessed_word = []
    tries = 6
    print("Let's Play Hangman !!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries>0:
        guess = input("Please Guess A Letter Or Word :) ").upper()

        if len(guess)==1 and guess.isalpha():
            if guess in guessed_letter:
                print("You Already guessed the letter ",guess)
            elif guess not in word:
                print(guess," is not in the word :(")
                tries-=1
                guessed_letter.append(guess)
            else:
                print("Well Done, "+guess+" is in the word :)")
                guessed_letter.append(guess)
                word_as_list=list(word_completion)

                indices=[i for i, letter in enumerate(word) if letter==guess]
            
                for index in indices:
                    word_as_list[index]=guess
            
                word_completion="".join(word_as_list)
                if "_" not in word_completion:
                    guessed=True

        elif len(guess)==len(word) and guess.isalpha():
            if guess in guessed_word:
                print("You Already guessed the letter ",guess)
            elif guess!=word:
                print(guess," is not a word")
                tries-=1
                guessed_word.append(guess)
            else:
                guessed=True
                word_completion=word

        else:
            print("NOT A VALID GUESS :( ")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        print("You Won the game !")
        print("You guessed the word !")
    else:
        print("Sorry !! You ran out of the tries.")
        print("The word was "+word+".")


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    word=get_Word()
    play(word)
    while input("Wanna Play Again? (Yes / No) ").upper()=="YES":
        word=get_word()
        play(word)

if __name__=="__main__":
    main()
    