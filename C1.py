import random
class Card:
    def __init__(self, value: int, color: str):
        self.value = value
        self.color = color
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o,Card):
            if __o.value == self.value and __o.color == self.color:
                return True
        return False
        
def main():
    print("Welcome to Badam Satti!")
    s = str(input("Enter your name:"))

    # create deck
    colors = ['heart', 'diamonds', 'spades', 'clubs']
    deck = [Card(value, color) for color in colors for value in range(1, 14) ]
    random.shuffle(deck)
    # assign cards to players
    cards = []
    for player in range(1,5):
        cards.append([ deck.pop(0) for i in range(1, 14) ])

    # assign deck to game environment (first array is player turn)
    # hearts [0], diamonds[1], spades[2], clubs[3]
    deck = [[0],[0],[0],[0]]

    # deal 7 of hearts
    startnum = 0
    
    for player in cards:
        y = False
        for card in player:
            if(card.color == "heart" and card.value == 7):
                deck[0][0] = card
                player.remove(card)
                y = True
                break
        if y: break
        startnum += 1

    # goes to next player that is after the player dealt 7
    startnum += 1 
    startnum %= 4

    # start game
    print("at this stage" + str(startnum))
    while len(deck[0]) != 0 or len(deck[1]) != 0 or len(deck[2]) != 0 or len(deck[3]) != 0:
        # start each player turn
        for player in cards:
            # human turn
            print("startnum: " + str(startnum))
            if startnum == 0:
                # print for player
                print("Your current deck: \n[")
                for card in player:
                    print(f"({card.value},{card.color}), ",)
                print("]")
                # make player turn
                possible_cards = []
                num = 0
                for suit in deck:
                    if suit[0] == 0:
                        # middle
                        if num == 1:
                            possible_cards.append(Card(7,"diamonds"))
                        elif num == 2:
                            possible_cards.append(Card(7,"spades"))
                        elif num == 3:
                            possible_cards.append(Card(7,"clubs"))
                    else:
                        # ends
                        if num == 0:
                            possible_cards.append(Card(suit[0].value-1,"heart"))
                            possible_cards.append(Card(suit[len(suit)-1].value+1,"heart"))
                        elif num == 1:
                            possible_cards.append(Card(suit[0].value-1,"diamonds"))
                            possible_cards.append(Card(suit[len(suit)-1].value+1,"diamonds"))
                        elif num == 2:
                            possible_cards.append(Card(suit[0].value-1,"spades"))
                            possible_cards.append(Card(suit[len(suit)-1].value+1,"spades"))  
                        elif num == 3:
                            possible_cards.append(Card(suit[0].value-1,"clubs"))
                            possible_cards.append(Card(suit[len(suit)-1].value+1,"clubs"))       
                    num += 1
                
                #retain all cards that are in the card list of player  
                print("BEFORE Possible cards:\n[")
                for card in possible_cards:
                    print(f"({card.value},{card.color})")
                print("]")           
                common_list = [c for c in possible_cards if c in player]
                possible_cards = common_list
                # print for debug
                print("Possible cards:\n[")
                for card in possible_cards:
                    print(f"({card.value},{card.color})")
                print("]")

                #ask user to place one of the possible cards
                inn = str(input("Which card would you like to pick: "))
                if inn != "skip":
                    inn_list = inn.split()
                    # put requested card into deck
                    req_value = int(inn_list[0])
                    req_color = str(inn_list[1])
                    req_card = Card(req_value,req_color)
                
                    if req_color == "heart":
                        if req_value == deck[0][0].value-1:
                            deck[0].insert(0,req_card)
                        elif req_value == deck[0][-1].value+1:
                            deck[0].append(req_card)

                    elif req_color == "diamonds":
                        if deck[1][0] == 0:
                            deck[1][0] = card
                        else:
                            if req_value == deck[1][0].value-1:
                                deck[1].insert(0,req_card)
                            elif req_value == deck[1][-1].value+1:
                                deck[1].append(req_card)

                    elif req_color == "spades":
                        if deck[2][0] == 0:
                            deck[2][0] = card
                        else:
                            if req_value == deck[1][0].value-1:
                                deck[2].insert(0,req_card)
                            elif req_value == deck[2][-1].value+1:
                                deck[2].append(req_card)

                    elif req_color == "clubs":
                        if deck[3][0] == 0:
                            deck[3][0] = card
                        else:
                            if req_value == deck[3][0].value-1:
                                deck[3].insert(0,req_card)
                            elif req_value == deck[3][-1].value+1:
                                deck[3].append(req_card)
                    
                    player.remove(card)

                print("BOARD DECK")
                print("[")
                for suit in deck:
                    print("[")
                    for i in range(len(suit)):
                        if isinstance(suit[0],Card):
                            print(f"({suit[i].value},{suit[i].color}),")
                        else:
                            print(str(suit[i]) + ",")
                    print("],")
                print("]")

            else:
                # robot turn
                # print for player
                print("Robot current deck: \n[")
                for card in player:
                    print(f"({card.value},{card.color}), ",)
                print("]")
                # make player turn
                possible_cards = []
                num = 0
                for suit in deck:
                    if suit[0] == 0:
                        # middle
                        if num == 1:
                            possible_cards.append(Card(7,"diamonds"))
                        elif num == 2:
                            possible_cards.append(Card(7,"spades"))
                        elif num == 3:
                            possible_cards.append(Card(7,"clubs"))
                    else:
                        # ends
                        if num == 0:
                            possible_cards.append(Card(suit[0].value-1,"heart"))
                            possible_cards.append(Card(suit[len(suit)-1].value+1,"heart"))
                        elif num == 1:
                            possible_cards.append(Card(suit[0].value-1,"diamonds"))
                            possible_cards.append(Card(suit[len(suit)-1].value+1,"diamonds"))
                        elif num == 2:
                            possible_cards.append(Card(suit[0].value-1,"spades"))
                            possible_cards.append(Card(suit[len(suit)-1].value+1,"spades"))  
                        elif num == 3:
                            possible_cards.append(Card(suit[0].value-1,"clubs"))
                            possible_cards.append(Card(suit[len(suit)-1].value+1,"clubs"))       
                    num += 1
                
                #retain all cards that are in the card list of player        
                print("BEFORE Possible cards:\n[")
                for card in possible_cards:
                    print(f"({card.value},{card.color})")
                print("]")   
                common_list = [c for c in possible_cards if c in player]
                possible_cards = common_list
                # print for debug
                print("Possible cards:\n[")
                for card in possible_cards:
                    print(f"({card.value},{card.color})")
                print("]")

                #random choice in accordance to if there are any cards in possible_cards
                if len(possible_cards) != 0:
                    req_card = random.choice(possible_cards)
                    print(f" req card: ({req_card.value},{req_card.color})")
                    req_color = req_card.color
                    req_value = req_card.value

                    if req_color == "heart":
                        if req_value == deck[0][0].value-1:
                            deck[0].insert(0,req_card)
                        elif req_value == deck[0][-1].value+1:
                            deck[0].append(req_card)

                    elif req_color == "diamonds":
                        if deck[1][0] == 0 and len(deck[1]) == 1:
                            deck[1][0] = card
                        else:
                            if isinstance(deck[1][0],Card):
                                if req_value == deck[1][0].value-1:
                                    deck[1].insert(0,req_card)
                                elif req_value == deck[1][-1].value+1:
                                    deck[1].append(req_card)

                    elif req_color == "spades":
                        if deck[2][0] == 0 and len(deck[2]) == 1:
                            deck[2][0] = card
                        else:
                            if isinstance(deck[2][0],Card):
                                if req_value == deck[2][0].value-1:
                                    deck[2].insert(0,req_card)
                                elif req_value == deck[2][-1].value+1:
                                    deck[2].append(req_card)

                    elif req_color == "clubs":
                        if deck[3][0] == 0 and len(deck[3]) == 1:
                            deck[3][0] = card
                        else:
                            if isinstance(deck[3][0],Card):
                                if req_value == deck[3][0].value-1:
                                    deck[3].insert(0,req_card)
                                elif req_value == deck[1][-1].value+1:
                                    deck[3].append(req_card)
                    
                    player.remove(req_card)

                print("BOARD DECK")
                print("[")
                for suit in deck:
                    print("[")
                    for i in range(len(suit)):
                        if isinstance(suit[0],Card):
                            print(f"({suit[i].value},{suit[i].color}),")
                        else:
                            print(str(suit[i]) + ",")
                    print("],")
                print("]")


            # skip to next turn
            startnum += 1
            startnum %= 4
        

            


if __name__ == '__main__':
    main()
