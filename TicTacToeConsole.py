board = ["0", "1", "2",
         "3", "4", "5",
         "6", "7", "8"]

human_player = "x"
comp_player = "o"


def clear_board():
    """This function should clear all fields to str from '0' to '8' """
    for ind in range(9):
        board[ind] = str(ind)


def empty_indexes(board_to_check):
    """This function return fields that are 'free'"""
    return [f for f in board_to_check if f != "x" and f != "o"]


def print_board():
    """Printing formatted board"""
    temp_board = board.copy()
    for ind in range(9):
        if temp_board[ind] != "x" and temp_board[ind] != "o":
            temp_board[ind] = " "
    print(" {}|{}|{}\n--+-+--\n {}|{}|{}\n--+-+--\n {}|{}|{}".format(*temp_board))


def is_win(b, player):
    """This function checks if given player ('x' or 'o') is winner"""
    if (b[0] == b[1] == b[2] == player) or (
            b[3] == b[4] == b[5] == player) or (
            b[6] == b[7] == b[8] == player) or (
            b[0] == b[3] == b[6] == player) or (
            b[1] == b[4] == b[7] == player) or (
            b[2] == b[5] == b[8] == player) or (
            b[0] == b[4] == b[8] == player) or (
            b[2] == b[4] == b[6] == player):
        return True


class Move:
    """Class whose objects are used by minimax as single moves"""
    def __init__(self, index=None, score=None):
        self.index = index
        self.score = score
        self.depth = 0


def minimax(new_board, player):
    """Minimax function, it should find the best possible move and return the best Move object"""
    free_fields = empty_indexes(new_board)

    if is_win(new_board, human_player):
        # case when human win
        temp_move = Move(None, -10)
        return temp_move
    elif is_win(new_board, comp_player):
        # case when comp win
        temp_move = Move(None, 10)
        return temp_move
    elif len(free_fields) == 0:
        # draw
        temp_move = Move(None, 0)
        return temp_move

    # All moves will be stored here:
    moves = []
    
    for i in range(len(free_fields)):
        move = Move()   # create new move
        move.index = new_board[int(free_fields[i])]

        new_board[int(free_fields[i])] = player     # set comp 'o' to board

        # Next iteration of minimax()
        if player == comp_player:
            move.score = minimax(new_board, human_player).score
        else:
            move.score = minimax(new_board, comp_player).score

        # After move and moves after it are processed -> return to current board
        new_board[int(free_fields[i])] = str(move.index)

        moves.append(move)  # add move to moves

    best_move = None
    if player == comp_player:
        # take the move with the best score
        best_score = -9999
        for i in range(len(moves)):
            sc = moves[i].score
            if sc > best_score:
                best_score = moves[i].score
                best_move = i
    else:
        # take the move with the lowest score while its player move
        best_score = 9999
        for i in range(len(moves)):
            sc = moves[i].score
            if sc < best_score:
                best_score = moves[i].score
                best_move = i
    # Function returns Move obj which is the best:
    return moves[best_move]


if __name__ == '__main__':
    print(" {}|{}|{}\n--+-+--\n {}|{}|{}\n--+-+--\n {}|{}|{}".format(*board))
    while True:
        human_move = input("Give your move: ")
        while human_move not in empty_indexes(board):
            human_move = input("Give correct move: ")
        for field in board:
            if human_move == field:
                board[int(field)] = "x"
                print_board()
                break
        if is_win(board, human_player):
            print("YOU WON!!")
            break
        for field in board:
            if minimax(board, comp_player).index == field:
                board[int(field)] = "o"
                print("Computer move is {}". format(field))
                print_board()
                break
        if is_win(board, comp_player):
            print("COMPUTER WON!!")
            break
        if len(empty_indexes(board)) == 0:
            print("DRAW!!")
            break
