# Code Review: Adma Taylor 

import random
win = 0
lose = 0
stay_cout = 0
switch_count = 0
games_played = 0
live_results = (0, 0, 0, 0, 0)
switch_count_won = 0
stay_cout_won = 0
repeat = True

# live game fucntion that player will play


def live_game(win, lose, switch_count, stay_cout, games_played, switch_count_won, stay_cout_won):
    repeat = True
    while repeat == True:
        switch = False  # defineing varilbes that are needed to be reset

        games_played += 1
        big_prize = random.randint(1, 3)  # random int for winning door
        while repeat == True:
            # prompt use to pick a door and check if that enter a valild input
            user_choise = input(
                "\nPick a door 1-3 for the chance to win a prize: ")
            if user_choise.isdigit():
                user_choise = int(user_choise)
                if (1 <= user_choise <= 3):
                    break
            print("Please type a number 1-3")
            # funcation call for a door to show and prints the reslts
        show_door = otherdoorpick(user_choise, big_prize)                 # fix $100 
        print("\nNow before we go on we go on. I will let you know that behind door {} we don't have a prize!".format(show_door))

        while repeat == True:  # prompt the user to stay or switch doors and checks for vaild input
            switch_choise = input("Would you like to stay with your current door #{} or switch to doors #{}: ".format(
                user_choise, switch_door_choise(show_door, user_choise)))
            if switch_choise.lower() == 'switch':
                switch_count += 1
                switch = True
                # funcation call to switch door choise
                user_choise = switch_door_choise(show_door, user_choise)
                break
            elif switch_choise.lower() == 'stay':
                stay_cout += 1

                break
            else:
                print("Error PLease type 'stay' or 'switch'.\n")
        # chekcs if player wins or loses the game
        if big_prize == user_choise:
            print('\n Congruations you win $100,000')
            win += 1
            if switch == True:  # count win for each for win/loss ratio
                switch_count_won += 1
            else:
                stay_cout_won += 1
        else:
            print("\n OH NO! You didn't win our Grand Prize better luck next time! ")
            lose += 1
        # prompts user if they want to play again and check for vaild input
        while repeat == True:
            user_repeat = input("\nWould you like to play again? (yes/no): ")
            if user_repeat.lower() == 'yes':
                break
            elif user_repeat.lower() == 'no':
                repeat = False
                break
            else:
                print("Please type 'yes' or 'no'.")

    return(win, lose, switch_count, stay_cout, games_played, switch_count_won, stay_cout_won)

# funciotn for the simulated game


def sim_game(win, lose, switch_count, stay_cout, games_played, switch_count_won, stay_cout_won):
    # prompt user to input how many game they want to simulate and the 3 for those games
    user_sim_len = int(
        input("How many times do you want to simulate a game?: "))
    print()

    games_played = user_sim_len
    for x in range(user_sim_len):  # for loop till lenght is fill
        x=x
        switch = False
        # random int for prize and door choise and choises and door to show
        big_prize = random.randint(1, 3)
        compu_choise = random.randint(1, 3)
        show_door = otherdoorpick(compu_choise, big_prize)

        # random int to see if computer stays or switches
        comput_switch_choise = random.randint(1, 2)

        # if and else statement to switch or stay
        if comput_switch_choise == 1:
            switch_count += 1
            switch = True
            compu_choise = switch_door_choise(show_door, compu_choise)
        else:
            stay_cout += 1

        # if-else to see if if computer won or loses
        if big_prize == compu_choise:
            win += 1
            if switch == True:  # count win for each for win/loss ratio
                switch_count_won += 1
            else:
                stay_cout_won += 1
        else:
            lose += 1
    return(win, lose, switch_count, stay_cout, games_played, switch_count_won, stay_cout_won)

# fucntino to pick a random door if it is able to


def otherdoorpick(userchoise, compuchoise):
    while repeat == True:
        show_door = random.randint(1, 3)
        if (compuchoise != show_door) and (userchoise != show_door):
            break
    return(show_door)

# fucntion to switch to a door that is not the door shown or the orginal choise


def switch_door_choise(show_door, choise):
    final = 0
    for i in range(1, 4):
        if (i != choise) and (i != show_door):
            final = i
            break
    return final


# main program
print("\nHello and Welcome to.....")
print("   PICK THE DOOR!\n")
# user input to seed random numbers and checks input
while repeat == True:
    try:
        user_seed = int(
            input("Please enter a seed so you can repeat the same results: "))
    except:
        print("Plesea type any number.")
        continue
    else:
        break


random.seed(user_seed)
# while loop so user and play a live game before or after simulated game
while repeat == True:
    print("Would you like to see a simulated game or play a live gamge.")
    print("Type 'play' to play a game, 'sim' to see a simulated game, or type 'quit' to exit the game.")
    user_pick = input()
    if user_pick.lower() == 'play':
        # calls the live game and prints the reuslts of games
        live_results = live_game(
            win, lose, switch_count, stay_cout, games_played, switch_count_won, stay_cout_won)
        try:
            print("\nHere are your results for the {} games you played".format(
                live_results[4]))
            print("Total wins: {}".format(live_results[0]))
            print("Total loses: {}".format(live_results[1]))
            print(
                "Your win/loss ratio {:.2%}\n".format(live_results[0]/live_results[4]))  # prints raito in % form
            print("Total stays: {}".format(live_results[3]))
            print(
                "   Your win/loss ratio for staying is: {:.2%}".format(live_results[6]/live_results[3]))
            print("Total switchs: {}".format(live_results[2]))
            print(
                "   Your win/loss ratio for switching is: {:.2%}".format(live_results[5]/live_results[2]))
        except:
            print("\nSomething when wrong sorry. Try again. \n")
            continue
        print()

    elif user_pick.lower() == 'sim':
        # call simulated game and print the results of the simulated games
        sim_results = sim_game(win, lose, switch_count, stay_cout,
                               games_played, switch_count_won, stay_cout_won)
        try:
            print("Total wins: {}".format(sim_results[0]))
            print("Total loses: {}".format(sim_results[1]))
            print(
                "Your win/loss ratio {:.2%}\n".format(sim_results[0]/sim_results[4]))  # prints raito in % form
            print("Total stays: {}".format(sim_results[3]))
            print(
                "   Your win/loss ratio for staying is: {:.2%}".format(sim_results[6]/sim_results[3]))
            print("Totaly switchs: {}".format(sim_results[2]))
            print(
                "   Your win/loss ratio for switching is: {:.2%}".format(sim_results[5]/sim_results[2]))
        except:
            print("\nSomething when wrong sorry. Try again. \n")
            continue
        print()

    elif user_pick.lower() == 'quit':
        break
    else:  # check for vaild input
        print("Please enter a one of the three opitions\n")
print("\nThank You For Playing")  # Endding message ofr user
