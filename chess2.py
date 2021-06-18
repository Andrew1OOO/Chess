import itertools
import pygame as pg
from pygame import sprite
from pygame.constants import BUTTON_RIGHT

def create(size):
    board = []
    x = []
    count = 0
    count2 = 0
    for row in range(size):
        for col in range(size):
            x.append("0")
        board.append(x)
        x = []
    return board
def put_pieces(board):

    for i in range(len(board)):
        for j in range(len(board[0])):
            if(i == 1):
                board[i][j] = "♙"
            if(i == 6):
                board[i][j] = "♟︎"
    king_col = (3,4)
    bis_col = (2,5)
    kn_col = (1,6)
    roo_col = (0,7)

    board[0][king_col[0]] = "♔"
    board[0][king_col[1]] ="♕"
    board[0][bis_col[0]] ="♗"
    board[0][bis_col[1]] ="♗"
    board[0][kn_col[0]] = "♘"
    board[0][kn_col[1]] = "♘"
    board[0][roo_col[0]] = "♖" 
    board[0][roo_col[1]] = "♖"
    board[7][king_col[1]] ="♚" 
    board[7][king_col[0]] = "♛"
    board[7][bis_col[0]] = "♝" 
    board[7][bis_col[1]] = "♝" 
    board[7][kn_col[0]] = "♞" 
    board[7][kn_col[1]] ="♞" 
    board[7][roo_col[0]] =  "♜" 
    board[7][roo_col[1]] = "♜" 
