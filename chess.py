
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
    for row in range(size):
        for col in range(size):
            x.append(str(0) + " ")
        board.append(x)
        x = []
    return board

def print_b(board):
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
                board[i][j] = bcolors.OKCYAN + "P " + bcolors.ENDC
            if(i == 6):
                board[i][j] = bcolors.OKGREEN + "P " + bcolors.ENDC
    king_col = (3,4)
    bis_col = (2,5)
    kn_col = (1,6)
    roo_col = (0,7)

    board[0][king_col[0]] = bcolors.OKCYAN + "K " + bcolors.ENDC
    board[0][king_col[1]] = bcolors.OKCYAN + "Q " + bcolors.ENDC
    board[0][bis_col[0]] = bcolors.OKCYAN + "B " + bcolors.ENDC
    board[0][bis_col[1]] = bcolors.OKCYAN + "B " + bcolors.ENDC
    board[0][kn_col[0]] = bcolors.OKCYAN + "N " + bcolors.ENDC
    board[0][kn_col[1]] = bcolors.OKCYAN + "N " + bcolors.ENDC
    board[0][roo_col[0]] = bcolors.OKCYAN + "R " + bcolors.ENDC
    board[0][roo_col[1]] = bcolors.OKCYAN + "R " + bcolors.ENDC

    board[7][king_col[1]] = bcolors.OKGREEN + "K " + bcolors.ENDC
    board[7][king_col[0]] = bcolors.OKGREEN + "Q " + bcolors.ENDC
    board[7][bis_col[0]] = bcolors.OKGREEN + "B " + bcolors.ENDC
    board[7][bis_col[1]] = bcolors.OKGREEN + "B " + bcolors.ENDC
    board[7][kn_col[0]] = bcolors.OKGREEN + "N " + bcolors.ENDC
    board[7][kn_col[1]] = bcolors.OKGREEN + "N " + bcolors.ENDC
    board[7][roo_col[0]] = bcolors.OKGREEN + "R " + bcolors.ENDC
    board[7][roo_col[1]] = bcolors.OKGREEN + "R " + bcolors.ENDC

