#imports
import random
import pandas as pd
import numpy as np
from IPython.display import display, Markdown
import time

game_on = True
game_continue = True
decided = False
new_game = True
game_point = ""
button = ""

while game_on == True: #Functions for NEW GAME here
    while decided == False:
        try:
            start_amount = int(input("DEALER: Welcome to Python Poker! Please nominate an amount for you and your opponent to start with! (Must be at least 100)"))
            if start_amount >99:
                your_stack = start_amount
                bot_stack = start_amount
                display(Markdown(f"**DEALER:** You will both be starting with: ${start_amount}! Best of Luck!"))
                decided = True
            else:
                display(Markdown("**DEALER:** The starting amount MUST be more than 100! Please try again."))
                time.sleep(3)
        except ValueError:
            display(Markdown("**DEALER:** The starting amount MUST be a valid number. Please try again."))
            time.sleep(3)

    
    if new_game == True:
        game_point = "pre-flop"        
        coin_sides = ["h", "t"]
        decided = False

        while decided == False:
            coin_guess = input("To decide our first button (person in traditional dealer position), how about a game of Heads Or Tails?")
            coin_flip = random.choice(coin_sides)

            if coin_flip == "h" or "heads":
                coin_outcome = "Heads"
                decided = True
            elif coin_flip == "t" or "tails":
                coin_outcome = "Tails"
                decided = True
            else:
                print(f"**DEALER:** That is not a valid call! Please type 'h' or 'heads' for 'heads' or 't' or 'tails' for 'tails'.")

        if coin_flip == coin_guess:
            decided = False
            while decided == False:  
                print(f"**DEALER:** {coin_outcome} it is! who will start as the button?")
                button = input("type 'Me' to start as the button or 'You' for Bot to start as the button")
                if button == "Me":
                    button = "You"
                    decided = True
                elif button == "You":
                    button = "Bot"
                    decided = True
                else:
                    print(f"**DEALER:** Your choice was unclear. Please try again")
                print(f"**DEALER:** Very well! {button} will start as the button!")

        else:
            button = random.choice(["I", "You"])
            if button == "I":
                button = "Bot"
            else:
                button = "You"
            print(f"**DEALER:** Unlucky, it was {coin_outcome}. Bot decides {button} will start as the button!")


    while game_continue == True: #Functions for NEW ROUND here
        if new_game == False:
            if button == "Bot":
                button == "You"
            else:
                button == "Bot"
            print(f"**DEALER:** This round, the button will be {button}!")
        new_game = False

        #PLAYING CARDS/VALUES/OTHER TOOLS
        playing_cards = ['A♠', 'K♠', 'Q♠', 'J♠', '10♠', '9♠', '8♠', '7♠', '6♠', '5♠', '4♠', '3♠', '2♠',
                        'A♥', 'K♥', 'Q♥', 'J♥', '10♥', '9♥', '8♥', '7♥', '6♥', '5♥', '4♥', '3♥', '2♥',
                        'A♦', 'K♦', 'Q♦', 'J♦', '10♦', '9♦', '8♦', '7♦', '6♦', '5♦', '4♦', '3♦', '2♦',
                        'A♣', 'K♣', 'Q♣', 'J♣', '10♣', '9♣', '8♣', '7♣', '6♣', '5♣', '4♣', '3♣', '2♣']

        values_dict = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, '10': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
        suit_list = ['♠','♥','♦','♣']


        #DEALING
        if game_point == "pre-flop":
            your_hand = []
            bot_hand = []

            your_values = []
            bot_values = []

            your_suits = []
            bot_suits = []

            flop = []
            turn = []
            river = []

            community_cards = []

            your_selection = []
            bot_selection = []

            card1 = random.choice(playing_cards)
            playing_cards.remove(card1)
            card2 = random.choice(playing_cards)
            playing_cards.remove(card2)
            card3 = random.choice(playing_cards)
            playing_cards.remove(card3)
            card4 = random.choice(playing_cards)
            playing_cards.remove(card4)

            if button == "Bot":
                your_hand.append(card1)
                your_hand.append(card3)
                bot_hand.append(card2)
                bot_hand.append(card4)
            elif button == "You":
                your_hand.append(card2)
                your_hand.append(card4)
                bot_hand.append(card1)
                bot_hand.append(card3)   

            for i in range(3):
                flop_card = random.choice(playing_cards)
                flop.append(flop_card)
                playing_cards.remove(flop_card)

            turn_card = random.choice(playing_cards)
            turn.append(turn_card)
            playing_cards.remove(turn_card)

            river_card = random.choice(playing_cards)
            river.append(river_card)
            playing_cards.remove(river_card)

            pot = 0

        #SELECTION APPENDS
        your_selection = []
        for card in your_hand:
                your_selection.append(card)

        bot_selection = []
        for card in bot_hand:
            bot_selection.append(card)

        community_cards = []

        if game_point == "flop":
            for card in flop:
                your_selection.append(card)

            for card in flop:
                bot_selection.append(card)

            for card in flop:
                community_cards.append(card)

            display(Markdown(f"**DEALER:** Here's the Flop! The {flop[0]}, The {flop[1]} And The {flop[2]}!")) 
            display(Markdown(f"**REMINDER:** The community cards are: {community_cards}, your pocket is: {your_hand}"))

        elif game_point == "turn":
            
            for card in flop:
                your_selection.append(card)
            for card in turn:
                your_selection.append(card)

            for card in flop:
                bot_selection.append(card)
            for card in turn:
                bot_selection.append(card)

            for card in flop:
                community_cards.append(card)
            for card in turn:
                community_cards.append(card)

            display(Markdown(f"**DEALER:** Here's the Turn! The {turn[0]}!")) 
            display(Markdown(f"**REMINDER:** The community cards are: {community_cards}, your pocket is: {your_hand}"))

        elif round == "river":
            for card in flop:
                your_selection.append(card)
            for card in turn:
                your_selection.append(card)
            for card in river:
                your_selection.append(card)

            for card in flop:
                bot_selection.append(card)
            for card in turn:
                bot_selection.append(card)
            for card in river:
                bot_selection.append(card)

            for card in flop:
                community_cards.append(card)
            for card in turn:
                community_cards.append(card)
            for card in river:
                community_cards.append(card)

            display(Markdown(f"**DEALER:** Here's the River! The {river[0]}!")) 
            display(Markdown(f"**REMINDER:** The community cards are: {community_cards}, your pocket is: {your_hand}"))

        display(Markdown(f"**REMINDER:** Your stack is: ${your_stack} and Bots stack is: ${bot_stack}"))
        display(Markdown(f"**REMINDER:** The pot is currently: ${pot}")) 

        your_values = []
        your_suits = []

        bot_values = []
        bot_suits = []

        for card in your_selection:
            yrank = card[:-1]
            yvalue = values_dict[yrank]
            ysuit = card[-1:]

            your_values.append(yvalue)
            your_suits.append(ysuit)

        for card in bot_selection:
            brank = card[:-1]
            bvalue = values_dict[brank]
            bsuit = card[-1:]

            bot_values.append(bvalue)
            bot_suits.append(bsuit)

        your_zip = zip(your_selection, your_values, your_suits)
        your_process = sorted(your_zip, key=lambda x: x[1], reverse=True)
        your_selection, your_values, your_suits = zip(*your_process)

        bots_zip = zip(bot_selection, bot_values, bot_suits)
        bots_process = sorted(bots_zip, key=lambda x: x[1], reverse=True)
        bot_selection, bot_values, bot_suits = zip(*bots_process)


        #LISTING ALL HANDS
        test_cards = ['A♠', 'K♠', 'Q♠', 'J♠', '10♠', '9♠', '8♠', '7♠', '6♠', '5♠', '4♠', '3♠', '2♠',
                        'A♥', 'K♥', 'Q♥', 'J♥', '10♥', '9♥', '8♥', '7♥', '6♥', '5♥', '4♥', '3♥', '2♥',
                        'A♦', 'K♦', 'Q♦', 'J♦', '10♦', '9♦', '8♦', '7♦', '6♦', '5♦', '4♦', '3♦', '2♦',
                        'A♣', 'K♣', 'Q♣', 'J♣', '10♣', '9♣', '8♣', '7♣', '6♣', '5♣', '4♣', '3♣', '2♣']

        for card in community_cards:
            test_cards.remove(card)


        hand_combos = pd.DataFrame(columns=['TestCard1', 'TestCard2'])

        filt = 0
        for i in range(len(test_cards)):
            filt += 1
            for ii in range(filt, len(test_cards)):
                test_card1 = test_cards[i]
                test_card2 = test_cards[ii]

                hand_info = {'TestCard1': test_card1, 'TestCard2': test_card2}
                new_index = len(hand_combos)
                hand_combos.loc[new_index] = hand_info

        best_hands = pd.DataFrame(columns=['Pocket1', 'Pocket2', 'BestHand', 'HandValue', 'Picture', 'HighValue1', 'HighValue2', 'HighValue3', 'HighValue4', 'HighValue5'])

        #TESTING HANDS
        if game_point in ["flop", "turn", "river"]:
            for i in range(len(hand_combos)):

                test_pocket = []
                test_hand = []
                test_values = []
                test_suits = []
                test_play = []
                
                royal_flush_hand = False
                straight_flush_hand = False
                straight_flush_draw = []
                straight_flush_values = []
                sf_count = 0 #measure for finding straight flush
                sf_start = 0 #measure for holding first straight flush card position
                quad_hand = False
                quad_draw = []
                quad_values = []
                full_house_hand = False
                full_house_draw = []
                full_house_values = []
                flush_hand = False
                flush_draw = []
                flush_values = []
                flush_suit = "" #variable to hold flush suit
                straight_hand = False
                straight_draw = []
                straight_values = []
                straight_suits = []
                low_straight_hand = False
                low_straight_draw = []
                low_straight_values = []
                low_straight_suits = []
                low_count = 0 #measure for finding low straight
                trip_hand = False
                trip_draw = []
                trip_values = []
                two_pair_hand = False
                two_pair_draw = []
                two_pair_values = []
                p = 0 #pair mark for finding second pairs
                one_pair_hand = False
                one_pair_draw = []
                one_pair_values = []

                test_rank = ""
                test_rank_value = 0

                high_value1 = 0
                high_value2 = 0
                high_value3 = 0
                high_value4 = 0
                high_value5 = 0

                test_pocket.append(hand_combos['TestCard1'][i])
                test_pocket.append(hand_combos['TestCard2'][i])
                
                for card in test_pocket:
                    test_hand.append(card)
                for card in community_cards:
                    test_hand.append(card)

                for i in range(len(test_hand)):
                    test_rank = test_hand[i][:-1]
                    test_value = values_dict[test_rank]
                    test_suit = test_hand[i][-1:]

                    test_values.append(test_value)
                    test_suits.append(test_suit)   

                    values_dict['A'] = 14
                    test_values = []

                for i in range(len(test_hand)):
                    rank = test_hand[i][:-1]
                    test_values.append(values_dict[rank])

                test_zip = zip(test_hand, test_values, test_suits)
                test_process = sorted(test_zip, key=lambda x: x[1], reverse=True)
                test_hand, test_values, test_suits = zip(*test_process)

                #QUADS
                for i in range(len(test_values)):
                    if test_values.count(test_values[i]) == 4:
                        for ii in range(i, i+4):
                            quad_draw.append(test_hand[ii])
                            quad_values.append(test_values[ii])
                        quad_hand = True
                        break

                #TRIPS
                for i in range(len(test_values)):
                    if test_values.count(test_values[i]) == 3:
                        for ii in range(i, i+3):
                            trip_draw.append(test_hand[ii])
                            trip_values.append(test_values[ii])
                        trip_hand = True
                        break
                
                #ONE PAIR
                for i in range(len(test_values)):
                    if test_values.count(test_values[i]) == 2:
                        p = i + 2
                        for ii in range(i, i+2):
                            one_pair_draw.append(test_hand[ii])
                            one_pair_values.append(test_values[ii])
                        one_pair_hand = True
                        break
                
                #TWO PAIR
                if one_pair_hand == True:
                    for i in range(p, len(test_values)):
                        if test_values.count(test_values[i]) == 2:
                            for card in one_pair_draw:
                                two_pair_draw.append(card)
                            for value in one_pair_values:
                                two_pair_values.append(value)
                            for ii in range(i, i+2):
                                two_pair_draw.append(test_hand[ii])
                                two_pair_values.append(test_values[ii])
                            two_pair_hand = True
                            break

                #FULL HOUSE
                if trip_hand == True and one_pair_hand == True:
                    for card in trip_draw:
                        full_house_draw.append(card)
                    for value in trip_values:
                        full_house_values.append(value)
                    for card in one_pair_draw:
                        full_house_draw.append(card)
                    for value in one_pair_values:
                        full_house_values.append(value)
                    full_house_hand = True
                
                #FLUSH
                for suit in suit_list:
                    if test_suits.count(suit) >=5:
                        flush_suit = suit
                        break
                if flush_suit != "":
                    for i in range(len(test_suits)):
                        if test_suits[i] == flush_suit:
                            flush_draw.append(test_hand[i])
                            flush_values.append(test_values[i])
                            if len(flush_draw) == 5:
                                flush_hand = True
                                break

                #STRAIGHT
                straight_draw.append(test_hand[0])
                straight_values.append(test_values[0])
                straight_suits.append(test_suits[0])

                for i in range(1, len(test_hand)):
                    if test_values[i-1] == test_values[i]:
                        straight_draw.append(test_hand[i])
                        straight_values.append(test_values[i])
                        straight_suits.append(test_suits[i])

                    elif test_values[i-1] - 1 == test_values[i]:
                        straight_draw.append(test_hand[i])
                        straight_values.append(test_values[i])
                        straight_suits.append(test_suits[i])

                    else:
                        if straight_values[0] - straight_values[-1] <4:
                            straight_draw.clear()
                            straight_values.clear()
                            straight_suits.clear()

                            straight_draw.append(test_hand[i])
                            straight_values.append(test_values[i])
                            straight_suits.append(test_suits[i])

                if straight_values[0] - straight_values[-1] <4:
                    straight_draw.clear()
                    straight_values.clear()
                    straight_suits.clear()
                else:
                    straight_hand = True

                #LOW STRAIGHT
                if straight_hand == False:
                    low_straight = [14, 5, 4, 3, 2]
                    low_count = 0

                    for low in low_straight:
                        if low in test_values:
                            low_count += 1
                            
                    if low_count == 5:
                        test_values = []
                        values_dict['A'] = 1

                        for i in range(len(test_hand)):
                            rank = test_hand[i][:-1]
                            test_values.append(values_dict[rank])

                        test_zip = zip(test_hand, test_values, test_suits)
                        test_processed = sorted(test_zip, key=lambda x: x[1], reverse=True)
                        test_hand, test_values, test_suits = zip(*test_processed)

                        low_straight = [5, 4, 3, 2, 1]

                        for i in range(len(test_hand)):
                            if test_values[i] in low_straight:
                                straight_draw.append(test_hand[i])
                                straight_values.append(test_values[i])
                                straight_suits.append(test_suits[i])

                        if straight_values[0] - straight_values[-1] <4:
                            straight_draw.clear()
                            straight_values.clear()
                            straight_suits.clear()
                        else:
                            straight_hand = True
                
                #STRAIGHT FLUSHES
                if straight_hand == True and flush_hand == True:
                    for i in range(len(test_suits)):
                        if test_suits[i] == flush_suit:

                            straight_flush_draw.append(test_hand[i])
                            straight_flush_values.append(test_values[i])

                elif low_straight_hand == True and flush_hand == True:
                    for i in range(len(test_suits)):
                        if test_suits[i] == flush_suit:

                            straight_flush_draw.append(test_hand[i])
                            straight_flush_values.append(test_values[i])

                for i in range(1,len(straight_flush_values)):
                    if straight_flush_values[i-1] -1 == straight_flush_values[i]:
                        sf_count += 1
                    else:
                        sf_count = 0

                    if sf_count == 4:
                        sf_start = i + 1
                        straight_flush_draw = straight_flush_draw[sf_start-5:sf_start]
                        straight_flush_values = straight_flush_values[sf_start-5:sf_start]
                        straight_flush_hand = True
                        if straight_flush_values[0] == 14:
                            royal_flush_hand = True            
                        break
                
                #RANKINGS
                if royal_flush_hand == True:
                    test_rank = "Royal Flush"
                    test_rank_value = 10
                    for card in straight_flush_draw:
                        test_play.append(card)
                    high_value1 = values_dict[test_play[0][:-1]]
                    high_value2 = values_dict[test_play[1][:-1]]
                    high_value3 = values_dict[test_play[2][:-1]]
                    high_value4 = values_dict[test_play[3][:-1]]
                    high_value5 = values_dict[test_play[4][:-1]]
                    

                elif straight_flush_hand == True:
                    test_rank = "Straight Flush"
                    test_rank_value = 9
                    for card in straight_flush_draw:
                        test_play.append(card)
                    high_value1 = values_dict[test_play[0][:-1]]
                    high_value2 = values_dict[test_play[1][:-1]]
                    high_value3 = values_dict[test_play[2][:-1]]
                    high_value4 = values_dict[test_play[3][:-1]]
                    high_value5 = values_dict[test_play[4][:-1]]

                elif quad_hand == True:
                    test_rank = "Four of a Kind"
                    test_rank_value = 8
                    for card in quad_draw:
                        test_play.append(card)
                    for card in test_hand:
                        if card not in test_play:
                            test_play.append(card)
                            if len(test_play) == 5:
                                break
                    high_value1 = values_dict[test_play[0][:-1]]
                    high_value2 = values_dict[test_play[1][:-1]]
                    high_value3 = values_dict[test_play[2][:-1]]
                    high_value4 = values_dict[test_play[3][:-1]]
                    high_value5 = values_dict[test_play[4][:-1]]

                elif full_house_hand == True:
                    test_rank = "Full House"
                    test_rank_value = 7
                    for card in full_house_draw:
                        test_play.append(card)
                    high_value1 = values_dict[test_play[0][:-1]]
                    high_value2 = values_dict[test_play[1][:-1]]
                    high_value3 = values_dict[test_play[2][:-1]]
                    high_value4 = values_dict[test_play[3][:-1]]
                    high_value5 = values_dict[test_play[4][:-1]]

                elif flush_hand == True:
                    test_rank = "Flush"
                    test_rank_value = 6
                    for card in flush_draw:
                        test_play.append(card)
                    high_value1 = values_dict[test_play[0][:-1]]
                    high_value2 = values_dict[test_play[1][:-1]]
                    high_value3 = values_dict[test_play[2][:-1]]
                    high_value4 = values_dict[test_play[3][:-1]]
                    high_value5 = values_dict[test_play[4][:-1]]

                elif straight_hand == True:
                    test_rank = "Straight"
                    test_rank_value = 5
                    for i in range(len(straight_values) -1):
                        if straight_values[i] != straight_values[i+1]:
                            test_play.append(straight_draw[i])
                            if len(test_play) == 5:
                                break
                    if len(test_play) == 4:
                        test_play.append(straight_draw[-1])
                    high_value1 = values_dict[test_play[0][:-1]]
                    high_value2 = values_dict[test_play[1][:-1]]
                    high_value3 = values_dict[test_play[2][:-1]]
                    high_value4 = values_dict[test_play[3][:-1]]
                    high_value5 = values_dict[test_play[4][:-1]]

                elif trip_hand == True:
                    test_rank = "Three of a Kind"
                    test_rank_value = 4
                    for card in trip_draw:
                        test_play.append(card)
                    for card in test_hand:
                        if card not in test_play:
                            test_play.append(card)
                            if len(test_play) == 5:
                                break
                    high_value1 = values_dict[test_play[0][:-1]]
                    high_value2 = values_dict[test_play[1][:-1]]
                    high_value3 = values_dict[test_play[2][:-1]]
                    high_value4 = values_dict[test_play[3][:-1]]
                    high_value5 = values_dict[test_play[4][:-1]]

                elif two_pair_hand == True:
                    test_rank = "Two Pair"
                    test_rank_value = 3
                    for card in two_pair_draw:
                        test_play.append(card)
                    for card in test_hand:
                        if card not in test_play:
                            test_play.append(card)
                            if len(test_play) == 5:
                                break
                    high_value1 = values_dict[test_play[0][:-1]]
                    high_value2 = values_dict[test_play[1][:-1]]
                    high_value3 = values_dict[test_play[2][:-1]]
                    high_value4 = values_dict[test_play[3][:-1]]
                    high_value5 = values_dict[test_play[4][:-1]]

                elif one_pair_hand == True:
                    test_rank = "One Pair"
                    test_rank_value = 2
                    for card in one_pair_draw:
                        test_play.append(card)
                    for card in test_hand:
                        if card not in test_play:
                            test_play.append(card)
                            if len(test_play) == 5:
                                break
                    high_value1 = values_dict[test_play[0][:-1]]
                    high_value2 = values_dict[test_play[1][:-1]]
                    high_value3 = values_dict[test_play[2][:-1]]
                    high_value4 = values_dict[test_play[3][:-1]]
                    high_value5 = values_dict[test_play[4][:-1]]

                else:
                    test_rank = "High Card"
                    test_rank_value = 1
                    for card in test_hand:
                        test_play.append(card)
                        if len(test_play) == 5:
                            break
                    high_value1 = values_dict[test_play[0][:-1]]
                    high_value2 = values_dict[test_play[1][:-1]]
                    high_value3 = values_dict[test_play[2][:-1]]
                    high_value4 = values_dict[test_play[3][:-1]]
                    high_value5 = values_dict[test_play[4][:-1]]

                hand_info = {'Pocket1': test_pocket[0], 'Pocket2': test_pocket[1], 'BestHand': test_rank, 'HandValue': test_rank_value, 'Picture': test_play, 'HighValue1': high_value1, 'HighValue2': high_value2, 'HighValue3': high_value3, 'HighValue4': high_value4, 'HighValue5': high_value5}
                
                new_index = len(best_hands)
                best_hands.loc[new_index] = hand_info

            #ORDERING DATAFRAME
            best_hands = best_hands.sort_values(by=['HandValue', 'HighValue1', 'HighValue2', 'HighValue3', 'HighValue4', 'HighValue5'], ascending=False)
            best_hands.reset_index(drop=True, inplace=True)

            #TEACHING BOT
            risk_assess = 0
            for i in range(len(best_hands)):
                if best_hands['Pocket1'][i] in bot_hand and best_hands['Pocket2'][i] in bot_hand:
                    risk_assess = best_hands.index[i]

            risk_assess = np.floor((risk_assess/len(best_hands)*100)*100)/100


        elif game_point == "pre-flop":

            bot_high = 0
            bot_low = 0
            bot_paired = False
            bot_suited = False
            bot_ranged = False
            aces = 0
            royals = 0
            mids = 0
            lows = 0

            bot_high = values_dict[bot_hand[0][:-1]]
            bot_low = values_dict[bot_hand[1][:-1]]

            
            if bot_hand[0][-1] == bot_hand[1][-1]:
                bot_suited = True

            if bot_high == bot_low:
                bot_paired = True
            elif bot_high - bot_low <=4:
                bot_ranged = True

            if bot_high == 14:
                aces +=1
            elif bot_high >9:
                royals +=1
            elif bot_high >5:
                mids +=1
            else:
                mids +=1

            if bot_low == 14:
                aces +=1
            elif bot_low >=10:
                royals +=1
            elif bot_low >=7:
                mids +=1
            else:
                mids +=1

            #TEACHING BOT
            risk_assess = 80

            if bot_paired == True:
                if aces == 2:
                    risk_assess -= 99
                elif royals == 2:
                    risk_assess -= 90
                elif mids == 2:
                    risk_assess -= 85
                elif lows == 2:
                    risk_assess -= 80

            if bot_suited == True:
                if aces == 1:
                    if royals == 1:
                        risk_assess -= 75
                    elif mids == 1:
                        risk_assess -= 70
                    elif lows == 1:
                        risk_assess -= 70
                elif royals == 1:
                    if royals == 2:
                        risk_assess -= 65
                    if mids == 1:
                        risk_assess -= 55
                    elif lows == 1:
                        risk_assess -= 40
                elif mids == 1:
                    if mids == 2:
                        risk_assess -= 40
                    elif lows == 1:
                        risk_assess -= 25
            
            elif bot_suited == False:
                if aces == 1:
                    if royals == 1:
                        risk_assess -= 60
                    elif mids == 1:
                        risk_assess -= 50
                    elif lows == 1:
                        risk_assess -= 40
                elif royals == 1:
                    if royals == 2:
                        risk_assess -= 40
                    if mids == 1:
                        risk_assess -= 25
                    elif lows == 1:
                        risk_assess -= 20
                elif mids == 1:
                    if mids == 2:
                        risk_assess -= 30
                    elif lows == 1:
                        risk_assess -= 20
                elif lows == 2:
                    risk_assess -= 10

            if bot_ranged == True:
                if royals == 2:
                    risk_assess -= 50
                elif royals == 1 and mids == 1:
                    risk_assess -=40
                elif mids == 2:
                    risk_assess -=30
                elif mids == 1 and lows == 1:
                    risk_assess -=20
                elif lows == 2:
                    risk_assess -= 15
            
            elif bot_ranged == False:
                if mids == 1 and lows == 1:
                    risk_assess +=40
                elif royals == 1 and lows == 1:
                    risk_assess += 20
                elif royals == 1 and mids == 1:
                    risk_assess +=10
                
            if risk_assess <0:
                risk_assess = 0
            elif risk_assess >100:
                risk_assess == 100

        
        #START PLAY
        start_betting = True
        betting_on = True
        you_all_in = False
        bot_all_in = False


        pot = 0

        if button == "You":
            your_turn = False
        else:
            your_turn = True


        #INITIALISE ROUND
        if start_betting == True:
            start_betting = False

            if your_turn == True: 
                decided = False
                while decided == False:
                    your_move = input("Would you like to 'Bet', 'Check' or 'Fold'?")
                    if your_move in ['Bet', 'Check', 'Fold']:
                        decided = True
                    else:
                        print("That is an invalid move! Please nominate to either 'Bet', 'Check' or 'Fold'.")
                        time.sleep(3)

                if your_move == "Bet":
                    decided = False
                    while decided == False:
                        your_bet = int(input(f"How much of your amount: {your_stack} would you like to bet? Must be at least 5% of your stack (${your_stack/100*5})"))
                        if your_bet < your_stack and your_bet > your_stack/100*5:
                            print(f"You have decided to open the pot for ${your_bet}! Action now on Bot!")
                            time.sleep(5)
                            pot += your_bet
                            your_stack -= your_bet
                            decided = True
                            your_turn = False
                        elif your_bet >= your_stack:
                            all_in = input(f"This amount will put you All-In! Type 'Confirm' to declaire you're All-In!")
                            if all_in == "Confirm":
                                you_all_in = True
                                your_bet = your_stack
                                pot += your_bet
                                your_stack -= your_stack
                                decided = True
                                your_turn = False
                                print(f"You have gone all in with ${your_bet}! Action now on Bot!")
                                time.sleep(5)
                elif your_move == "Check":
                    print("You have decided to check over to Bot! Action now on Bot!")
                    decided = True
                elif your_move == "Fold":
                    see_bot = input("You have decided to forfeit this round to Bot! Would you like to see Bots Hand? 'Yes' or 'No'?")
                    if see_bot == "Yes":
                        print(f"BOT: Certainly! I have {bot_hand}!")
                        decided = True
                    elif see_bot == "No":
                        print(f"BOT: Very well! I can respect that!")
                        decided = True
                    else:
                        print(f"BOT: Decision unclear, please answer 'Yes' or 'No'.")

            else:
                bot_factor = random.randint(35,100)
    
                if bot_factor - risk_assess >= 30:
                    bot_move = "Bet"
                elif bot_factor - risk_assess >= 0:
                    bot_move = "Check"
                else:
                    bot_move = "Fold"

                if bot_move == "Bet":
                    digit1 = random.randint(1,10)
                    digit2 = random.randint(1,10)
                    if digit1 == digit2:
                        print("ALL IN")
                        bot_all_in = True
                        bot_bet = bot_stack
                        pot += bot_bet
                        bot_stack -= bot_bet
                        action = "You"
                        display(Markdown(f"**DEALER:** Bot has gone All-In with: ${bot_bet}! Action is on you."))
                    else:
                        bot_bet = bot_stack/100*(bot_factor/(digit1+digit2))
                        bot_bet = int(bot_bet + 0.5)
                        pot += bot_bet
                        bot_stack -= bot_bet
                        action = "You"
                        display(Markdown(f"**DEALER:** Bot has wagered: ${bot_bet}, leaving them with: ${bot_stack}!"))
                        display(Markdown(f"**DEALER:** Pot-Size is now: ${pot}! Action on You"))
                elif bot_move == "Check":
                    display(Markdown(f"**DEALER:** Bot has decided to 'Check' over to You!"))
                    action = "Bot"   
                elif bot_move == "Fold":
                    your_stack += pot
                    pot = 0
                    start_round = True
                    display(Markdown(f"**DEALER:** Bot has decided to fold this hand and forfeit the pot total: ${pot} to You!"))
                    display(Markdown(f"**BOT:** Would you like to see my hand?"))
                    
                    decided = False
                    while decided == False:
                        bot_reveal = input("Would you like to see Bots hand? 'Yes' or 'No'")
                        if bot_reveal == "Yes":
                            display(Markdown(f"**BOT:** Certainly! I had: {bot_hand}"))
                            decided = True
                        elif bot_reveal == "No":
                            display(Markdown(f"**BOT:** Very well, I can respect that!"))
                            decided = True
                        else:
                            display(Markdown(f"**BOT:** I misunderstood, please answer 'Yes' or 'No'"))
                            time.sleep(3)
                            
                your_turn = True
        
        elif start_betting == False:
            start_betting = True


        
    

    

        #####################
        game_continue = False
        #####################


    ###############
    game_on = False
    ###############




        