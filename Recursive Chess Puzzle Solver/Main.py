
board_file = input()
opponent_file = input()

def board_creator(board_file):
    board = [[None for i in range(8)] for j in range(8)]
    board_file_hand = open(board_file, "r")
    board_file_lst = board_file_hand.readlines()
    player_color, all_pieces = board_file_lst[0].strip().upper()[0], board_file_lst[1:]
    for code_loc in all_pieces:
        piece_code, piece_loc = code_loc.split()
        row, column = (8 - int(piece_loc[1])), ord(piece_loc[0]) - ord("a")
        piece = {"color": piece_code[0], "type": piece_code[1], "location": (row, column), "moves": []}
        board[row][column] = piece
    board_file_hand.close()
    return board, player_color



def board_printer(board):
    a = 8
    for row in board:
        print(a, end="  ")
        for column in row:
            if column is not None:
                print(column["color"] + column["type"], end="  ")
            else:
                print("--", end="  ")
        a -= 1
        print()
    lst = []
    for i in range(ord("a"), ord("i")):
        lst.append(chr(i))
    print("   " + "   ".join(lst))
    print()



def opponent_move_list_creator(opponent_file):
    opponent_handle = open(opponent_file, "r")
    opponent_move_lst = opponent_handle.readlines()
    move_lst = []
    for i in range(len(opponent_move_lst)):
        move_lst.append([])
        for j in opponent_move_lst[i].split(","):
            start, end = j[:2], j[3:]
            move_lst[i].append((convert_to_index(start), convert_to_index(end)))
    opponent_handle.close()
    return move_lst



def get_piece(board, loc):
    return board[loc[0]][loc[1]]



def convert_to_index(location):
    return (8 - int(location[1]), ord(location[0]) - ord("a"))



def convert_to_pos(location):
    return str(chr(location[1] + ord("a"))) + str(8 - location[0])



def pawn_moves(board, piece):
    moves = []
    row, col = piece["location"]
    if piece["color"] == "W":
        if 0 <= row - 1 <= 7:
            if not get_piece(board, (row - 1, col)):
                moves.append((row - 1, col))
            if 0 <= col - 1 <= 7:
                if get_piece(board, (row - 1, col - 1)) and get_piece(board, (row - 1, col - 1))["color"] != piece["color"]:
                    moves.append((row - 1, col - 1))
            if 0 <= col + 1 <= 7:
                if get_piece(board, (row - 1, col + 1)) and get_piece(board, (row - 1, col + 1))["color"] != piece["color"]:
                    moves.append((row - 1, col + 1))
    else:
        if 0 <= row + 1 <= 7:
            if not get_piece(board, (row + 1, col)):
                moves.append((row + 1, col))
            if 0 <= col - 1 <= 7:
                if get_piece(board, (row + 1, col - 1)) and get_piece(board, (row + 1, col - 1))["color"] != piece["color"]:
                    moves.append((row + 1, col - 1))
            if 0 <= col + 1 <= 7:
                if get_piece(board, (row + 1, col + 1)) and get_piece(board, (row + 1, col + 1))["color"] != piece["color"]:
                    moves.append((row + 1, col + 1))
    piece["moves"] = moves



def knight_moves(board, piece):
    moves = []
    row, col = piece["location"]
    for r in range(-2, 3):
        for c in range(-2, 3):
            if r ** 2 + c ** 2 == 5 and 0 <= row + r <= 7 and 0 <= col + c <= 7:
                if not get_piece(board, (row + r, col + c)) or get_piece(board, (row + r, col + c))["color"] != piece["color"]:
                    moves.append((row + r, col + c))
    piece["moves"] = moves



def rook_moves(board, piece):
    moves = []
    row, col = piece["location"]
    for i in range(row + 1, 8):
        if get_piece(board, (i, col)):
            if get_piece(board, (i, col))["color"] != piece["color"]:
                moves.append((i, col))
            break
        moves.append((i, col))
    for i in range(row - 1, -1, -1):
        if get_piece(board, (i, col)):
            if get_piece(board, (i, col))["color"] != piece["color"]:
                moves.append((i, col))
            break
        moves.append((i, col))
    for i in range(col + 1, 8):
        if get_piece(board, (row, i)):
            if get_piece(board, (row, i))["color"] != piece["color"]:
                moves.append((row, i))
            break
        moves.append((row, i))
    for i in range(col - 1, -1, -1):
        if get_piece(board, (row, i)):
            if get_piece(board, (row, i))["color"] != piece["color"]:
                moves.append((row, i))
            break
        moves.append((row, i))
    piece["moves"] = moves



