class Player():
    def __init__(self, name, balance=100):
        self.name = name
        self.balance = balance

    def place_bet(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
            raise Exception
        elif amount < 0:
            print("We're not paying you to gamble")
            raise Exception
        self.balance -= amount
    
    def win_bet(self, amount):
        self.balance += amount

    def __str__(self):
        return self.name
    