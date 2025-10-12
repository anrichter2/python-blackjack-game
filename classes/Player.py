# Player class object with methods for adding cards checking if the players hand has busted change their money amount and clear their hand.
class Player:
    def __init__(self, name, money=2000):
        self.name = name
        self.money = money
        self.hand = []
        self.hand_total = 0
        self.aces = 0

    def add_card(self, new_card):
        self.hand.append(new_card)
        print(f"The card you are given is the {new_card}")
        if new_card.rank == 'Ace':
            self.aces += 1
            self.hand_total += new_card.value
        else:
            self.hand_total += new_card.value
        print(f"Your total hand score is {self.hand_total}")
    
    def check_aces(self):
        while self.hand_total > 21 and self.aces:
            print("Your hand score is over 21, but you have an ace in your hand so you can fix it.")
            self.hand_total -= 10
            self.aces -= 1
            print(f"Your new hand score is {self.hand_total}.")

    def check_bust(self):
        if self.hand_total > 21:
            print(f"Your total hand score is {self.hand_total} which is over 21 which means your hand is bust.")
            return True
        else:
            return False

    def change_money(self, amount):
        self.money += amount

    def clear_hand(self):
        self.hand.clear()
        self.aces = 0
        self.hand_total = 0
