# Group name: August28th
# Members: Shunnosuke Takei, Zhixing Huang, Tan Jiun Koon, Brandon Gze Loong Lau

import random
import time


# a function display_game_options(player) that uses the passed player dictionary and their attributes to display the appropriate options for when it is player's turn.
def display_game_options(player):
    print("------------" + player.get('name') + "'s turn------------")

    # a line displaying the player's score.
    print(player.get('name') + "'s score:", player.get('score'))
    print("1. Roll")
    print("2. Stay")

    # If the player's score is at or above 14 then it must also display "3. Roll One".
    if player.get('score') >= 14:
        print("3. Roll One")


# A function display_round_stats(round, players) print the round statistics.
def display_round_stats(round, players):
    print('-----------Round {}-----------'.format(round))

    # A for loops to print the name of each player in the list of players as well as their corresponding score.
    for player in players:
        print('{} is at {}'.format(player['name'], player['score']))


# a function roll_dice(num_of_dice=1) that simulates a dice roll based on the number of dice the user wishes to roll, which by default is set to 1.
# the integer argument num_of_dice determining the number of dice rolls.
def roll_dice(num_of_dice=1):
    # result is list to represent a list of integers representing the result of each dice roll, a string combining the provided dice art for each roll into one big string.
    # dice_rolls a list of integers representing the result of each dice roll.
    result = []
    dice_rolls = []
    die_art = {
        1: ["┌─────────┐", "│         │", "│    ●    │", "│         │", "└─────────┘"],
        2: ["┌─────────┐", "│  ●      │", "│         │", "│      ●  │", "└─────────┘"],
        3: ["┌─────────┐", "│  ●      │", "│    ●    │", "│      ●  │", "└─────────┘"],
        4: ["┌─────────┐", "│  ●   ●  │", "│         │", "│  ●   ●  │", "└─────────┘"],
        5: ["┌─────────┐", "│  ●   ●  │", "│    ●    │", "│  ●   ●  │", "└─────────┘"],
        6: ["┌─────────┐", "│  ●   ●  │", "│  ●   ●  │", "│  ●   ●  │", "└─────────┘"]
    }

    # roll is a random number generator that replicates the roll of a 6 face die between 1 and 6 inclusive.
    # roll will need to be repeated as per num_of_dice.
    for x in range(num_of_dice):
        roll = random.randint(1, 6)
        dice_rolls.append(roll)

    # display_string a string combining the provided dice art for each roll into one big string, after the string will be appended to result.
    # counter is a variable to determine whether the string has to turn into next line or not.
    display_string = ""
    counter = 0

    # A for loops to combinine the provided dice art for each roll into one big string.
    for line_num in range(5):
        for dice_num in range(len(dice_rolls)):
            current = dice_rolls[dice_num]
            display_string += die_art[current][line_num]
            counter += 1

            # A if...else statement to concatenate a list of strings with newline separators to create a string of simple text-art.
            if counter % len(dice_rolls) == 0:
                display_string += "\n"
            else:
                continue

    # appending all the outcomes of variables dice_rolls and display_string into result.
    result.append(dice_rolls)
    result.append(display_string)
    return result


# a function execute_turn(player, player_input) that takes a player dictionary object and an integer for the player's choice of game options.
def execute_turn(player, player_input):
    # If the player's choice is a regular roll(2) and print the chosen action "Rolling both...".
    if player_input == 1:
        print("Rolling both...")

        # roll is a variable to roll the die by calling roll_dice(2) function and calculate the score player has rolled for this round, finally print the result of the roll as text-art.
        roll = roll_dice(2)
        print(roll[1])

        # update stats for player object 'score'.
        player['score'] += sum(roll[0])
        print(player['name'], "is now on", player['score'])

    # If the player's choice is 2(stayed), print the chosen action and update the stayed key of player to True.
    elif player_input == 2:
        print(player['name'], "has stayed with a score of", str(player['score']))
        player['stayed'] = True

    # If the player's choice is a single roll and print the chosen action "Rolling one...".
    elif player_input == 3:
        print("Rolling one...")

        # roll is a variable to roll the die by calling roll_dice(1) function and calculate the score player has rolled for this round, finally print the result of the roll as text-art.
        roll = roll_dice(1)
        print(roll[1])
        # update stats for player object 'score'
        player['score'] += sum(roll[0])
        print(player['name'], "is now on", player['score'])

    # If the roll causes them to go bust, it must print a message saying so and update the bust key of player to True.
    if player['score'] > 21:
        player['bust'] = True
        print(player['name'], "goes bust!")

    # If a player's roll is >= 14, in which case it must update the at_14 key of player to True.
    elif player['score'] >= 14:
        player['at_14'] = True

    # updating player object needs to be returned.
    return player


