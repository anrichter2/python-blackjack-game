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
        return self.rank + ' of ' + self.suit

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
        print(f"The card you are givin is the {new_card}")
        if new_card.rank == 'Ace':
            while True:
                card_value = input("You got an ace do you want it's value to be 1 or 11? ")
                if card_value not in ['1', '11']:
                    print("Sorry you didn't input a proper value try again.")
                    continue
                elif card_value == '1':
                    self.handTotal += new_card.value[0]
                    break
                else:
                    self.handTotal += new_card.value[1]
                    break   
        else:
            self.handTotal += new_card.value
        print(f"Your total hand score is {self.handTotal}")
    
    def check_bust(self):
        if self.handTotal > 21:
            print(f"Your total hand score is {self.handTotal} which is over 21 which means your hand is bust.")
            return True
        else:
            return False

    def change_money(self, amount):
        self.money += amount

    def clear_hand(self):
        self.hand.clear()
        self.handTotal = 0
    
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
        print(f"The card givin to the dealer is the {new_card}")
        if new_card.rank == 'Ace':
            if self.handTotal <= 10:
                self.handTotal += 11
            else:
                self.handTotal += 1   
        else:
            self.handTotal += new_card.value
        print(f"Dealer's total hand score is {self.handTotal}")
    
    def add_sec_card(self, new_card):
        self.secHand.append(new_card)

    def check_bust(self):
        if self.handTotal > 21:
            print(f"Dealer's total hand score is {self.handTotal} which is over 21 which means their hand is bust.")
            return True
        else:
            return False

    def clear_hand(self):
        self.hand.clear()
        self.secHand.clear()
        self.handTotal = 0

def ask_bet(money):
    while True:
        try:
            gameBet = int(input("How much do you want to bet on this round? "))

            if gameBet > money:
                print("Sorry you don't have enough money to make that bet. Try again.")
                continue
            elif gameBet < 0:
                print("Sorry you can't make negative bets. Please Try again.")
            else:
                break
        except:
            print("Sorry you need to input an integer value.")
    return gameBet

def play_again():
    while True:
        response = input("Would you like to play again? Yes or no? ").lower()
        if response not in ['yes', 'no']:
            print("Sorry you didn't answer yes or no. Please try again.")
        else:
            if response == 'yes':
                return True
            else:
                return False

def blackjack_game():
    yourName = input('What is your name? ')

    playerOne = Player(yourName, 5000)
    dealer = Dealer()

    gameOn = True
    while gameOn:
        print(f'Hello {playerOne.name} your balance is ${playerOne.money}.')
        gameDeck = Deck()
        gameDeck.shuffle()

        bet_amount = ask_bet(playerOne.money)
        print("Dealing two cards to the player face up.")
        playerOne.add_card(gameDeck.deal_card())
        playerOne.add_card(gameDeck.deal_card())
        print("Dealing one card to the dealer face up and one card face down.")
        dealer.add_card(gameDeck.deal_card())
        dealer.add_sec_card(gameDeck.deal_card())
        
        playerBust = False

        print(f"Your total hand score is {playerOne.handTotal}")
        while not playerBust:

            hit_stay = input("Do you want to hit or stay? ").lower()
            if hit_stay not in ['hit', 'stay']:
                print("Sorry you didn't enter hit or stay. Please try again.")
                continue
            if hit_stay == 'stay':
                break
            if hit_stay == 'hit':
                playerOne.add_card(gameDeck.deal_card())

            playerBust = playerOne.check_bust()

        dealerBust = False

        print(f"Dealer's total hand score is {dealer.handTotal}.")
        while not dealerBust and not playerBust:
            if len(dealer.secHand):
                print("Revealing the dealer's secret second card.")
                dealer.add_card(dealer.secHand[0])
                dealer.secHand.clear()
            elif dealer.handTotal < 17:
                print("Dealer decides to draw another card.")
                dealer.add_card(gameDeck.deal_card())
            else:
                print(f"Dealer decides to stay.")
                break
            
            dealerBust = dealer.check_bust()

        if playerBust:
            print(f"Sorry but you went bust so the dealer wins. You lose ${bet_amount}.")
            playerOne.change_money(-bet_amount)
        elif dealerBust:
            print(f"Dealer went bust so you win. You win ${bet_amount}.")
            playerOne.change_money(bet_amount)
        elif playerOne.handTotal == dealer.handTotal:
            print(f"You and the dealer have equal value hands so the dealer wins. You lose ${bet_amount}.")
            playerOne.change_money(-bet_amount)
        elif playerOne.handTotal > dealer.handTotal:
            print(f"Your hand is better than the dealers. You win ${bet_amount}.")
            playerOne.change_money(bet_amount)
        else:
            print(f"Dealers hand is better. You lose ${bet_amount}.")
            playerOne.change_money(-bet_amount)

        gameOn = play_again()

        if gameOn:
            playerOne.clear_hand()
            dealer.clear_hand()
        
    print(f"Thank you for playing. Your end money total was ${playerOne.money}.")

blackjack_game()