# Serge Martin
# Libraries needed
import random
import time
from utils.game import Hangman

def main ():
    pass
if __name__ == '__main__':
    main()

# Attributes
# words to guess
possible_words = ['becode', 'learning', 'mathematics', 'sessions']
word = random.choice(possible_words)
word_to_find = ['B', 'E', 'C', 'O', 'D', 'E']
well_guessed_letters =  list('_')*(word_to_find)
bad_guessed_letters = []
turn_count = 1
error_count = 0
lives = 5
guesses = ""


class Hangman:
    """" Attributes definiation :
    - possible_words
    - word_to_find
    - well_guessed_letters
    - bad_guessed_letters
    - turn_count
    - error_count
    - lives
    """"
    def __init__(self):
        """Construction of the Hangman class"""
        self.possible_words = possible_words
        self.word_to_find = word_to_find
        self.well_guessed_letters = well_guessed_letters
        self.bad_guessed_letters = bad_guessed_letters
        turn_count = 0
        self.error_count = 1
        self.lives = 5
        print(self.word_to_find)

    def start_game():
# the user is ask to enter his/her name
       name = input("Please enter your name")
       print("Good Luck", name)

# the player method that ask the player to enter a letter
    def play(self):
        """method that ask the player to enter a letter only
        """
        letter = input ("please enter a letter:")
        if len in letter == 1 and letter == possible_words:
            self.turn_count += 1
            for character in range(len(self.word_to_find)):
                if self.word_to_find[character]==letter:
                self.well_guessed_letter[character]==letter
            else:
                self.bad_guesses_letter = self.bad_guessed_letter + letter
                self.error_count += 1
                self.lives-=1
    else:
        print("Enter a correct letter ")
    return self.well_guessed_letter

    def game_over():
        pass
        print("game is over")

    def well_played():
        if self.guessed_letter == well_guessed_letters:
            print("you found the word")

    def start_game():
        pass


    
    


  

    

    