import random

# Создаём поле, которое можно изменять по ходу игры
def create_board(size):
    board = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append('-')
        board.append(row)
    return board

# Вывод игрового поля
def print_board(board):
    print(" ", end='')
    for x in range(len(board)): print(f'{x}'.rjust(2), end="")
    print()
    for ind, i in enumerate(board):
        print(ind, end=' ')
        for j in i:
            print(j, end=" ")
        print()

# Ход игрока за X
def turn(player):
    print(f'Сейчас ходит {player}')
    while True:
        turn_input = input("Выберите ячейку (Напишите координаты слитно XY):")
        if str(turn_input).isnumeric() and len(str(turn_input)) == 2 and not board[int(turn_input[0])][int(turn_input[1])] != '-': break
    x, y = turn_input
    board[int(x)][int(y)] = player

# Ход компьютера за O
def computer_turn(board):
    possible_moves = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == "-"                         \
            or board[row-1][col] != ("X" or "O")              \
            or board[row][col-1] != ("X" or "O")              \
            or board[row-1][col-1] != ("X" or "O")            \
            or board[row][col+1] != ("X" or "O")              \
            or board[row+1][col] != ("X" or "O")              \
            or board[row+1][col+1] != ("X" or "O"):
                possible_moves.append((row, col))
    return possible_moves[random.randrange(len(possible_moves))]

# Проверка наличия 5 ходов в один ряд (Горизонталь/вертикаль/диагональ)
def is_player_lose(player):
    lose = 0
    n = len(board)
    # Горизонталь
    for i in range(n):
        for j in range(n):
            if board[i][j] == player:
                lose += 1
                if lose == 5:
                    return lose
            else:
                lose = 0
    # Вертикаль
    for i in range(n):
        for j in range(n):
            if board[j][i] == player:
                lose += 1
                if lose >= 5:
                    return lose
            else:
                lose = 0
    # Диагонали 
    for i in range(-(n - 1), n):
        for j in range(n):
            row, col = j, i + j
            if 0 <= row < n and 0 <= col < n:
                if board[row][col] == player:
                    lose += 1
                    if lose >= 5:
                        return lose
                else:
                    lose = 0
                    
    for i in range(-(n - 1), n):
        for j in range(n):
            row, col = j, i + j
            if 0 <= row < n and 0 <= col < n:
                if board[row][10 - col - 1] == player:
                    lose += 1
                    if lose >= 5:
                        return lose
                else:
                    lose = 0

# Проверка заполненности поля. Если возвращает True - завершает игру
def board_filled():
    for row in board:
        for item in row:
            if item == '-':
                return False
    return True


def main():
    turns = 0
    global board
    board = create_board(10)
    
    while True:
        player = "X" if turns % 2 == 0 else "O"
        turns += 1
        
        print_board(board)
        
        if player == "X":
            turn(player)
        else:
            row, col = computer_turn(board)
            board[row][col] = player

        if is_player_lose(player):
            print(f"Игрок {player} проиграл")
            print_board(board)
            break
        elif board_filled():
            print('Ничья!')
            break

if __name__ == "__main__":
    main()
