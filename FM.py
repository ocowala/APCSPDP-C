import random,time
# reward: you win / 
# loss: you lose (-2) / 
class Game:

    def __init__(self):
        self.suits = ['♥', '♦', '♣', '♠']
        self.values = ['A','2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


        self.deck = []
        for i in range(4):
            for j in range(13):
                s = str(self.values[j]) + "" + str(self.suits[i])
                self.deck.append(s)

        random.shuffle(self.deck)
        #print(len(deck))
        #print(deck)
        self.player_list = []
        j = 0
        for i in range(4):
            new_list = []
            for k in range(13):
                new_list.append(self.deck[j])
                j = j + 1
            self.player_list.append(new_list)

        #print(deck[0])

        self.game_deck = [["7♥"],[],[],[]]
        self.idx_first = 0
        for i in range(4):
            for j in range(13):
                if self.player_list[i][j] == "7♥":
                    self.player_list[i].remove("7♥")
                    self.idx_first = (i+1)%4
                    break
        
        if self.idx_first > 0:
            print(f"PLAYER FIRST TO GO: ROBOT {self.idx_first}")
        else:
            print(f"PLAYER FIRST TO GO: PLAYER")
        print()


    def rl_turn(self):