def bishop_moves(board, piece):
    moves = []
    row, col = piece["location"]
    for i in range(1, 8):
        if not 0 <= row + i <= 7 or not 0 <= col + i <= 7:
            break
        if get_piece(board, (row + i, col + i)):
            if get_piece(board, (row + i, col + i))["color"] != piece["color"]:
                moves.append((row + i, col + i))
            break
        moves.append((row + i, col + i))
    for i in range(1, 8):
        if not 0 <= row - i <= 7 or not 0 <= col - i <= 7:
            break
        if get_piece(board, (row - i, col - i)):
            if get_piece(board, (row - i, col - i))["color"] != piece["color"]:
                moves.append((row - i, col - i))
            break
        moves.append((row - i, col - i))
    for i in range(1, 8):
        if not 0 <= row + i <= 7 or not 0 <= col - i <= 7:
            break
        if get_piece(board, (row + i, col - i)):
            if get_piece(board, (row + i, col - i))["color"] != piece["color"]:
                moves.append((row + i, col - i))
            break
        moves.append((row + i, col - i))
    for i in range(1, 8):
        if not 0 <= row - i <= 7 or not 0 <= col + i <= 7:
            break
        if get_piece(board, (row - i, col + i)):
            if get_piece(board, (row - i, col + i))["color"] != piece["color"]:
                moves.append((row - i, col + i))
            break
        moves.append((row - i, col + i))
    piece["moves"] = moves



def queen_moves(board, piece):
    rook_moves(board, piece)
    rook_moves_lst = piece["moves"]
    bishop_moves(board, piece)
    bishop_moves_lst = piece["moves"]
    piece["moves"] = rook_moves_lst + bishop_moves_lst



def king_moves(board, piece):
    moves = []
    row, col = piece["location"]
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if 0 <= row + i <= 7 and 0 <= col + j <= 7:
                if get_piece(board, (row + i, col + j)) and get_piece(board, (row + i, col + j))["color"] == piece["color"]:
                    continue
                moves.append((row + i, col + j))
    piece["moves"] = moves



def all_moves(board, player_color):
    player_moves_lst = []
    opponent_moves_lst = []
    for row in range(8):
        for col in range(8):
            piece = get_piece(board, (row, col))
            if piece:
                if piece["type"] == "P":
                    pawn_moves(board, piece)
                elif piece["type"] == "N":
                    knight_moves(board, piece)
                elif piece["type"] == "R":
                    rook_moves(board, piece)
                elif piece["type"] == "B":
                    bishop_moves(board, piece)
                elif piece["type"] == "Q":
                    queen_moves(board, piece)
                elif piece["type"] == "K":
                    king_moves(board, piece)

                if piece["color"] == player_color:
                    for moves in piece["moves"]:
                        player_moves_lst.append((piece["location"], moves))
                else:
                    for moves in piece["moves"]:
                        opponent_moves_lst.append((piece["location"], moves))
    return player_moves_lst, opponent_moves_lst



def make_move(board, move):
    start_pos, target_pos = move
    piece = get_piece(board, start_pos)
    piece["location"] = target_pos
    board[target_pos[0]][target_pos[1]] = piece
    board[start_pos[0]][start_pos[1]] = None



def copy_board(board):
    new_board = []
    for row in board:
        new_row = []
        for piece in row:
            if piece:
                new_piece = {"color": piece["color"], "type": piece["type"], "location": piece["location"], "moves": piece["moves"]}
                new_row.append(new_piece)
            else:
                new_row.append(None)
        new_board.append(new_row)
    return new_board



def check(board, player_color):
    player_moves_lst, opponent_moves_lst = all_moves(board, player_color)
    for move in player_moves_lst:
        start, target = move[0], move[1]
        piece = get_piece(board, target)
        if piece and piece["type"] == "K":
            return True
    return False



def valid_op_moves(board, player_color):
    player_moves_lst, opponent_moves_lst = all_moves(board, player_color)
    valid_moves = []
    for move in opponent_moves_lst:
        new_board = copy_board(board)
        make_move(new_board, move)
        if not check(new_board, player_color):
            valid_moves.append(move)
    return valid_moves



def compare_lists(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    for move in lst1:
        if move not in lst2:
            return False
    return True



def solve(board, player_color, true_op_moves, solution=None):
    if solution is None:
        solution = []
    player_moves_lst, opponent_moves_lst = all_moves(board, player_color)
    for move in player_moves_lst:
        new_board = copy_board(board)
        make_move(new_board, move)
        valid_opponent_moves = valid_op_moves(new_board, player_color)
        if not true_op_moves:
            if not valid_opponent_moves:
                start, target = move
                board_printer(new_board)
                return solution + [move]
        elif compare_lists(true_op_moves[0], valid_opponent_moves):
            start, target = move

            make_move(new_board, true_op_moves[0][0])
            start, target = true_op_moves[0][0]

            sol = solve(new_board, player_color, true_op_moves[1:], solution=solution + [move])
            if sol:
                return sol


board, player_color = board_creator(board_file)
true_op_moves = opponent_move_list_creator(opponent_file)
board_printer(board)


solution = solve(board, player_color, true_op_moves)

for i in solution:
    start, target = i
    print(convert_to_pos(start), convert_to_pos(target))



# separator	Main.py_2_false.txt
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