def find_all_moves(board, origin):
    v_moves = []
    piece = board[origin[0]][origin[1]]
    
    
    i = 1
    j = 1
    k = 1
    l = 1
    vertical_move = "0"
    horizontal_move = "0"
    vertical_move_1 = "0"
    horizontal_move_1 = "0"
    end = False
    
    if(piece == "♙"):
        try:
            v_moves.append((origin[0]+1,origin[1]))
            v_moves.append((origin[0]+2,origin[1])) #TODO: make sure this is only for the first move
            if board[origin[0]+1][origin[1]+1] != "0":
                v_moves.append((origin[0]+1,origin[1]+1))
            if board[origin[0]+1][origin[1]-1] != "0" and origin[1]-1 >= 0:
                v_moves.append((origin[0]+1,origin[1]-1))
        except(IndexError):
            print("index error")
            pass
    
    if(piece == "♟︎"):

        try:
            
            if(origin[0]-1 >= 0):
                v_moves.append((origin[0]-1,origin[1]))
                try:
                    if board[origin[0]-1][origin[1]+1] != "0" and origin[1]+1 <= 7 and origin[0]-1 >= 0:
                        v_moves.append((origin[0]-1,origin[1]+1))
                except:
                    pass
            
            if(origin[0]-2 >= 0):
                v_moves.append((origin[0]-2,origin[1]))
            if board[origin[0]-1][origin[1]-1] != "0" and origin[1]-1 >= 0 and origin[0]-1 >= 0:
                v_moves.append((origin[0]-1,origin[1]-1))
        except(IndexError):
            print("index error")
            pass
    
    if(piece == "♖" or piece == "♜" or piece == "♕" or piece == "♛"):
            while(vertical_move == "0" and origin[0]+i <= 7): 
                vertical_move = board[origin[0]+i][origin[1]]
                if(vertical_move != "0"):
                    end = True
                if vertical_move == "0" or end:
                    v_moves.append((origin[0]+i,origin[1]))
                if(end):
                    break
                i += 1
            end = False
            while((vertical_move_1 == "0") and origin[0]-k <= 7): 
                #print(str(board[origin[0]-k][origin[1]]) + "- " +str((origin[0]-k,origin[1])))
                vertical_move_1 = board[origin[0]-k][origin[1]]
                if(vertical_move_1 != "0"):
                    end = True
                if vertical_move_1 == "0" or end:
                    v_moves.append((origin[0]-k,origin[1]))
                if(end):
                    break
                k += 1
            end = False
            while((horizontal_move == "0") and origin[1]+j <= 7):
                horizontal_move = board[origin[0]][origin[1]+j]
                if(horizontal_move != "0"):
                    end = True
                if horizontal_move == "0" or end:
                    v_moves.append((origin[0],origin[1]+j))
                if(end):
                    break
                j += 1
            end = False
            while(origin[1]-l >= 0 and (horizontal_move_1 == "0")):
                horizontal_move_1 = board[origin[0]][origin[1]-l]
                if(horizontal_move_1 != "0"):
                    end = True
                if horizontal_move_1 == "0" or end:
                    v_moves.append((origin[0],origin[1]-l))
                if(end):
                    break
                l += 1
    end = False
    if(piece =="♗" or piece == "♝" or piece ==  "♕" or piece == "♛"):
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
            left_move_up = "0"
            left_move_down = "0"
            right_move_up = "0"
            right_move_down = "0"
        end = False
        
        while((left_move_up != "♔" and left_move_up != "♚") and origin[0]+i <= 7 and origin[1]-i >= 0): 
            left_move_up = board[origin[0]+i][origin[1]-i]
            if(left_move_up != "0"):
                end = True
            if left_move_up == "0" or end == True:
                v_moves.append((origin[0]+i,origin[1]-i))
            i += 1
            if(end):
                break

        end = False
        while((left_move_down != "♔" and left_move_down != "♚") and k <= 7 and origin[1]-k >= 0 and origin[0]-k >= 0): 
            left_move_down = board[origin[0]-k][origin[1]-k]
            if(left_move_down != "0"):
                end = True
            if left_move_down == "0" or end == True:
                v_moves.append((origin[0]-k,origin[1]-k))
            k += 1
            if(end):
                break

        end = False
        while((right_move_up != "♔" and right_move_up != "♚") and origin[0]+j <= 7 and origin[1]+j <= 7):
            right_move_up = board[origin[0]+j][origin[1]+j]
            if(right_move_up != "0"):
                end = True
            if right_move_up == "0" or end == True:
                print(origin[0]+j,origin[1]+j)
                v_moves.append((origin[0]+j,origin[1]+j))
            j += 1
            if(end):
                break

        end = False
        while((right_move_down != "♔" and right_move_down != "♚") and origin[0]-l > -1 and origin[1]+l <= 7):
            right_move_down = board[origin[0]-l][origin[1]+l]
            if(right_move_down != "0"):
                end = True
            if right_move_down == "0" or end == True:
                v_moves.append((origin[0]-l,origin[1]+l))
            l += 1
            if(end):
                break

            
    if(piece == "♘" or piece == "♞"):
        moves = [(origin[0]+2,origin[1]+1),(origin[0]+1,origin[1]+2),(origin[0]+2,origin[1]-1),(origin[0]+1,origin[1]-2),(origin[0]-2,origin[1]+1),(origin[0]-1,origin[1]+2),(origin[0]-2,origin[1]-1),(origin[0]-1,origin[1]-2)]
        for o in range(len(moves)):
            try:
                if(moves[o][0] <=7 and moves[o][0] >= 0 and moves[o][1] <=7 and moves[o][1] >= 0):
                    v_moves.append(moves[o])
            except(IndexError):
                pass

    if(piece == "♔" or piece == "♚"):
        moves = [(origin[0]+1, origin[1]), (origin[0]+1, origin[1]+1),(origin[0]+1, origin[1]-1), (origin[0], origin[1]-1), (origin[0], origin[1]+1), (origin[0]-1, origin[1]), (origin[0]-1, origin[1]-1), (origin[0]-1, origin[1]+1)]
        for g in range(len(moves)):
            try:
                if(moves[g][0] <=7 and moves[g][0] >= 0 and moves[g][1] <=7 and moves[g][1] >= 0):
                    v_moves.append(moves[g])
            except(IndexError):
                pass
    #print(move, " - ", v_moves, " - ", move in v_moves)
    return v_moves
