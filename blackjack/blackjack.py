# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 19:17:02 2022

@author: Zikou
"""


# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 15:32:07 2022

@author: Zikou
"""



from random import shuffle
from colorama import Fore, Back, Style
import time

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}


class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    def __repr__(self):
        return f"Card('{self.suit}','{self.rank}')"
    
    def show(self):
        print(f"{self.rank} of {self.suit}")

class Deck:
    #create deck of cards num of card in the deck is equal 52
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    #this will show for example 5 of Spades
    def show(self):
        for card in self.deck:
            card.show()


    def shuffle(self):
       shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces +=1
    # if there is an ace in the hand of player we need to adjust it = 1 if we exceed 21 else 11
    def adjust_aces(self):
        while self.value > 21 and self.aces:
            self.value -=10
            self.aces -=1

class Chips:
    def __init__(self):
        self.total = self.buy()
        self.bet = 0
    @staticmethod
    def buy():
        valid_value= False
        while not valid_value:
            try:
                amount = int(input("How many chips you want to buy: "))
                valid_value = True
            except ValueError:
                print("Invalid value")
        return amount
            
    
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet
    
       
    def take_bet(self):
        valid_value= False
        while not valid_value:
            try:
                self.bet=int(input("Please give you bet: "))
            except ValueError:
                print("Please provide a valid value")
            else:
                if self.bet > self.total:
                    print("You dont have enough chips to bets")
                else:
                    valid_value= True




class Table:
    # in this class we gonna defined the method when player bust or win
    @staticmethod
    def rules():
        print("Welcome to Blackjack")
        print("If the player exceed 21 then the player bust (lose)\nIf the dealer doesnt bust the person who has the bigger number but dont exceed 21 win the bet\n ")
     
    @staticmethod
    def hit(deck,hand):
        hand.add_card(deck.deal())
        hand.adjust_aces()
    
    @staticmethod
    def show_some(player,dealer):
        print("Dealer's Hand")
        time.sleep(0.4)
        print("<< Hidden card >>")
        time.sleep(0.4)
        print(dealer.cards[1])
        print("\nPlayer's hand")
        for card in player.cards:
            print(card)
            time.sleep(0.4)
        print(f"Total value of card is:{player.value}\n ")
    
    @staticmethod
    def show_all(player,dealer):
        print("Dealer's Hand")
        for card in dealer.cards:
            print(card)
            time.sleep(0.3)
        print(f"Total value of card is:{dealer.value}")
        print("\nPlayer's hand")
        for card in player.cards:
            print(card)
            time.sleep(0.3)
        print(f"Total value of card is:{player.value}\n ")

    
    
    def player_wins(self,chips):
        print("Player wins")
        chips.win_bet()
    
    def player_bust(self,chips):
        print("Player bust!!")
        chips.lose_bet()
    
    def dealer_wins(self,chips):
        print("Dealer wins")
        chips.lose_bet()
    
    def dealer_bust(self,chips):
        print("Dealer bust")
        chips.win_bet()
    
    @staticmethod
    def push():
        print("Dealer and Player tie! It's a push.")

       
    def play_again(self):
        while True:
            user_input = input("Do you want to play again y/n: ").lower()
            if user_input =="y":
                return True
            elif user_input == "n":
                return False
            else:
                print("please enter either 'y' or 'n'")
                
        
    @staticmethod
    def buy_chips():
        while True:
            user_input = input("Do you want to buy new chips to bet y/n: ").lower()
            if user_input =="y":
                return True
            elif user_input =='n':
                return False
            else:
                print("please enter either 'y' or 'n'")
   


     
def play_blackjack():
    #instantiate all the instance of classes
    
    chips = Chips()
    game_on = True
    while game_on:
        table=Table()
        player = Hand()
        dealer = Hand()
        #making deck of cards and shuffle it
        new_deck = Deck()
        new_deck.shuffle()
        
        #adding card to the hand of player
        for i in range(2):
            player.add_card(new_deck.deal())
            dealer.add_card(new_deck.deal())
        #asking the bet of the player
        chips.take_bet()
        #show some of the card of dealer and the full card of player
        table.show_some(player,dealer)
        #we ask the player if he want to hit or stand
        asking = True
        while asking:
            user_input = input("Enter 'h' to Hit or 's' to stand: ").lower()
            if user_input == "h":
                table.hit(new_deck,player)
                table.show_some(player,dealer)
            elif user_input =='s':
                asking = False
            else:
                print("please provide a valid input")
                continue
            
            # if the player bust we exsit the loop
            if player.value > 21:
                table.player_bust(chips)
                break
        
        if player.value <=21:
            while dealer.value < 17:
                table.hit(new_deck,dealer)
            
            #show all cards
            print("\n")
            table.show_all(player,dealer)
            if dealer.value > 21:
                table.dealer_bust(chips)
            elif dealer.value > player.value:
                table.dealer_wins(chips)
            elif dealer.value < player.value:
                table.player_wins(chips)
            else:
                table.push()
        
        # Inform Player of their chips total 
        print("\nYour total chips is: ",chips.total)
        
        if table.play_again():
            if chips.total <=0:
                print(Fore.RED,"You dont have enough chips to bet, you should buy some!!")
                print(Style.RESET_ALL)
                if table.buy_chips():
                    play_blackjack()
                else:
                    print(f"Thank you for playing you have {chips.total} in your pocket now")
                    break
            else:
                continue
        else:
            print(f"Thank you for playing you have {chips.total} chips in your pocket now")
            break
        

        
if __name__ == "__main__":
    print("Welcome to Blackjack")
    print("If the player exceed 21 then the player bust (lose)\nIf the dealer doesnt bust the person who has the bigger number but dont exceed 21 win the bet\n ")
    play_blackjack()


    
        
            
    
    
    