# A function end_of_game(players) that takes a list of player dictionary objects, representing the statistics for all players.
def end_of_game(players):
    for x in range(len(players)):
        # If the game is not over, the function simply needs to return False and not print anything.
        if not (players[x]['stayed']) and not (players[x]['bust']):
            return False
        else:
            continue

    # score_tally is a empty list to calculate all the players status, if the players is busted, appending the number 0, else just appending their score.
    score_tally = []
    for x in range(len(players)):
        # if the players is busted, appending the number 0.
        if players[x]['bust']:
            score_tally.append(0)

        # if the players is not busted, appending their score.
        else:
            score_tally.append(players[x]['score'])

    # winner_score is a variable to count the number of highest player's score.
    # winner_index is a variable to get the index of highest player's score.
    winner_score = score_tally.count(max(score_tally))
    winner_index = score_tally.index(max(score_tally))

    # If the maximum score of all the players is still 0, which means all the players are gone bust.
    if max(score_tally) == 0:
        print("Everyone's gone bust! No one wins :(")

    # If the winner_score of all the players more than 1, which means there are players have the same maximum score.
    elif winner_score > 1:
        print("The game is a draw! No one wins :(")

    # If there is only one players has the highest score, that the player is the winner.
    else:
        print(players[winner_index]['name'], "is the winner!")
    return True


# a function multiplayer_game(num_of_players) that runs a game of Twenty One for multiple users playing on the same device.
# an argument num_of_players which represents the number of players.
def multiplayer_game(num_of_players):
    players = []
    count = 0
    round = 0

    # A for loops to combine the different players into a list of players.
    for x in range(num_of_players):
        count += 1
        player_x = {'name': 'Player ' + str(count), 'score': 0, 'stayed': False, 'at_14': False, 'bust': False}
        players.append(player_x)

    # When the returned value of calling the function end_of_game(players) is False, the code below will be executed.
    while not end_of_game(players):
        round += 1
        display_round_stats(round, players)

        for x in range(len(players)):
            # If either of player's object 'bust' or 'stayed' is True, the code will go back to the while loops and the code below the else statement will not be executed.
            if players[x]['bust'] or players[x]['stayed']:
                continue
            else:
                display_game_options(players[x])
                player_choice = int(input("Please enter an option: "))
                # calling the function execute_turn() to update the player object.
                execute_turn(players[x], player_choice)


# The function main() will put all our different features into one program with a simple user interface.
def main():
    # initializing start_game into False.
    start_game = False
    while not start_game:

        # try block lets you test a block of code for errors.
        # First needs to display a list of options.
        try:
            print('------------Main Menu------------')
            print('Welcome to Twenty One!')
            print('1. Solo')
            print('2. Local Multiplayer')
            print('3. Rules')
            print('4. Exit')
            print('---------------------------------')

            # variable user_input prompt the users to select a valid option.
            user_input = int(input('Select option: '))

            # If the input is 1, it will turn start_game into True and calling the fucntion solo_game()
            if user_input == 1:
                start_game = True
                solo_game()

            # If the input is 2, it will turn start_game into True and calling the fucntion multiplayer_game(num_players)
            elif user_input == 2:
                start_game = True
                num_players = int(input('Enter number of players: '))
                multiplayer_game(num_players)

            # If the input is 3, it will call the fucntion display_rules() and go back function def main()
            elif user_input == 3:
                display_rules()

            # If the input is 4, it will exit and stop execute the code.
            elif user_input == 4:
                break

        # If the input is invalid value, try block raises an error, the except block will be executed.
        except:
            print('Error - Invalid input')


