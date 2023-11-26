def allowed_moves_func(playing_list: list, current_position: int) -> list:
    moves_list = []
    m = len(playing_list)
    left_adjacent = playing_list[max(0, current_position-2): current_position]
    right_adjacent = playing_list[current_position+1: min(m+1, current_position+3)]
    left_length = len(left_adjacent)
    right_length = len(right_adjacent)

    if left_length == 2:
        if left_adjacent[0] == 1 and left_adjacent[1] == -1:
            moves_list.append([-2, 1])
        elif left_adjacent[0] == -1 and left_adjacent[1] == -1 and playing_list[:current_position].count(-1) != current_position:
            return []
    if right_length == 2:
        check = m-current_position-1
        if right_adjacent[0] == 1 and right_adjacent[1] == -1:
            moves_list.append([2, -1])
        elif right_adjacent[0] == 1 and right_adjacent[1] == 1 and playing_list[current_position+1:].count(1) != m-current_position-1:
            return []

    if left_length >= 1:
        if left_adjacent[-1] == 1:
            moves_list.append([-1, 1])
            # index = current position -1, current position += 1
    if right_length >= 1:
        if right_adjacent[0] == -1:
            moves_list.append([1, -1])

    return moves_list


def update_playing_board(playing_board_inside, current_position: int, move: list) -> int:
    playing_board_inside[current_position] += move[1]
    playing_board_inside[current_position + move[0]] -= move[1]
    return current_position + move[0]


n = int(input('Please enter a natural number n. (Enter 0 to quit) '))

while n != 0:

    print([1]*n + [0] + [-1]*n)
    playing_board = [1]*(n-1) + [0] + [1] + [-1]*(n)
    goal = [-1]*n + [0] + [1]*n
    blank = n-1

    branching_points = []
    history_boards = []
    while playing_board != goal:
        if not branching_points:
            print(playing_board)
        else:
            history_boards.append(playing_board.copy())

        allowed_moves = allowed_moves_func(playing_board, blank)
        if len(allowed_moves) == 0:
            history_boards.clear()
            old_board, old_blank, old_move = branching_points.pop()
            blank = update_playing_board(old_board, old_blank, old_move)
            playing_board = old_board
        elif len(allowed_moves) == 1:
            blank = update_playing_board(playing_board, blank, allowed_moves.pop())
        else:
            move_1, move_2 = allowed_moves
            branching_points.append([playing_board.copy(), blank, move_2])
            blank = update_playing_board(playing_board, blank, move_1)

    for board in history_boards:
        print(board)
    print(playing_board)

    n = int(input('Please enter a natural number n. (Enter 0 to quit) '))
