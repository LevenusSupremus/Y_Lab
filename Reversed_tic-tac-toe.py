import random


def create_board(size):
    """ Creates a field of :size: """
    board = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append('-')
        board.append(row)
    return board


def print_board(board):
    """ Outputs a field :board: """
    print(" ", end='')
    for x in range(len(board)):
        print(f'{x}'.rjust(2), end="")
    print()
    for ind, i in enumerate(board):
        print(ind, end=' ')
        for j in i:
            print(j, end=" ")
        print()


def turn(player):
    """ In this game :player: plays as cross 

    The loop validates the coordinates entered by the :player:
    (Is the input a number? Are two coordinates given? Is the cell free?)
    """
    print(f'Now {player} turn')
    while True:
        turn_input = input("Choose cell (Something like '12' or '34'): ")
        if str(turn_input).isnumeric() \
                and len(str(turn_input)) == 2 \
                and not board[int(turn_input[0])][int(turn_input[1])] != '-':
            break
    x, y = turn_input
    board[int(x)][int(y)] = player


def computer_turn(board, player):
    """ Simulation of the computer's progress. 

    All possible moves are viewed, the most optimal ones are added 
    (Although I can't even think of what "Optimal move" means in this case...)
    """
    possible_moves = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == "-":
                possible_moves.append((row, col))
    return possible_moves[random.randrange(len(possible_moves))]


def lose_message(player):
    print(f"Player {player} lost")
    print_board(board)


def is_player_lose(player):
    """ Checking if there are 5 in a row for 
    any :player: in any of the directions.
    I need an lose_arr to check that the values are
    not carried over
    """
    lose = 0
    lose_arr = []
    size = len(board)

    # Horizontal
    temp = 0
    for i in range(size):
        for j in range(size):
            if board[i][j] == player:
                if temp != i:
                    lose_arr.clear()
                    lose = 0
                    temp = i
                lose += 1
                lose_arr.append((player, i, j))
                if lose >= 5:
                    lose_message(player)
                    return True
            else:
                lose_arr.clear()
                lose = 0
    lose = 0
    lose_arr.clear()

    # Vertical
    for i in range(size):
        for j in range(size):
            if board[j][i] == player:
                if temp != i:
                    lose_arr.clear()
                    lose = 0
                    temp = i
                lose += 1
                lose_arr.append((player, j, i))
                if lose >= 5:
                    lose_message(player)
                    return True
            else:
                lose_arr.clear()
                lose = 0
    lose = 0
    lose_arr.clear()

    # Diagonal upper-left to bottom-right
    for i in range(-(size - 1), size):
        for j in range(size):
            row, col = j, i + j
            if 0 <= row < size and 0 <= col < size:
                if board[row][col] == player:
                    if len(lose_arr):
                        if lose_arr[-1][1]+1 != col:
                            lose_arr.clear()
                            lose = 0
                    lose += 1
                    lose_arr.append((player, col, row))
                    if lose >= 5:
                        lose_message(player)
                        return True
                else:
                    lose_arr.clear()
                    lose = 0
    lose = 0
    lose_arr.clear()

    # Diagonal bottom-left to bottom-right
    for i in range(-(size - 1), size):
        for j in range(size):
            row, col = j, i + j
            if 0 <= row < size and 0 <= col < size:
                if board[row][10 - col - 1] == player:
                    if len(lose_arr):
                        if lose_arr[-1][1]+1 != row:
                            lose_arr.clear()
                            lose = 0
                    lose += 1
                    lose_arr.append((player, row, 10 - col - 1))
                    if lose >= 5:
                        lose_message(player)
                        return True
                else:
                    lose_arr.clear()
                    lose = 0
    lose = 0
    lose_arr.clear()


def board_filled():
    """ Checking whether the field is full  
    If return True - game over
    """
    for row in board:
        for item in row:
            if item == '-':
                return False
    return True


def main():
    """ The logic of the game

        - At first, initialize the turns and field;
        Then, in loop:
    >--> - Output the field;
    |    - Check, whose turn is it now - PLayer(X) / Program(O). He makes a move;
    |    - Check if there 5 in a row and free space available on the filed;
    ^--< Try again, until someone will fall...
    """
    turns = 0
    global board
    board = create_board(10)

    while True:
        print_board(board)

        player = "X" if turns % 2 == 0 else "O"
        turns += 1

        if player == "X":
            turn(player)
            # ? Uncomment part of the code below so the programm
            # ? will play with istelf, if u know what i mean
            # row, col = computer_turn(board, player)
            # board[row][col] = player
        else:
            row, col = computer_turn(board, player)
            board[row][col] = player

        if is_player_lose(player):
            break
        elif board_filled():
            if is_player_lose("O"):
                print(f"Player O lost")
            elif is_player_lose("X"):
                print(f"Player X lost")
            else:
                print('Draw!')
                print_board(board)
            break


if __name__ == "__main__":
    main()
