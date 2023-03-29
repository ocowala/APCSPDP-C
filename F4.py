import random
import time
# For a certain player, this method checks the possible cards that can be played from the card deck of the player
# the method returns a list that is the possible cards that could be played
def get_possible_cards(game_deck : list ,card_list : list) -> list:
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

#places a certain card on the game deck in a specific manner
def place_card(game_deck: list ,card: str) -> list:

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

#outputs the game deck in a neat and structured manner
def game_deck_output(game_deck: list) -> None:
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
                if output_list[j][i][-1] == "♥" or output_list[j][i][-1] == "♦":
                    print(f"|  \033[0;31;48m{output_list[j][i]}\033[0m\t",end="")
                else:
                    print(f"|  \033[0;30;48m{output_list[j][i]}\033[0m\t",end="")
        print("|")
    print("---------------------------------")
    #print(output_list)

#outputs cards in a colorized way for formatting purposes.
def color_output_card(card: str) -> str:
    new_card = ""
    if card == "pass":
        #yellow
        new_card = f"\033[1;33;48m{card}\033[0m"
    elif card[-1] == "♥" or card[-1] == "♦":
        #red
        new_card = f"\033[0;31;48m{card}\033[0m"
    else:
        #black
        new_card = f"\033[0;30;48m{card}\033[0m"
    return new_card

# outputs the possible cards list in a colorized mannner for output-formatting purposes
def output_color_possible_cards(possible_cards: list) -> None:
    new_possible_cards = []
    for i in range(len(possible_cards)):
        new_possible_cards.append(color_output_card(str(possible_cards[i])))
    print("[",end="")
    for i in range(len(new_possible_cards)):
        if i == len(new_possible_cards)-1:
            print(new_possible_cards[i],end="")
        else:
            print(new_possible_cards[i]+",",end="")
    print("]")

# checks which player is the winner by checking if any of the lists in the player_list is of length 0 which means they win
# it returns the index or if none, -1
def check_win(player_list: list) -> int:
    for i in range(len(player_list)):
        if len(player_list[i]) == 0:
            return i
    return -1

# main method that contains the instructions and simulation of the game
def main() -> None:

    print("Welcome to Badam Satti")
    print("Instructions:")
    print("\t1. Place down cards on the game deck in order to clear your hand")
    print("\t2. If you don't have any cards, type \"pass\"")
    print("\t3. HAVE FUN!\n")
    print("\t\t\033[0;31;48mFIRST PLAYER TO CLEAR THEIR HAND WINS!\033[0m\n\n\n")
    time.sleep(2)
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
    idx_first = 0
    for i in range(4):
        for j in range(13):
            if player_list[i][j] == "7♥":
                player_list[i].remove("7♥")
                idx_first = (i+1)%4
                break
    
    if idx_first > 0:
        print(f"PLAYER FIRST TO GO: ROBOT {idx_first}")
    else:
        print(f"PLAYER FIRST TO GO: PLAYER")
    print()
    #print(player_list[0])

    # potential error for robot player is wrong card and results bad game deck
    break_variable = False
    while True:
        card = "pass"
        possible_cards = get_possible_cards(game_deck,player_list[idx_first])
        if(idx_first == 0):
            #print("PLAYER Cards:" + str(player_list[idx_first]))
            print("PLAYER Possible Cards That Can Be Played:",end="")
            output_color_possible_cards(possible_cards)
            inp = input("Pick an Index [0-n] from possible cards (else pass):")
            string_val_index = []
            for i in range(len(possible_cards)):
                string_val_index.append(str(i))

            if inp != "pass" and inp in string_val_index:
                inp = int(inp)
                card = possible_cards[inp]
                game_deck = place_card(game_deck,card)
                player_list[idx_first].remove(card)
                #possible_cards.remove(possible_cards[inp])

            else:
                if len(possible_cards) > 0:
                    while True:
                        inp = input("Pick an Index [0-n] from possible cards (MUST BE VALID):")
                        if inp != "pass" and inp in string_val_index:
                            inp = int(inp)
                            card = possible_cards[inp]
                            game_deck = place_card(game_deck,card)
                            player_list[idx_first].remove(card)
                            break
        else:
            #print(f"ROBOT {idx_first} CARDS:" + str(player_list[idx_first]))
            #print(f"ROBOT {idx_first} Possible Cards That Can Be Played:" + str(possible_cards))
            if len(possible_cards) != 0:
                rand_idx = random.randint(0,len(possible_cards)-1)
                card = possible_cards[rand_idx]
                game_deck = place_card(game_deck,card)
                player_list[idx_first].remove(card)
                #possible_cards.remove(possible_cards[rand_idx])

        game_deck_output(game_deck)
        if idx_first == 0:
            print(f"PLAYER DEALT {color_output_card(card)}")
        else:
            print(f"ROBOT {idx_first} DEALT {color_output_card(card)}")
        #print(output_robots_that_completely_sure(player_list))
        idx_first += 1
        idx_first %= 4
        #print("AFTER TURN:")
        time.sleep(1)
        print("\n\n\n\n")
        # for j in range(4):
        #     if j == 0:
        #         print(f"# OF PLAYER CARDS:{len(player_list[j])}")
        #     else:
        #         print(f"# OF ROBOT {j} CARDS:{len(player_list[j])}")
            
        if(check_win(player_list) != -1):
            break_variable = True
            break
    
    who = check_win(player_list)
    if who == 0:
        print("YOU WIN!")   
    else:
        print(f"ROBOT {who} WINS!")
        
if __name__ == '__main__':
    main()