# The function display_rules() will display all the rules.
def display_rules():
    print("""
      _____________________________________________________________________________
      Twenty One is a game of chance where players take turns rolling two dice every 
      round until they decide to stop rolling and lock in their score or end up 
      going bust with a total over 21. The objective is to be the closest to 21 
      when everyone is done rolling.

      Rules are as per follows:
        - Players begin with a score of 0.
        - Each player has one turn to either roll or stop rolling each round.
        - Players can only do a regular roll of two dice until they 
          reach a score of at least 14.
        - Players with a score >= 14 have the option to only roll one dice.
        - If a player scores more than 21 they go bust and are out of the game.
        - The winning player is the one with the score closest to 21 when everyone 
          has finished rolling.
        - If all players go bust, no one wins.
        - If more than one player has the winning score, no one wins.
      _____________________________________________________________________________
      """)
    # after Press Enter will go back to the Main Menu.
    input("Press Enter to go back to the Main Menu\n")
    return


#  a function solo_game() that runs a game of Twenty One for one user against a computer player.
def solo_game():
    # players is a variable contains two player objects, one for the user and one computer player.
    players = [{'name': 'Player 1', 'score': 0, 'stayed': False, 'at_14': False, 'bust': False},
               {'name': 'CPU Player', 'score': 0, 'stayed': False, 'at_14': False, 'bust': False}]
    # Tracking the round for players.
    round = 0

    # If calling function end_of_game() returns False, the code below will be executed.
    while not end_of_game(players):
        round += 1

        # each round the round statistics will be printed.
        display_round_stats(round, players)
        for x in range(len(players)):
            # If either of player's object 'bust' or 'stayed' is True, the code will go back to the while loops and the code below the else statement will not be executed.
            if players[x]['bust'] or players[x]['stayed']:
                continue

            else:
                # If x = 0, meaning is for the (players) turn, and the code below will be executed.
                if x == 0:

                    # calling display_game_options(player) to show options for player to choose .
                    display_game_options(players[0])
                    player_choice = int(input("Please enter an option: "))

                    # calling the function execute_turn() to update the player object.
                    execute_turn(players[0], player_choice)

                # If x = 1, meaning is for the (CPU players) turn, and the code below will be executed.
                else:
                    cpu_player_choice(players[1], players[1]['score'])


# A function cpu_player_choice(score) with the CPU player's score to receive an integer as a choice.
def cpu_player_choice(player, score):
    # calling display_game_options(player) to show options for CPU player to choose.
    display_game_options(player)
    print('Please enter an option: ', end='\r')

    # Generating a random number.
    secs = random.random() * 5
    probability = random.random()

    # If the score of CPU player is lower than 14, definitely will select the choice 1 to roll 2 dice.
    if score < 14:
        choice = 1

    # If the score of CPU player is lower than 16, CPU player can select the option for choices 1, 2 and 3.
    elif score <= 16:
        if probability <= 0.75:  # 75% chance of choosing to roll 2 dice.
            choice = 1
        elif probability <= 0.95:  # 20% chance of choosing to roll 1 die.
            choice = 3
        else:
            choice = 2  # 5% chance of choosing to stay.

    # When the score of CPU player is getting higher, the probability of choosing 1(roll 2 dice) will definitely become lower.
    elif score <= 18:
        if probability <= 0.4:  # 40% chance of choosing to roll 1 die.
            choice = 3
        elif probability <= 0.9:  # 50% chance of choosing to stay.
            choice = 2
        else:
            choice = 1  # 10% chance of choosing to roll 2 dice.

    # When the score of CPU player is getting higher and higher, the probability of choosing 2(stayed) will definitely become higher.
    elif score <= 20:
        if probability <= 0.92:  # 92% chance of choosing to stay.
            choice = 2
        elif probability <= 0.98:  # 6% chance of choosing to roll 1 die.
            choice = 3
        else:
            choice = 1  # 2% chance of choosing to roll 2 dice.
    else:  # if score is 21
        choice = 2  # 100% chance of choosing to stay

    #  time.sleep(secs) to suspend the execution of the code for secs seconds.
    time.sleep(secs)
    print('Please enter an option:', choice)

    # calling the function execute_turn() to update the CPU player object.
    execute_turn(player, choice)


# Calling the method main()
main()

# just make some random changes.
