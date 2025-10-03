import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': [1, 11]}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + 'of ' + self.suit

class Deck:
    def __init__(self):
        self.avail_cards = []
        for suit in suits:
            for rank in ranks:
                self.avail_cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.avail_cards)

    def deal_card(self):
        return self.avail_cards.pop()

class Player:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.hand = []
        self.handTotal = 0

    def add_card(self, new_card):
        self.hand.append(new_card)
        print(new_card)
        if new_card.rank == 'Ace':
            while True:
                card_value = input("You got an ace do you want it's value to be 1 or 11")
                if card_value not '1' or card_value not '11':
                    print("Sorry you didn't input a proper value try again.")
                    continue
                elif card_value = '1':
                    self.handTotal += new_card.value[0]
                    break
                else:
                    self.handTotal += new_card.value[1]
                    break   
        else:
            self.handTotal += new_card.value
        print(f"Your score total is {self.handTotal}")

    def __str__(self):
        for card in self.hand:
            print(card)

class Dealer:
    def __init__(self):
        self.hand = []
        self.secHand = []
        self.handTotal = 0

    def add_card(self, new_card):
        self.hand.append(new_card)
        print(new_card)
        if new_card.rank == 'Ace':
            if self.handTotal <= 10:
                self.handTotal += 11
            else:
                self.handTotal += 1   
        else:
            self.handTotal += new_card.value
        print(f"Dealer score total is {self.handTotal}")
    
    def add_sec_card(self, new_card):
        self.secHand.append(new_card)

def ask_bet(money):
    while True:
        try:
            gameBet = int(input("How much do you want to bet on this round?"))

            if gameBet > money:
                print("Sorry you don't have enough money to make that bet. Try again.")
                continue
            else:
                break
        except:
            print("Sorry you need to input an integer value")
#list of what needs to happen
# Start the game welcoming player and saying starting balance
# Make the deck
# give player two cards and dealer two cards one hidden and one not
# Ask player if they want to hit or just stay
# have dealer reveal hidden card then hit till they beat player or bust
# reveal winner and ask to play again

def card_tally():
    pass

def blackjack_game():
    yourName = input('What is your name?')

    playerOne = Player(yourName, 5000)
    dealer = Dealer()

    print(f'Hello {playerOne.name} your starting balance is {playerOne.money}')

    gameOn = True
    while gameOn:
        gameDeck = Deck()
        gameDeck.shuffle()

        ask_bet(playerOne.money)
        playerOne.add_card(gameDeck.deal_card())
        playerOne.add_card(gameDeck.deal_card())
        dealer.add_card(gameDeck.deal_card())
        dealer.add_sec_card(gameDeck.deal_card())
        
        playerTurn = True
        while playerTurn:
            pass

        dealerTurn = True
        while dealerTurn:
            pass




blackjack_game()