def paint(board, screen):
    size = 60

    wpawn = pg.image.load('wpawn.png').convert_alpha()
    wpawn = pg.transform.smoothscale(wpawn, (size, size))

    bpawn = pg.image.load('bpawn.png').convert_alpha()
    bpawn = pg.transform.smoothscale(bpawn, (size, size))  

    wking = pg.image.load('wking.png').convert_alpha()
    wking = pg.transform.smoothscale(wking, (size, size))

    bking = pg.image.load('bking.png').convert_alpha()
    bking = pg.transform.smoothscale(bking, (size, size))

    bqueen = pg.image.load('bqueen.png').convert_alpha()
    bqueen = pg.transform.smoothscale(bqueen, (size, size))

    wqueen = pg.image.load('wqueen.png').convert_alpha()
    wqueen = pg.transform.smoothscale(wqueen, (size, size))
    
    bbishop = pg.image.load('bbishop.png').convert_alpha()
    bbishop = pg.transform.smoothscale(bbishop, (size, size))

    wbishop = pg.image.load('wbishop.png').convert_alpha()
    wbishop = pg.transform.smoothscale(wbishop, (size, size))

    bhorse = pg.image.load('bhorse.png').convert_alpha()
    bhorse = pg.transform.smoothscale(bhorse, (size, size))

    whorse = pg.image.load('whorse.png').convert_alpha()
    whorse = pg.transform.smoothscale(whorse, (size, size))

    wrook = pg.image.load('wrook.png').convert_alpha()
    wrook = pg.transform.smoothscale(wrook, (size, size))

    brook = pg.image.load('brook.png').convert_alpha()
    brook = pg.transform.smoothscale(brook, (size, size))
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(board[i][j] == "♙"):
                screen.blit(wpawn, decrypt(j,i))
            if(board[i][j] == "♟︎"):
                screen.blit(bpawn, decrypt(j,i))
            if(board[i][j] == "♔"):
                screen.blit(wking, decrypt(j,i))
            if(board[i][j] == "♚"):
                screen.blit(bking, decrypt(j,i))
            if(board[i][j] == "♕"):
                screen.blit(wqueen, decrypt(j,i))
            if(board[i][j] == "♛"):
                screen.blit(bqueen, decrypt(j,i))
            if(board[i][j] == "♗"):
                screen.blit(wbishop, decrypt(j,i))
            if(board[i][j] == "♝"):
                screen.blit(bbishop, decrypt(j,i))
            if(board[i][j] == "♞"):
                screen.blit(bhorse, decrypt(j,i))
            if(board[i][j] == "♘"):
                screen.blit(whorse, decrypt(j,i))
            if(board[i][j] == "♖" ):
                screen.blit(wrook, decrypt(j,i))
            if(board[i][j] == "♜"):
                screen.blit(brook, decrypt(j,i))

def encrypt(position):
    start = (100,100)
    size = 60
    for j in range(1,9):
        for i in range(1,9):
            if position[0] <= (start[0]+size*i) and position[1] <= (start[1] + (size*j)) and position[0] > (start[0]+(size*(i-1)) and position[1] > start[1]+size*(j-1)):
                return j-1,i-1
def decrypt(i,j):
    return 97+i*60, 105+j*60

def change_rect_color(board, v_moves):
    pass


board = create(8)
put_pieces(board)
pg.init()

BLACK = pg.Color(100,60,7)
WHITE = pg.Color('white')

screen = pg.display.set_mode((800, 600))
clock = pg.time.Clock()

colors = itertools.cycle((WHITE, BLACK))
tile_size = 60
width, height = 8*tile_size, 8*tile_size
background = pg.Surface((width, height))

for y in range(0, height, tile_size):
    for x in range(0, width, tile_size):
        rect = (x, y, tile_size, tile_size)
        pg.draw.rect(background, next(colors), rect)
    next(colors)

game_exit = False
origin1 = (0,0)
v_moves = []
while not game_exit:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_exit = True
        if event.type == pg.MOUSEBUTTONDOWN:
            if(event.button == 1):
                pos = pg.mouse.get_pos()
                origin = encrypt(pos)
                origin1 = origin
                list1 = find_all_moves(board, origin)
                v_moves = list1
            elif(event.button == 3):
                pos2 = pg.mouse.get_pos()
                move = encrypt(pos2)
                if(move in v_moves):
                    board[move[0]][move[1]] = board[origin1[0]][origin1[1]] 
                    board[origin1[0]][origin1[1]] = "0"

        


    screen.fill((60, 70, 90))

    screen.blit(background, (100, 100))
    paint(board, screen)    

    pg.display.update()

    pg.display.flip()
    clock.tick(30)

pg.quit()