def move_piece(board, piece, move, p_moves):
    piece1, move1 = encrypt(board, piece, move)
    print(p_moves)
    if(tuple(move1) in p_moves):
        moving = board[piece1[0]][piece1[1]]
        print("moving - " + str(moving))
        board[piece1[0]][piece1[1]] = "0 "
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
    vertical_move = "0 "
    horizontal_move = "0 "
    vertical_move_1 = "0 "
    horizontal_move_1 = "0 "
    
    if(piece == bcolors.OKCYAN + "P " + bcolors.ENDC):
        try:
            v_moves.append((origin[0]+1,origin[1]))
            v_moves.append((origin[0]+2,origin[1]))
            if board[origin[0]+1][origin[1]+1] != "0 ":
                v_moves.append((origin[0]+1,origin[1]+1))
            if board[origin[0]+1][origin[1]-1] != "0 " and origin[1]-1 >= 0:
                v_moves.append((origin[0]+1,origin[1]-1))
        except(IndexError):
            print("index error")
            pass
    
    if(piece == bcolors.OKGREEN + "P " + bcolors.ENDC):

        try:
            
            if(origin[0]-1 >= 0):
                v_moves.append((origin[0]-1,origin[1]))
                try:
                    if board[origin[0]-1][origin[1]+1] != "0 " and origin[1]+1 <= 7 and origin[0]-1 >= 0:
                        v_moves.append((origin[0]-1,origin[1]+1))
                except:
                    pass
            
            if(origin[0]-2 >= 0):
                
                v_moves.append((origin[0]-2,origin[1]))
            if board[origin[0]-1][origin[1]-1] != "0 " and origin[1]-1 >= 0 and origin[0]-1 >= 0:
                v_moves.append((origin[0]-1,origin[1]-1))
        except(IndexError):
            print("index error")
            pass
    print("piece ---", str(piece) + "comparison --- ", bcolors.OKCYAN + "Q " + bcolors.ENDC)
    if(piece == bcolors.OKCYAN + "R " + bcolors.ENDC or piece == bcolors.OKGREEN + "R " + bcolors.ENDC or piece == bcolors.OKCYAN + "Q " + bcolors.ENDC or piece == bcolors.OKGREEN + "Q " + bcolors.ENDC):
            print("horizontalklkdfglk;df")
            while(vertical_move == "0 " and origin[0]+i <= 7): 
                vertical_move = board[origin[0]+i][origin[1]]
                if vertical_move == "0 ":
                    v_moves.append((origin[0]+i,origin[1]))
                i += 1
            while(vertical_move_1 == "0 " and origin[0]-k <= 7): 
                #print(str(board[origin[0]-k][origin[1]]) + "- " +str((origin[0]-k,origin[1])))
                vertical_move_1 = board[origin[0]-k][origin[1]]
                if vertical_move_1 == "0 ":
                    v_moves.append((origin[0]-k,origin[1]))
                k += 1
            while(horizontal_move == "0 " and origin[1]+j <= 7):
                horizontal_move = board[origin[0]][origin[1]+j]
                if horizontal_move == "0 ":
                    v_moves.append((origin[0],origin[1]+j))
                j += 1
            while(horizontal_move_1 == "0 " and origin[1]-l >= 0):
                horizontal_move_1 = board[origin[0]][origin[1]-l]
                if horizontal_move_1 == "0 ":
                    v_moves.append((origin[0],origin[1]-l))
                l += 1
    if(piece == bcolors.OKCYAN + "B " + bcolors.ENDC or piece == bcolors.OKGREEN + "B " + bcolors.ENDC or piece == bcolors.OKCYAN + "Q " + bcolors.ENDC or piece == bcolors.OKGREEN + "Q " + bcolors.ENDC):
        print("diagonal")
        left_move_up = "0 "
        left_move_down = "0 "
        right_move_up = "0 "
        right_move_down = "0 "
        i = 1
        j = 1
        k = 1
        l = 1
        while(left_move_up == "0 " and origin[0]+i <= 7 and origin[1]-i >= 0): 
            left_move_up = board[origin[0]+i][origin[1]-i]
            if left_move_up == "0 ":
                v_moves.append((origin[0]+i,origin[1]-i))
            i += 1
        while(left_move_down == "0 " and k <= 7 and origin[1]-k >= 0 and origin[0]-k >= 0): 
            left_move_down = board[origin[0]-k][origin[1]-k]
            if left_move_down == "0 ":
                v_moves.append((origin[0]-k,origin[1]-k))
            k += 1
        while(right_move_up == "0 " and origin[0]+j <= 7 and origin[1]+j <= 7):
            print(right_move_up)
            right_move_up = board[origin[0]+j][origin[1]+j]
            if right_move_up == "0 ":
                v_moves.append((origin[0]+j,origin[1]+j))
            j += 1
        while(right_move_down == "0 " and origin[1]-l >= -1 and origin[1]+l <= 7):
            right_move_down = board[origin[0]-l][origin[1]+l]
            if right_move_down == "0 ":
                v_moves.append((origin[0]-l,origin[1]+l))
            l += 1
    if(piece == bcolors.OKCYAN + "N " + bcolors.ENDC or piece == bcolors.OKGREEN + "N " + bcolors.ENDC):
        moves = [(origin[0]+2,origin[1]+1),(origin[0]+1,origin[1]+2),(origin[0]+2,origin[1]-1),(origin[0]+1,origin[1]-2),(origin[0]-2,origin[1]+1),(origin[0]-1,origin[1]+2),(origin[0]-2,origin[1]-1),(origin[0]-1,origin[1]-2)]
        for o in range(len(moves)):
            try:
                if(moves[o][0] <=7 and moves[o][1] <=7):
                    
                    v_moves.append(moves[o])
            except(IndexError):
                pass
    #print(move, " - ", v_moves, " - ", move in v_moves)
    return v_moves

def encrypt(board,origin, move):
    list1 = ["A","B","C","D","E","F","G","H"]
    origin2 = [0,0]
    move2 = [0,0]
    for i in range(len(list1)):
    
        if(str(split(origin)[0]) == list1[i]):
            origin2[1] = i
        if(str(split(move)[0]) == list1[i]):
            move2[1] = i
    origin2[0] = int(split(origin)[1]) -1
    move2[0] = int(split(move)[1]) - 1

    return origin2, move2

def encrypt_1(origin):
    list1 = ["A","B","C","D","E","F","G","H"]
    origin2 = [0,0]
    for i in range(len(list1)):
    
        if(str(split(origin)[0]) == list1[i]):
            origin2[1] = i
    origin2[0] = int(split(origin)[1]) -1

    return origin2

def split(word):
    return [char for char in word]

def game_finished():
    return False
board = create(8)
put_pieces(board)
print_b(board)
count = 0
while game_finished() != True:
    if count % 2 == 0:
        origin = input("Blue's turn, What is the origin of your move?")
        e_origin = encrypt_1(origin)
        while('\033[96m' not in board[e_origin[0]][e_origin[1]]):
            origin = input("Blue's turn, not Green's, re-input origin")
            e_origin = encrypt_1(origin)

        list1 = find_all_moves(board, e_origin)
        print("all moves", list1)
        for i in range(len(list1)):
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
    

