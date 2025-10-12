# Dealer class object with methods for adding cards to their main hand or their secret second hand, checking if their hand is bust, and clearing their hands.
class Dealer:
    def __init__(self):
        self.hand = []
        self.sec_hand = []
        self.hand_total = 0
        self.aces = 0

    def add_card(self, new_card):
        self.hand.append(new_card)
        print(f"The card given to the dealer is the {new_card}")
        if new_card.rank == 'Ace':
            self.aces += 1
            self.hand_total += new_card.value
        else:
            self.hand_total += new_card.value
        print(f"Dealer's total hand score is {self.hand_total}")
    
    def add_sec_card(self, new_card):
        self.sec_hand.append(new_card)

    def check_aces(self):
        while self.hand_total > 21 and self.aces:
            print("Dealer hand score is over 21, but they have an ace in their hand so they can fix it.")
            self.hand_total -= 10
            self.aces -= 1
            print(f"Dealers new hand score is {self.hand_total}.")
    
    def check_bust(self):
        if self.hand_total > 21:
            print(f"Dealer's total hand score is {self.hand_total} which is over 21 which means their hand is bust.")
            return True
        else:
            return False

    def clear_hand(self):
        self.hand.clear()
        self.sec_hand.clear()
        self.aces = 0
        self.hand_total = 0