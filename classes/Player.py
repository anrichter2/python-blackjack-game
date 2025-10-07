# Player class object with methods for adding cards checking if the players hand has busted change their money amount and clear their hand.
class Player:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.hand = []
        self.hand_total = 0

    def add_card(self, new_card):
        self.hand.append(new_card)
        print(f"The card you are given is the {new_card}")
        if new_card.rank == 'Ace':
            while True:
                card_value = input("You got an ace do you want it's value to be 1 or 11? ")
                if card_value not in ['1', '11']:
                    print("Sorry you didn't input a proper value try again.")
                    continue
                elif card_value == '1':
                    self.hand_total += new_card.value[0]
                    break
                else:
                    self.hand_total += new_card.value[1]
                    break   
        else:
            self.hand_total += new_card.value
        print(f"Your total hand score is {self.hand_total}")
    
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
        self.hand_total = 0
