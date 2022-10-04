from collections import Counter
import sys
from termcolor import colored, cprint
from colorama import Fore, Back, Style
from colored import fg, bg, attr
import time
from random import choice


class Player():  
    @staticmethod
    def read_content(value):
        with open('words.txt','r') as f:
            contents=f.read()
            if value.lower() in contents:
                return True
            else:
                return False
    
    
    def check_word(self):
        valid_word=False
        while not valid_word:
            val=input()
            if len(val)>5:
                print("You have given a word that exceeds 5 letters")
                continue
            elif len(val)<5:
                print("You have given a word less than 5 letters")
                continue
            elif len(val)==5 and not self.read_content(val):
                print("you give a word with 5 letter that doesn't exist in dictionnary")
                continue
            elif len(val)==5 and self.read_content(val):
                return val
                valid_word=True


class Wordle():
    def __init__(self):
        self.word=self.today_word()
        
    @staticmethod
    def today_word():
        with open('words.txt','r') as f:
            contents=[line.rstrip() for line in f]
            return choice(contents)
    @staticmethod
    def game_rules():
        print("\tYou have six attempts to guess today word\n")
        print(f"when the color is {colored('GREEN','green',attrs=['bold'])} that means the letter in the right postion\n"
          +f"when the color is {colored('YELLOW','yellow',attrs=['bold'])} that means the letter is in the wrong position\n"
          +f"when the color is {colored('GREY','grey',attrs=['bold'])} that means the letter doesn't exist in the word")
        print("please print the word that's in your mind")
        
    #this a method to get red of duplicate letter in our guess if the letter is not duplicated in today's word
    @staticmethod
    def compare(guess, target):
        length = len(target)
        output = ["-" for i in range(length)]      
        for index in range(len(target)):
            if guess[index] == target[index]:
                output[index] = "X"
                target = target.replace(guess[index], "-", 1)
        
        for index in range(len(target)):
            if guess[index] in target and output[index] == "-":
                output[index] = "O"
                target = target.replace(guess[index], "-", 1)
        return output
    
    def color_word(self,guess):
        output=self.compare(guess,self.word)
        for index,letter in enumerate(guess):
            if output[index]=='X':
                print(colored(letter.upper(),'red','on_green',attrs=['bold']),end='')
                print('  ',end='')
            elif output[index]=='O':
                print(colored(letter.upper(),'red','on_yellow',attrs=['bold']),end='')
                print('  ',end='')
            else:
                print(colored(letter.upper(),'red','on_grey',attrs=['bold']),end='')
                print('  ',end='')
            time.sleep(0.5)




def play_wordle(game,player):
    game.game_rules()
    todays_word=game.word
    attempt=1
    while attempt<=6:
        player_word=player.check_word()
        game.compare(player_word,todays_word)
        game.color_word(player_word)
        if player_word != todays_word:
            attempt=attempt+1
        elif player_word == todays_word:
            print(f"\nAttempt:{attempt}/6")
            print(f"Congratulation you've guessed the word of today:{game.word} ")
            break
    if player_word != todays_word:
        print(f"\nSorry you lost today's word is :{todays_word.upper()}")


if __name__ == '__main__':
    game=Wordle()
    player=Player()
    play_wordle(game,player)
    
        
    




