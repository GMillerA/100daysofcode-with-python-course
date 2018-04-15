from RPS_Classes import Roll, Player
import random


def main():
    print_header()

    #rolls = build_the_three_rolls() # TODO: figure out what this function should do

    name = get_players_name()

    player1 = Player(name)
    player2 = Player("computer")

    game_loop(player1, player2)


def print_header():
    print('---------------------------------------------')
    print('          Rock Paper Scissors ')
    print('---------------------------------------------')
    print("            Best 2 out of 3 ")
    print("")


def game_loop(player1, player2):
    moves = ["Rock", "Paper", "Scissors"]
    count = 1
    count_wins = 0
    count_loss = 0
    while count < 3:
        p2_choice = random.choice(moves)
        p2_roll = Roll(p2_choice)  # get random roll
        p1_roll = get_player_move()  # have player choose a roll

        outcome = p1_roll.can_defeat(p2_roll)

        # display throws
        print("{}: {}".format(player1.name, p1_roll.name))
        print("{}: {}".format(player2.name, p2_roll.name))
        # display winner for this round
        print(outcome)

        if outcome == "Win":
            count_wins += 1
            count += 1
        if outcome == "Lose":
            count_loss += 1
            count += 1
        else:
            print("Try Again!")

    # Compute who won
    if count_wins > count_loss:
        print("{} Wins!".format(player1.name))
    else:
        print("{} Wins!".format(player2.name))


def get_players_name():
    name = input("Enter Player Name: ")
    return name


def get_player_move():
    move = input("What is your move? ")
    #if move not in moves:
    if move not in ["Rock", "Paper", "Scissors"]:
        print("Not a possible move. Try again.")
        move = input("What is your move? ")
    return Roll(move)


def build_the_three_rolls():
    pass


if __name__ == '__main__':
    main()