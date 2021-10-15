import random


def create_board(size):
    """ Создает поле размером :size: """
    board = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append('-')
        board.append(row)
    return board


def print_board(board):
    """ Выводит поле :board: """
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
    """ В данной игре игрок :player: ходит только за крестик 
        В цикле происходит валидация вводимых игроком координат
        (Являются ли числом? Две ли коориднаты даны? Свободна ли клетка?)
    """
    print(f'Сейчас ходит {player}')
    while True:
        turn_input = input("Выберите ячейку (Напишите координаты слитно XY):")
        if str(turn_input).isnumeric() \
                and len(str(turn_input)) == 2 \
                and not board[int(turn_input[0])][int(turn_input[1])] != '-':
            break
    x, y = turn_input
    board[int(x)][int(y)] = player


def computer_turn(board):
    """ Имитация хода компьютера. Просматриваются все возможные
        ходы, добавляются наиболее оптимальные (Хотя я даже не могу
        придумать, что означает "Оптимальный ход" в данном случае...)
    """
    possible_moves = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == "-"                                 \
                    or board[row-1][col] != ("X" or "O")              \
                    or board[row][col-1] != ("X" or "O")              \
                    or board[row-1][col-1] != ("X" or "O"):
                possible_moves.append((row, col))
    return possible_moves[random.randrange(len(possible_moves))]


def is_player_lose(player):
    """ Проверка, есть ли 5 в ряд для любого игрока :player:
        в любом из направлений
    """
    lose = 0
    size = len(board)
    # Горизонталь
    for i in range(size):
        for j in range(size):
            if board[i][j] == player:
                lose += 1
                if lose == 5:
                    return lose
            else:
                lose = 0
    # Вертикаль
    for i in range(size):
        for j in range(size):
            if board[j][i] == player:
                lose += 1
                if lose >= 5:
                    return lose
            else:
                lose = 0
    # Диагонали
    for i in range(-(size - 1), size):
        for j in range(size):
            row, col = j, i + j
            if 0 <= row < size and 0 <= col < size:
                if board[row][col] == player:
                    lose += 1
                    if lose >= 5:
                        return lose
                else:
                    lose = 0

    for i in range(-(size - 1), size):
        for j in range(size):
            row, col = j, i + j
            if 0 <= row < size and 0 <= col < size:
                if board[row][10 - col - 1] == player:
                    lose += 1
                    if lose >= 5:
                        return lose
                else:
                    lose = 0


def board_filled():
    """ Проверка зполненности поля 
        Если выдаёт True - геймовер
    """
    for row in board:
        for item in row:
            if item == '-':
                return False
    return True


def main():
    """ Процесс и логика игры
        - Сначала инициализируем ходы и поле;
        Далее, в цикле:
    >--> - Выводим поле;
    |    - Проверяем, кому отдавать ход - Игроку(X) / Компьютеру(O). Отдаём;
    |    - Проверяем есть ли 5 в ряд и свободное место в поле;
    ^--< По новой.
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
