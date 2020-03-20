from deck import Deck
from player import Player

class Game_Controller():
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle_deck()
        #self.player = Player(input("What is your name? "))
        self.player = Player("Duncan")
        self.player_hand = []
        self.dealer_hand = []

    def deal_card(self, target):
        card = self.deck.deck.pop()
        if target == 'dealer':
            self.dealer_hand.append(card)
        elif target == 'player':
            self.player_hand.append(card)

    def show_hand(self, target):
        print("")
        if target == "player":
            print(f"{self.player.name}'s Hand:")
            for index, card in enumerate(self.player_hand):
                print(self.player_hand[index])
            player_score = self.calculate_hand('player')
            print(f"Score: {player_score}")

        elif target == "dealer":
            print("Dealer's Hand:")
            for index, card in enumerate(self.dealer_hand):
                print(self.dealer_hand[index])
            dealer_score = self.calculate_hand('dealer')
            print(f"Score: {dealer_score}")

        elif target == 'dealer-hidden':
            print("Dealer's Hand:")
            print(self.dealer_hand[0])
            print("Face down card")
            
        print("")

    def calculate_hand(self, target):
        if target == 'dealer':
            hand = self.dealer_hand
        elif target == 'player':
            hand = self.player_hand
        
        score = 0
        number_of_aces = 0
        for card in hand:
            if card.value in ['Jack', 'Queen', 'King']:
                score += 10
            elif card.value == 'Ace':
                number_of_aces += 1
            else:
                score += card.value
        
        while number_of_aces > 0:
            if score <= 10:
                score += 11
                number_of_aces -= 1
            else:
                score += 1
                number_of_aces -= 1
        
        return score

    def play_again(self):
        while True:    
            play_again = input("Do you want to play again? y/n ").lower()
            if play_again == 'y':
                return True
            elif play_again =='n':
                return False
            else:
                continue

    def play_game(self):
        playing = True 

        while playing:
            #player chooses stake
            while True:
                try:
                    print(f"Your current balance is: {self.player.balance}")
                    stake = int(input("How much do you want to bet? "))
                    self.player.place_bet(stake)
                except:
                    continue
                else:
                    break
            #initialise game
            self.deck = Deck()
            self.deck.shuffle_deck()
            self.player_hand = []
            self.dealer_hand = []
            #deal 2 cards to player and dealer
            self.deal_card('player')
            self.deal_card('dealer')
            self.deal_card('player')
            self.deal_card('dealer')
            
            #display starting hands and scores
            self.show_hand('player')
            self.show_hand('dealer-hidden')

            #playing hand
            currently_playing = 'player'
            player_won = False

            while True:
                score = self.calculate_hand(currently_playing)
                #decide whether current player hits or stands
                if currently_playing == 'player':
                    choice = input("Do you want to hit or stand? (h/s): ")
                else:
                    input("Press enter to see dealer's action")
                    choice = 'h' if score < 17 else 's'
                #resolve action    
                if choice == 'h':
                    print("\nHit me!\n")
                    self.deal_card(currently_playing)
                    self.show_hand(currently_playing)
                    score = self.calculate_hand(currently_playing)

                    if score > 21:
                        print("BUST!\n")
                        if currently_playing == 'player':
                            break
                        else:
                            player_won = True
                            break
                    else:
                        continue

                elif choice == 's':
                    print("\nI stand\n")
                    #print final hand
                    print("Final:")
                    self.show_hand(currently_playing)
                    #if player stands, now dealer plays
                    if currently_playing == 'player':
                        player_score = score
                        currently_playing = 'dealer'
                        self.show_hand(currently_playing)
                        continue
                    #if both players stand, work out who won
                    else:
                        dealer_score = score
                        print(f"Player: {player_score}")
                        print(f"Dealer: {dealer_score}")                        
                        player_won = player_score > dealer_score
                        break
            #tell player if they won, and pay them if they did
            if player_won:
                print("You win! You double your stake!")
                self.player.win_bet(stake*2)
                print(f"Your balance is now {self.player.balance}")
            else:
                print("You lost! Better luck next time.")
            #check if player wants to play another hand
            playing = self.play_again()

        print("See you next time!")

        


        
       

        


game = Game_Controller()
game.play_game()
