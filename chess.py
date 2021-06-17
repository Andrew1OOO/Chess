
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\u001b[0m'
    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''


def create(size):
    board = []
    x = []
    count = 0
    count2 = 0
    for row in range(size):
        if(count2 % 2 == 1):
            count = 1
        else:
            count = 0
        count2 += 1
        for col in range(size):
            if count % 2 == 0:
                x.append("□ ")
            else:
                x.append("■ ")
            count += 1
        board.append(x)
        x = []
    return board

def print_b(board):
    list1 = [3,4,5,6]
    print(f"{bcolors.BOLD}  A|B|C|D|E|F|G|H{bcolors.ENDC}")
    for i in range(len(board)):
        print(bcolors.BOLD + str(i+1) + "|", bcolors.ENDC, *board[i], sep='')

def repaint(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            
            if('\033[95m' in board[i][j]):
                board[i][j] = board[i][j].replace('\033[95m',"").replace('\033[0m',"")
    
def put_pieces(board):

    for i in range(len(board)):
        for j in range(len(board[0])):
            if(i == 1):
                board[i][j] = bcolors.OKCYAN + "♙ " + bcolors.ENDC
            if(i == 6):
                board[i][j] = bcolors.OKGREEN + "♟︎ " + bcolors.ENDC
    king_col = (3,4)
    bis_col = (2,5)
    kn_col = (1,6)
    roo_col = (0,7)

    board[0][king_col[0]] = bcolors.OKCYAN + "♔ " + bcolors.ENDC
    board[0][king_col[1]] = bcolors.OKCYAN + "♕ " + bcolors.ENDC
    board[0][bis_col[0]] = bcolors.OKCYAN + "♗ " + bcolors.ENDC
    board[0][bis_col[1]] = bcolors.OKCYAN + "♗ " + bcolors.ENDC
    board[0][kn_col[0]] = bcolors.OKCYAN + "♘ " + bcolors.ENDC
    board[0][kn_col[1]] = bcolors.OKCYAN + "♘ " + bcolors.ENDC
    board[0][roo_col[0]] = bcolors.OKCYAN + "♖ " + bcolors.ENDC
    board[0][roo_col[1]] = bcolors.OKCYAN + "♖ " + bcolors.ENDC

    board[7][king_col[1]] = bcolors.OKGREEN + "♚ " + bcolors.ENDC
    board[7][king_col[0]] = bcolors.OKGREEN + "♛ " + bcolors.ENDC
    board[7][bis_col[0]] = bcolors.OKGREEN + "♝ " + bcolors.ENDC
    board[7][bis_col[1]] = bcolors.OKGREEN + "♝ " + bcolors.ENDC
    board[7][kn_col[0]] = bcolors.OKGREEN + "♞ " + bcolors.ENDC
    board[7][kn_col[1]] = bcolors.OKGREEN + "♞ " + bcolors.ENDC
    board[7][roo_col[0]] = bcolors.OKGREEN + "♜ " + bcolors.ENDC
    board[7][roo_col[1]] = bcolors.OKGREEN + "♜ " + bcolors.ENDC

def move_piece(board, piece, move, p_moves):
    piece1, move1 = encrypt(board, piece, move)
    print(p_moves)
    col = int(piece1[1])+1
    origin_point = 8*int(piece1[0]+1) - (8-col)
    if(tuple(move1) in p_moves):
        moving = board[piece1[0]][piece1[1]]
        print("moving - " + str(moving))
        if((int(piece1[0])+1) % 2 != 0):
            if(origin_point % 2 == 0):
                board[piece1[0]][piece1[1]] = "■ "
            else:
                board[piece1[0]][piece1[1]] = "□ "
        elif((int(piece1[0])+1) % 2 == 0):
            
            if(origin_point % 2 == 0):
                board[piece1[0]][piece1[1]] = "□ "
            else:
                board[piece1[0]][piece1[1]] = "■ "
        board[move1[0]][move1[1]] = moving
    else:
        print("\nnot a valid move")
def find_all_moves(board, origin):
    v_moves = []
    piece = board[origin[0]][origin[1]]
    
    
    i = 1
    j = 1
    k = 1
    l = 1
    vertical_move = "□ "
    horizontal_move = "□ "
    vertical_move_1 = "□ "
    horizontal_move_1 = "□ "
    
    if(piece == bcolors.OKCYAN + "♙ " + bcolors.ENDC):
        try:
            v_moves.append((origin[0]+1,origin[1]))
            v_moves.append((origin[0]+2,origin[1])) #TODO: make sure this is only for the first move
            if board[origin[0]+1][origin[1]+1] != "□ " and board[origin[0]+1][origin[1]+1] != "■ ":
                v_moves.append((origin[0]+1,origin[1]+1))
            if board[origin[0]+1][origin[1]-1] != "□ " and board[origin[0]+1][origin[1]-1] != "■ " and origin[1]-1 >= 0:
                v_moves.append((origin[0]+1,origin[1]-1))
        except(IndexError):
            print("index error")
            pass
    
    if(piece == bcolors.OKGREEN + "♟︎ " + bcolors.ENDC):

        try:
            
            if(origin[0]-1 >= 0):
                v_moves.append((origin[0]-1,origin[1]))
                try:
                    if board[origin[0]-1][origin[1]+1] != "□ " and board[origin[0]-1][origin[1]+1] != "■ " and origin[1]+1 <= 7 and origin[0]-1 >= 0:
                        v_moves.append((origin[0]-1,origin[1]+1))
                except:
                    pass
            
            if(origin[0]-2 >= 0):
                v_moves.append((origin[0]-2,origin[1]))
            if board[origin[0]-1][origin[1]-1] != "□ " and board[origin[0]-1][origin[1]-1] != "■ " and origin[1]-1 >= 0 and origin[0]-1 >= 0:
                v_moves.append((origin[0]-1,origin[1]-1))
        except(IndexError):
            print("index error")
            pass
    
    if(piece == bcolors.OKCYAN + "♖ " + bcolors.ENDC or piece == bcolors.OKGREEN + "♜ " + bcolors.ENDC or piece == bcolors.OKCYAN + "♕ " + bcolors.ENDC or piece == bcolors.OKGREEN + "♛ " + bcolors.ENDC):
            print("horizontalklkdfglk;df")
            while((vertical_move == "□ " or vertical_move == "■ ") and origin[0]+i <= 7): 
                vertical_move = board[origin[0]+i][origin[1]]
                if vertical_move == "□ " or vertical_move == "■ ":
                    v_moves.append((origin[0]+i,origin[1]))
                i += 1
            while((vertical_move_1 == "□ " or vertical_move_1 == "■ ") and origin[0]-k <= 7): 
                #print(str(board[origin[0]-k][origin[1]]) + "- " +str((origin[0]-k,origin[1])))
                vertical_move_1 = board[origin[0]-k][origin[1]]
                if vertical_move_1 == "□ " or vertical_move_1 == "■ ":
                    v_moves.append((origin[0]-k,origin[1]))
                k += 1
            while((horizontal_move == "□ " or horizontal_move == "■ ") and origin[1]+j <= 7):
                horizontal_move = board[origin[0]][origin[1]+j]
                if horizontal_move == "□ " or horizontal_move == "■ ":
                    v_moves.append((origin[0],origin[1]+j))
                j += 1
            while(origin[1]-l >= 0 and (horizontal_move_1 == "□ " or horizontal_move_1 == "■ ")):
                horizontal_move_1 = board[origin[0]][origin[1]-l]
                if horizontal_move_1 == "□ " or horizontal_move_1 == "■ ":
                    v_moves.append((origin[0],origin[1]-l))
                l += 1
    if(piece == bcolors.OKCYAN + "♗ " + bcolors.ENDC or piece == bcolors.OKGREEN + "♝ " + bcolors.ENDC or piece == bcolors.OKCYAN + "♕ " + bcolors.ENDC or piece == bcolors.OKGREEN + "♛ " + bcolors.ENDC):
        print("diagonal")
        i = 1
        j = 1
        k = 1
        l = 1
        try:
            left_move_up = board[origin[0]+i][origin[1]-i]
            left_move_down = board[origin[0]-k][origin[1]-k]
            right_move_up = board[origin[0]+j][origin[1]+j]
            right_move_down = board[origin[0]-l][origin[1]+l]
        except:
            left_move_up = "□ "
            left_move_down = "□ "
            right_move_up = "□ "
            right_move_down = "□ "
        end = False
        
        while((left_move_up != "♔ " and left_move_up != "♚ ") and origin[0]+i <= 7 and origin[1]-i >= 0): 
            left_move_up = board[origin[0]+i][origin[1]-i]
            print("LEFTY",left_move_up)
            if(left_move_up != "□ " and left_move_up != "■ "):
                end = True
            if left_move_up == "□ " or left_move_up == "■ " or end == True:
                v_moves.append((origin[0]+i,origin[1]-i))
            i += 1
            if(end):
                break

        end = False
        while((left_move_down != "♔ " and left_move_down != "♚ ") and k <= 7 and origin[1]-k >= 0 and origin[0]-k >= 0): 
            left_move_down = board[origin[0]-k][origin[1]-k]
            if(left_move_down != "□ " and left_move_down != "■ "):
                end = True
            if left_move_down == "□ " or left_move_down == "■ " or end == True:
                v_moves.append((origin[0]-k,origin[1]-k))
            k += 1
            if(end):
                break

        end = False
        while((right_move_up != "♔ " and right_move_up != "♚ ") and origin[0]+j <= 7 and origin[1]+j <= 7):
            right_move_up = board[origin[0]+j][origin[1]+j]
            if(right_move_up != "□ " and right_move_up != "■ "):
                end = True
            if right_move_up == "□ " or right_move_up == "■ "  or end == True:
                print(origin[0]+j,origin[1]+j)
                v_moves.append((origin[0]+j,origin[1]+j))
            j += 1
            if(end):
                break

        end = False
        while((right_move_down != "♔ " and right_move_down != "♚ ") and origin[0]-l > -1 and origin[1]+l <= 7):
            right_move_down = board[origin[0]-l][origin[1]+l]
            if(right_move_down != "□ " and right_move_down != "■ "):
                end = True
            if right_move_down == "□ " or right_move_down == "■ " or end == True:
                v_moves.append((origin[0]-l,origin[1]+l))
            l += 1
            if(end):
                break

            
    if(piece == bcolors.OKCYAN + "♘ " + bcolors.ENDC or piece == bcolors.OKGREEN + "♞ " + bcolors.ENDC):
        moves = [(origin[0]+2,origin[1]+1),(origin[0]+1,origin[1]+2),(origin[0]+2,origin[1]-1),(origin[0]+1,origin[1]-2),(origin[0]-2,origin[1]+1),(origin[0]-1,origin[1]+2),(origin[0]-2,origin[1]-1),(origin[0]-1,origin[1]-2)]
        for o in range(len(moves)):
            try:
                if(moves[o][0] <=7 and moves[o][0] >= 0 and moves[o][1] <=7 and moves[o][1] >= 0 and not same_color(piece, board[moves[o][0]][moves[o][1]])):
                    v_moves.append(moves[o])
            except(IndexError):
                pass

    if(piece == bcolors.OKCYAN + "♔ " + bcolors.ENDC or piece == bcolors.OKGREEN + "♚ " + bcolors.ENDC):
        moves = [(origin[0]+1, origin[1]), (origin[0]+1, origin[1]+1),(origin[0]+1, origin[1]-1), (origin[0], origin[1]-1), (origin[0], origin[1]+1), (origin[0]-1, origin[1]), (origin[0]-1, origin[1]-1), (origin[0]-1, origin[1]-1)]
        for g in range(len(moves)):
            try:
                if(moves[g][0] <=7 and moves[g][0] >= 0 and moves[g][1] <=7 and moves[g][1] >= 0 and not same_color(piece, board[moves[g][0]][moves[g][1]])):
                    v_moves.append(moves[g])
            except(IndexError):
                pass
    #print(move, " - ", v_moves, " - ", move in v_moves)
    return v_moves

def same_color(o_piece, m_piece):
    num = ""
    start = False
    for i in range(len(o_piece)):
        if(o_piece[i] == "m"):
            break
        if(start):
            num += o_piece[i]
        if(o_piece[i] == '['):
            start = True
    num1 = ""
    start = False
    for j in range(len(m_piece)):
        if(m_piece[j] == "m"):
            break
        if(start):
            num1 += m_piece[j]
        if(m_piece[j] == '['):
            start = True
    try:
        return int(num1) == int(num)
    except:
        return False
def encrypt(board,origin, move):
    list1 = ["A","B","C","D","E","F","G","H"]
    origin2 = [0,0]
    move2 = [0,0]
    for i in range(len(list1)):
    
        if(str(split(origin)[0]).upper() == list1[i]):
            origin2[1] = i
        if(str(split(move)[0]).upper() == list1[i]):
            move2[1] = i
    origin2[0] = int(split(origin)[1]) -1
    move2[0] = int(split(move)[1]) - 1

    return origin2, move2

def encrypt_1(origin):
    list1 = ["A","B","C","D","E","F","G","H"]
    origin2 = [0,0]
    
    if(str(split(origin)[0]).upper() in list1):
        origin2[1] = list1.index(str(split(origin)[0]).upper())

    origin2[0] = int(split(origin)[1]) - 1
    
    return origin2

def split(word):
    return [char for char in word]

def game_finished(board, white_king_pos, black_king_pos):
    return False
'''    if(white_check() and find_all_moves(board, white_king_pos) == []):
        return True
    elif(black_check() and find_all_moves(board, black_king_pos) == []):
        return True'''
    
    #TODO: need to check the surrounding squares to see if they are in check, making checkmate instead of seeing if there are no moves
    
def find_wKing(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(board[i][j] == bcolors.OKCYAN + "♔ " + bcolors.ENDC):
                return (i,j)

def find_bKing(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(board[i][j] == bcolors.OKGREEN + "♚ " + bcolors.ENDC):
                return (i,j)

def white_check():
    return False

def black_check():
    return False
board = create(8)
put_pieces(board)
print_b(board)
count = 0
w_king = find_wKing(board)
b_king = find_bKing(board)

while game_finished(board, w_king, b_king) != True:
    if count % 2 == 0:
        origin = input("Blue's turn, What is the origin of your move?")
        e_origin = encrypt_1(origin)
        while('\033[96m' not in board[e_origin[0]][e_origin[1]]):
            origin = input("Blue's turn, not Green's, re-input origin")
            e_origin = encrypt_1(origin)

        list1 = find_all_moves(board, e_origin)
        print("all moves", list1)
        for i in range(len(list1)):
            print(board[list1[i][0]][list1[i][1]])
            board[list1[i][0]][list1[i][1]] = bcolors.HEADER + board[list1[i][0]][list1[i][1]] + bcolors.ENDC
        print_b(board)
        move = input("What move do you want to make?")

        while tuple(encrypt_1(move)) not in list1:
            move = input("Invalid move, input again.")
        move_piece(board,origin,move, list1)
        repaint(board)
        print_b(board)
    else:
        origin = input("Greens turn, what is the origin of your move?")
        e_origin = encrypt_1(origin)
        while('\033[92m' not in board[e_origin[0]][e_origin[1]]):
            origin = input("Green's turn, not Blue's, re-input origin")
            e_origin = encrypt_1(origin)
        list1 = find_all_moves(board, e_origin)
        for i in range(len(list1)):
            board[list1[i][0]][list1[i][1]] = bcolors.HEADER + board[list1[i][0]][list1[i][1]] + bcolors.ENDC
        print_b(board)
        move = input("What move do you want to make?")
        while tuple(encrypt_1(move)) not in list1:
            move = input("Invalid move, input again.")
        move_piece(board,origin,move, list1)
        repaint(board)
        print_b(board)
    count += 1
    


