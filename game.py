from classes import Deck, Player, Dealer
import os

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Function for asking the player how much money they want to bet on the game of blackjack
def ask_bet(money):
    while True:
        # Try except block for making sure the player gives a positive integer value
        try:
            game_bet = int(input("How much do you want to bet on this round? "))

            if game_bet > money:
                print("Sorry you don't have enough money to make that bet. Try again.")
                continue
            elif game_bet < 0:
                print("Sorry you can't make negative bets. Please Try again.")
            else:
                break
        except:
            print("Sorry you need to input an integer value.")
    return game_bet

# Function for asking the player if they want to play again after a game of blackjack
def play_again():
    # While loop used for making sure the player gives proper yes or no response
    while True:
        response = input("Would you like to play again? Yes or no? ").lower()
        if response not in ['yes', 'no']:
            print("Sorry you didn't answer yes or no. Please try again.")
        else:
            if response == 'yes':
                return True
            else:
                return False

# Main game function
def blackjack_game():
    # Creating player object and dealer object
    player_name = input('What is your name? ')
    player_one = Player(player_name, 5000)
    dealer = Dealer()

    clear_console()
    # While loop continuously restarting the game for as long as the player wants
    game_on = True
    while game_on:
        print(f'Hello {player_one.name} your balance is ${player_one.money}.')
        # Creates the deck object and shuffles the card objects inside the deck object
        game_deck = Deck()
        game_deck.shuffle()

        # Ask player for bet amount and then give initial cards
        bet_amount = ask_bet(player_one.money)
        print("Dealing two cards to the player face up.")
        player_one.add_card(game_deck.deal_card())
        player_one.add_card(game_deck.deal_card())
        print("Dealing one card to the dealer face up and one card face down.")
        dealer.add_card(game_deck.deal_card())
        dealer.add_sec_card(game_deck.deal_card())
        
        print(f"Your total hand score is {player_one.hand_total}")

        player_bust = False
        # While loop used to allow the player to continuously add cards to their hand till satisfied or they bust.
        while not player_bust:
            hit_stay = input("Do you want to hit or stay? ").lower()
            if hit_stay not in ['hit', 'stay']:
                print("Sorry you didn't enter hit or stay. Please try again.")
                continue
            if hit_stay == 'stay':
                break
            if hit_stay == 'hit':
                player_one.add_card(game_deck.deal_card())

            player_bust = player_one.check_bust()

        print(f"Dealer's total hand score is {dealer.hand_total}.")
        
        dealer_bust = False
        # While loop used to make the dealer reveal their second card then they hit till they hit 17 or bust.
        while not dealer_bust and not player_bust:
            if len(dealer.sec_hand):
                print("Revealing the dealer's secret second card.")
                dealer.add_card(dealer.sec_hand[0])
                dealer.sec_hand.clear()
            elif dealer.hand_total < 17:
                print("Dealer decides to draw another card.")
                dealer.add_card(game_deck.deal_card())
            else:
                print(f"Dealer decides to stay.")
                break
            
            dealer_bust = dealer.check_bust()

        # if and elif statements to determine the winner
        if player_bust:
            print(f"Sorry but you went bust so the dealer wins. You lose ${bet_amount}.")
            player_one.change_money(-bet_amount)
        elif dealer_bust:
            print(f"Dealer went bust so you win. You win ${bet_amount}.")
            player_one.change_money(bet_amount)
        elif player_one.hand_total == dealer.hand_total:
            print(f"You and the dealer have equal value hands so the dealer wins. You lose ${bet_amount}.")
            player_one.change_money(-bet_amount)
        elif player_one.hand_total > dealer.hand_total:
            print(f"Your hand is better than the dealers. You win ${bet_amount}.")
            player_one.change_money(bet_amount)
        else:
            print(f"Dealers hand is better. You lose ${bet_amount}.")
            player_one.change_money(-bet_amount)

        game_on = play_again()

        # Clears the hands for the dealer and the player
        if game_on:
            player_one.clear_hand()
            dealer.clear_hand()
        
        clear_console()
    
    # Print statement for when the player is done playing   
    print(f"Thank you for playing. Your end money total was ${player_one.money}.")

blackjack_game()