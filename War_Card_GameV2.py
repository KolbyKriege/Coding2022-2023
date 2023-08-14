"Code Review by Karson Chrispens at 5:06 PM on 1/19"

from player import Player
deck1 = 'deck_b.txt'
#deck1 = 'own_test_double_war.txt'  # deBugging fast swich for txt files
#deck1 = 'deck_test_war.txt'

turns = 0
autolose_player1 = False
autolose_player2 = False


def sort_deck(deck):
    with open(deck) as temp:  # sort deck aka opens file text and returns the list for check hand
        temp = temp.read()
        temp = temp.strip()
        deck = temp.split('\n')
    return deck


def battle(player1, player2):  # normal battle check to to see if war or normal battle
    global turns
    player1_card = player1.playerdeck[0]
    player2_card = player2.playerdeck[0]
    # print(player1)
    # print(player2)
    if player1_card == player2_card:
        #turns += 0
        war(player1, player2)

    elif player1_card > player2_card:
        turns += 1
        player1.player_wins(player1_card, player2_card)
        player2.player_loses()

    elif player1_card < player2_card:
        turns += 1
        player2.player_wins(player1_card, player2_card)
        player1.player_loses()

    # print(turns)
    # print('battle', player1)  # debug tool
    # print('battle', player2)


def war(player1, player2):  # war code to see who wins after or contuinaly war FIX???
    global turns
    global autolose_player1
    global autolose_player2
    repeat_count = 0
    repeat_count_index = 4
    repeat = True
    if len(player1.playerdeck) < repeat_count_index:
        autolose_player1 = True
    elif len(player2.playerdeck) < repeat_count_index:
        autolose_player2 = True
    elif player1.playerdeck[repeat_count_index] > player2.playerdeck[repeat_count_index]:
        player1.player_wins_war(player2, player2)
        player2.player_loses_war()

    elif player1.playerdeck[repeat_count_index] < player2.playerdeck[repeat_count_index]:
        player2.player_wins_war(player1, player2)
        player1.player_loses_war()

    else:  # code for repeat ear after each other with a count for the player code
        if player1.playerdeck[repeat_count_index] == player2.playerdeck[repeat_count_index]:
            repeat_count_index == 8
            while repeat == True:

                # auto lose if the player doesn't have the needed cards
                if len(player1.playerdeck) < repeat_count_index:
                    autolose_player1 = True
                    break
                elif len(player2.playerdeck) < repeat_count_index:
                    autolose_player2 = True
                    break
                elif player1.playerdeck[repeat_count_index] > player2.playerdeck[repeat_count_index]:
                    player1.player_wins_war(player1, player2, repeat_count)
                    player2.player_loses_war(repeat_count)
                    break
                elif player1.playerdeck[repeat_count_index] < player2.playerdeck[repeat_count_index]:
                    player2.player_wins_war(player1, player2, repeat_count)
                    player1.player_loses_war(repeat_count)
                    break
                repeat_count_index += 4
                repeat_count += 1
    # print(turns)
    # print(player1)  # debug tool
    # print(player2)


deck = sort_deck(deck1)
test = Player(deck, 'Player 1')
test1 = Player(deck, 'Player 2')
test.check_hand(1)
test1.check_hand(2)

repeat = True
test_counds = 0
while repeat == True:
    test_counds += 1  # debug tool to stop program automatcily
    if test_counds == 700:
        # print(test)
        # print(test1)
        # print("NOPE!!!!!!!!!")
        break

        # OUtput for winner and loser
    if (test.playerdeck == []) or (autolose_player1 == True):
        print("Player 2 wins in {} turn(s)".format(turns))
        # print(test1)
        break
    elif (test1.playerdeck == []) or (autolose_player2 == True):
        print("Player 1 wins in {} turn(s)".format(turns))
        # print(test)
        break
    battle(test, test1)

# print(test)
# print(test1)# debug to see final list
