import random

def get_possible_cards(game_deck,card_list):
    possible_cards = []
    suits = ['♥', '♦', '♣', '♠']
    for i in range(4):
        if len(game_deck[i]) == 0:
            possible_cards.append("7" + str(suits[i]))
        elif len(game_deck) > 0: 
            if game_deck[i][0][:-1] == "2":
                possible_cards.append("A" + str(suits[i]))
            elif game_deck[i][-1][:-1] == "10":
                possible_cards.append("J" + str(suits[i]))
            elif game_deck[i][-1][:-1] == "J":
                possible_cards.append("Q" + str(suits[i]))
            elif game_deck[i][-1][:-1] == "Q":
                possible_cards.append("K" + str(suits[i]))
            else:
                if game_deck[i][0][:-1] == "A" and game_deck[i][-1][:-1] != "K":
                    possible_cards.append(str(int(game_deck[i][-1][:-1])+1) + str(suits[i]))
                elif game_deck[i][0][:-1] != "A" and game_deck[i][-1][:-1] == "K":
                    possible_cards.append(str(int(game_deck[i][0][:-1])-1) + str(suits[i]))
                elif game_deck[i][0][:-1] != "A" and game_deck[i][-1][:-1] != "K":
                    possible_cards.append(str(int(game_deck[i][-1][:-1])+1) + str(suits[i]))
                    possible_cards.append(str(int(game_deck[i][0][:-1])-1) + str(suits[i]))
                else:
                    pass
                
    final_possible_cards = list(set(card_list).intersection(possible_cards))

    return final_possible_cards

def place_card(game_deck,card):

    suits = ['♥', '♦', '♣', '♠']
    for i in range(4):
        if card[-1] == suits[i]:
            if len(game_deck[i]) == 0:
                game_deck[i].append(card)
            elif game_deck[i][0][:-1] == "2" and card[:-1] == "A":
                game_deck[i].insert(0,card)
            elif game_deck[i][-1][:-1] == "10" and card[:-1] == "J":
                game_deck[i].append(card)
            elif game_deck[i][-1][:-1] == "J" and card[:-1] == "Q":
                game_deck[i].append(card)
            elif game_deck[i][-1][:-1] == "Q" and card[:-1] == "K":
                game_deck[i].append(card)
            elif game_deck[i][0][:-1] != "A" and str(int(game_deck[i][0][:-1])-1) == card[:-1]:
                game_deck[i].insert(0,card)
            else:
                game_deck[i].append(card)
    
    return game_deck


def game_deck_output(game_deck):
    output_list = []
    for i in range(4):
        new_list = []
        for i in range(13):
            new_list.append("0")
        output_list.append(new_list)
    print("\t    GAME DECK")
    print("---------------------------------")
    for i in range(4):
        for j in range(len(game_deck[i])):
            if game_deck[i][j][:-1] == "A":
                output_list[i][0] = game_deck[i][j]
            elif game_deck[i][j][:-1] == "J":
                output_list[i][-3] = game_deck[i][j]
            elif game_deck[i][j][:-1] == "Q":
                output_list[i][-2] = game_deck[i][j]
            elif game_deck[i][j][:-1] == "K":
                output_list[i][-1] = game_deck[i][j]
            else:
                output_list[i][int(game_deck[i][j][:-1])-1] = game_deck[i][j]
                
        # print(str(game_deck[i]))
    for i in range(13):
        for j in range(4):
            if output_list[j][i] == "0":
                print("|\t",end="")
            else:
                print(f"|  {output_list[j][i]}\t",end="")
        print("|")
    print("---------------------------------")
    #print(output_list)

            


def check_win(player_list):
    for i in range(len(player_list)):
        if len(player_list[i]) == 0:
            return i
    return -1


suits = ['♥', '♦', '♣', '♠']
values = ['A','2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


deck = []
for i in range(4):
    for j in range(13):
        s = str(values[j]) + "" + str(suits[i])
        deck.append(s)

random.shuffle(deck)
#print(len(deck))
#print(deck)
player_list = []
j = 0
for i in range(4):
    new_list = []
    for k in range(13):
        new_list.append(deck[j])
        j = j + 1
    player_list.append(new_list)

#print(deck[0])

game_deck = [["7♥"],[],[],[]]

for i in range(4):
    for j in range(13):
        if player_list[i][j] == "7♥":
            player_list[i].remove("7♥")
            break
#print(player_list[0])

# potential error for robot player is wrong card and results bad game deck
break_variable = False
while True:
    for i in range(4):
        possible_cards = get_possible_cards(game_deck,player_list[i])
        if(i == 0):
            #print("Your Cards:" + str(player_list[0]))
            print("PLAYER Possible Cards That Can Be Played:" + str(possible_cards))
            inp = input("Pick an Index [0-n] from possible cards (else pass):")
            if inp != "pass":
                inp = int(inp)
                game_deck = place_card(game_deck,possible_cards[inp])
                player_list[i].remove(possible_cards[inp])
                #possible_cards.remove(possible_cards[inp])
        else:
            #print("ROBOT CARDS:" + str(player_list[i]))
            print("ROBOT Possible Cards That Can Be Played:" + str(possible_cards))
            if len(possible_cards) != 0:
                rand_idx = random.randint(0,len(possible_cards)-1)
                game_deck = place_card(game_deck,possible_cards[rand_idx])
                player_list[i].remove(possible_cards[rand_idx])
                #possible_cards.remove(possible_cards[rand_idx])
        print("AFTER TURN:")
        
        game_deck_output(game_deck)
        for j in range(4):
            print(len(player_list[j]))
            
        if(check_win(player_list) != -1):
            break_variable = True
            break

    
    if break_variable == True:
        break

print(f"PLAYER {check_win(player_list) } wins")    





        
