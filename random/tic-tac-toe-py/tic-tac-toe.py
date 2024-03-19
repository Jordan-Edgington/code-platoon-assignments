# This function creates the game board. It takes the board template,
# converts that to a list of lists, each containing numbers 1-3, 4-6, and 7-9
# It takes the input of x and o moves, and replaces the existing
import random
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def generate_board(x_moves, o_moves):
    board_template = '''\n\n\n\n\n\n\n\n
               1 | 2 | 3\n
    ---------\n4 | 5 | 6\n
    ---------\n7 | 8 | 9
    '''
    board_list = list(board_template.replace("|", "").replace(
        "-", "").replace("\n", "").replace(" ", ""))

    for move in x_moves:
        board_list[move - 1] = "X"

    for move in o_moves:
        board_list[move - 1] = "O"

    return [
        [board_list[0], board_list[1], board_list[2]],
        [board_list[3], board_list[4], board_list[5]],
        [board_list[6], board_list[7], board_list[8]]
    ]

# this just recreates the board from board_list


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * (5 * len(row) - 1))

# this creates the board... but coloring the winning spaces a diff color. This is only called at the end of the game.


def print_colored_board(board, winning_player=None, winning_positions=None):
    clear_screen()
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            position = i * 3 + j + 1
            if winning_positions and position in winning_positions:
                if winning_player == "X":
                    print("\033[95m{}\033[0m".format(cell), end="")
                elif winning_player == "O":
                    print("\033[91m{}\033[0m".format(cell), end="")
            else:
                print(cell, end="")
            if j < 2:
                print(" | ", end="")
        print()
        if i < 2:
            print("-" * 17)

# this takes the player's input, compares it against the existing x and o moves


def make_move(player, position, x_moves, o_moves):
    if 1 <= position <= 9:
        if player == "X":
            if position not in x_moves and position not in o_moves:
                x_moves.append(position)
                return True
            else:
                print("Invalid move. Cell already occupied.")
                return False
        elif player == "O":
            if position not in x_moves and position not in o_moves:
                o_moves.append(position)
                return True
            else:
                print("Invalid move. Cell already occupied.")
                return False
    else:
        print("Invalid move. Please choose a position between 1 and 9.")
        return False


# This creates the computer's move


def computer_move(x_moves, o_moves):
    all_moves = set(x_moves + o_moves)
    available_positions = [i for i in range(1, 10) if i not in all_moves]

    if available_positions:
        return o_moves.append(random.choice(available_positions))
    else:
        print("No moves available for computer.")
        return None

# checks to see if any winning combination exists on both X and O move lists


def check_game_state(x_moves, o_moves):
    winning_combinations = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Columns
        [1, 5, 9], [3, 5, 7]              # Diagonals
    ]
    for combination in winning_combinations:
        if all(move in x_moves for move in combination):
            global x_wins
            x_wins = True
            return combination
        elif all(move in o_moves for move in combination):
            global o_wins
            o_wins = True
            return combination

    if len(x_moves) + len(o_moves) == 9:
        global tie_game
        tie_game = True
        return

    return None

# returns whether X or O won the game


def check_winner(x_moves, o_moves):
    winning_combinations = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Columns
        [1, 5, 9], [3, 5, 7]              # Diagonals
    ]

    for combination in winning_combinations:
        if all(move in x_moves for move in combination):
            return "X"
        elif all(move in o_moves for move in combination):
            return "O"

    return None


# initialized all the variables used
x_moves = []
o_moves = []
x_wins = False
o_wins = False
tie_game = False
player = "X"

# this is the actual game loop which is exited when any of the game ending variables are set to True
while x_wins == False and o_wins == False and tie_game == False:
    # clears the screen, prints the board, and prints the moves that have been used
    clear_screen()
    print_board(generate_board(x_moves, o_moves))
    print("X Moves:", x_moves)
    print("O Moves:", o_moves)
    # prompts the player to make their move
    position = int(input("Player X, enter your move (1-9): "))
    success = make_move(player, position, x_moves, o_moves)
    # if the Player move is successful:
    if success:
        # checks to see if either player has won or if it is a tie
        check_game_state(x_moves, o_moves)
        # the computer plays its move
        computer_move(x_moves, o_moves)
        # checks game status again
        check_game_state(x_moves, o_moves)

print_colored_board(generate_board(x_moves, o_moves), check_winner(x_moves, o_moves),
                    check_game_state(x_moves, o_moves))
if x_wins == True:
    print("X Wins!")
elif o_wins == True:
    print("O wins!")
elif tie_game == True:
    print("It's a tie.")
