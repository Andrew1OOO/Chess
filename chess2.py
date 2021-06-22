import itertools
import pygame as pg
from pygame import Color, Rect, Surface, sprite
from pygame import transform
from pygame import draw
from pygame import surface
from pygame.constants import BLEND_RGBA_MAX, BLEND_RGB_MAX, BUTTON_RIGHT, SRCALPHA

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
    
    white_pieces = ["♔", "♙", "♕", "♗", "♘", "♖"]
    black_pieces = ["♚", "♛", "♝", "♞", "♜", "♟︎"]
    i = 1
    j = 1
    k = 1
    l = 1
    vertical_move = "0"
    horizontal_move = "0"
    vertical_move_1 = "0"
    horizontal_move_1 = "0"
    end = False
    
    '''if(piece == "♙"):
        if(origin[0]+1 <= 7):
            if(board[origin[0]+1][origin[1]] == "0"):
                v_moves.append((origin[0]+1,origin[1]))
                if(origin[0] == 6):
                    v_moves.append((origin[0]+2,origin[1])) #TODO: make sure this is only for the first move
            if(origin[1]+1 <= 7):
                if board[origin[0]+1][origin[1]+1] != "0" and board[origin[0]+1][origin[1]+1] not in white_pieces:
                    v_moves.append((origin[0]+1,origin[1]+1))
            if(origin[1]-1 >= 0):
                if board[origin[0]+1][origin[1]-1] != "0" and origin[1]-1 >= 0 and board[origin[0]+1][origin[1]-1] not in white_pieces:
                    v_moves.append((origin[0]+1,origin[1]-1))'''
        
    
    if(piece == "♟︎" or piece == "♙"):
            if(origin[0]-1 >= 0):
                if(board[origin[0]-1][origin[1]] == "0"):
                    v_moves.append((origin[0]-1,origin[1]))
                try:
                    if board[origin[0]-1][origin[1]+1] != "0" and origin[1]+1 <= 7 and origin[0]-1 >= 0 and board[origin[0]-1][origin[1]+1]:
                        v_moves.append((origin[0]-1,origin[1]+1))
                except:
                    pass
            
            if(origin[0]-2 >= 0):
                if(board[origin[0]-2][origin[1]] == "0"):
                    if(origin[0] == 6):
                        v_moves.append((origin[0]-2,origin[1]))
            if board[origin[0]-1][origin[1]-1] != "0" and origin[1]-1 >= 0 and origin[0]-1 >= 0 and board[origin[0]-1][origin[1]-1]:
                v_moves.append((origin[0]-1,origin[1]-1))
    
    if(piece == "♖" or piece == "♜" or piece == "♕" or piece == "♛"):
            while(vertical_move == "0" and origin[0]+i <= 7): 
                vertical_move = board[origin[0]+i][origin[1]]
                if(vertical_move != "0"):
                    end = True
                if(piece == "♖" or piece == "♕"):
                    if vertical_move == "0" or end and vertical_move not in white_pieces:
                        v_moves.append((origin[0]+i,origin[1]))
                if(piece == "♜" or piece == "♛"):
                    if vertical_move == "0" or end and vertical_move not in black_pieces:
                        v_moves.append((origin[0]+i,origin[1]))
                if(end):
                    break
                i += 1
            end = False
            while((vertical_move_1 == "0") and origin[0]-k >= 0): 
                #print(str(board[origin[0]-k][origin[1]]) + "- " +str((origin[0]-k,origin[1])))
                vertical_move_1 = board[origin[0]-k][origin[1]]
                if(vertical_move_1 != "0"):
                    end = True
                if(piece == "♖" or piece == "♕"):
                    if vertical_move_1 == "0" or end and vertical_move_1 not in white_pieces:
                        v_moves.append((origin[0]-k,origin[1]))
                if(piece == "♜" or piece == "♛"):
                    if vertical_move_1 == "0" or end and vertical_move_1 not in black_pieces:
                        v_moves.append((origin[0]-k,origin[1]))
                if(end):
                    break
                k += 1
            end = False
            while((horizontal_move == "0") and origin[1]+j <= 7):
                horizontal_move = board[origin[0]][origin[1]+j]
                if(horizontal_move != "0"):
                    end = True
                if(piece == "♖" or piece == "♕"):
                    if horizontal_move == "0" or end and horizontal_move not in white_pieces:
                        v_moves.append((origin[0],origin[1]+j))
                if(piece == "♜" or piece == "♛"):
                    if horizontal_move == "0" or end and horizontal_move not in black_pieces:
                        v_moves.append((origin[0],origin[1]+j))
                if(end):
                    break
                j += 1
            end = False
            while(origin[1]-l >= 0 and (horizontal_move_1 == "0")):
                horizontal_move_1 = board[origin[0]][origin[1]-l]
                if(horizontal_move_1 != "0"):
                    end = True
                if(piece == "♖" or piece == "♕"):
                    if horizontal_move_1 == "0" or end and horizontal_move_1 not in white_pieces:
                        v_moves.append((origin[0],origin[1]-l))
                if(piece == "♜" or piece == "♛"):
                    if horizontal_move_1 == "0" or end and horizontal_move_1 not in black_pieces:
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
            if(piece == "♗" or piece == "♕"):
                if left_move_up == "0" or end and left_move_up not in white_pieces:
                    v_moves.append((origin[0]+i,origin[1]-i))
            if(piece == "♝" or piece == "♛"):
                if left_move_up == "0" or end and left_move_up not in black_pieces:
                    v_moves.append((origin[0]+i,origin[1]-i))
            i += 1
            if(end):
                break

        end = False
        while((left_move_down != "♔" and left_move_down != "♚") and k <= 7 and origin[1]-k >= 0 and origin[0]-k >= 0): 
            left_move_down = board[origin[0]-k][origin[1]-k]
            if(left_move_down != "0"):
                end = True
            if(piece == "♗" or piece == "♕"):
                if left_move_down == "0" or end and left_move_down not in white_pieces:
                    v_moves.append((origin[0]-k,origin[1]-k))
            if(piece == "♝" or piece == "♛"):
                if left_move_down == "0" or end and left_move_down not in black_pieces:
                    v_moves.append((origin[0]-k,origin[1]-k))
            k += 1
            if(end):
                break

        end = False
        while((right_move_up != "♔" and right_move_up != "♚") and origin[0]+j <= 7 and origin[1]+j <= 7):
            right_move_up = board[origin[0]+j][origin[1]+j]
            if(right_move_up != "0"):
                end = True
            if(piece == "♗" or piece == "♕"):
                if (right_move_up == "0" or end) and right_move_up not in white_pieces:
                    v_moves.append((origin[0]+j,origin[1]+j))
            
            if(piece == "♝" or piece == "♛"):
                if (right_move_up == "0" or end) and right_move_up not in black_pieces:
                    v_moves.append((origin[0]+j,origin[1]+j)) 
            j += 1
            if(end):
                break

        end = False
        while((right_move_down != "♔" and right_move_down != "♚") and origin[0]-l > -1 and origin[1]+l <= 7):
            right_move_down = board[origin[0]-l][origin[1]+l]
            if(right_move_down != "0"):
                end = True
            if(piece == "♗" or piece == "♕"):
                if right_move_down == "0" or end and right_move_down not in white_pieces:
                    v_moves.append((origin[0]-l,origin[1]+l))
            if(piece == "♝" or piece == "♛"):
                if right_move_down == "0" or end and right_move_down not in black_pieces:
                    v_moves.append((origin[0]-l,origin[1]+l))
            l += 1
            if(end):
                break

            
    if(piece == "♘" or piece == "♞"):
        moves = [(origin[0]+2,origin[1]+1),(origin[0]+1,origin[1]+2),(origin[0]+2,origin[1]-1),(origin[0]+1,origin[1]-2),(origin[0]-2,origin[1]+1),(origin[0]-1,origin[1]+2),(origin[0]-2,origin[1]-1),(origin[0]-1,origin[1]-2)]
        for o in range(len(moves)):
            try:
                if(piece == "♘"):
                    if(moves[o][0] <=7 and moves[o][0] >= 0 and moves[o][1] <=7 and moves[o][1] >= 0 and board[moves[o][0]][moves[o][1]] not in white_pieces):
                        v_moves.append(moves[o])
                if(piece == "♞"):
                    if(moves[o][0] <=7 and moves[o][0] >= 0 and moves[o][1] <=7 and moves[o][1] >= 0 and board[moves[o][0]][moves[o][1]] not in black_pieces):
                        v_moves.append(moves[o])
            except(IndexError):
                pass

    if(piece == "♔" or piece == "♚"):
        moves = [(origin[0]+1, origin[1]), (origin[0]+1, origin[1]+1),(origin[0]+1, origin[1]-1), (origin[0], origin[1]-1), (origin[0], origin[1]+1), (origin[0]-1, origin[1]), (origin[0]-1, origin[1]-1), (origin[0]-1, origin[1]+1)]
        for g in range(len(moves)):
            
            try:
                if(piece == "♔"):
                    if(moves[g][0] <=7 and moves[g][0] >= 0 and moves[g][1] <=7 and moves[g][1] >= 0 and board[moves[g][0]][moves[g][1]] not in white_pieces):
                        v_moves.append(moves[g])
                if(piece == "♚"):
                    if(moves[g][0] <=7 and moves[g][0] >= 0 and moves[g][1] <=7 and moves[g][1] >= 0 and board[moves[g][0]][moves[g][1]] not in black_pieces):
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

def change_rect_color(position):
    pass
def midpoint(i):
    x = (i[0] + (i[0]+65))/2
    y = (i[1]+ (i[1]+55))/2
    return (int(x),int(y))
def AAfilledRoundedRect(surface,rect,color,radius=0.4):

    """
    AAfilledRoundedRect(surface,rect,color,radius=0.4)

    surface : destination
    rect    : rectangle
    color   : rgb or rgba
    radius  : 0 <= radius <= 1
    """

    rect         = Rect(rect)
    color        = Color(*color)
    alpha        = color.a
    color.a      = 0
    pos          = rect.topleft
    rect.topleft = 0,0
    rectangle    = Surface(rect.size,SRCALPHA)

    circle       = Surface([min(rect.size)*3]*2,SRCALPHA)
    draw.ellipse(circle,(0,0,0),circle.get_rect(),0)
    circle       = transform.smoothscale(circle,[int(min(rect.size)*radius)]*2)

    radius              = rectangle.blit(circle,(0,0))
    radius.bottomright  = rect.bottomright
    rectangle.blit(circle,radius)
    radius.topright     = rect.topright
    rectangle.blit(circle,radius)
    radius.bottomleft   = rect.bottomleft
    rectangle.blit(circle,radius)

    rectangle.fill((0,0,0),rect.inflate(-radius.w,0))
    rectangle.fill((0,0,0),rect.inflate(0,-radius.h))

    rectangle.fill(color,special_flags=BLEND_RGBA_MAX)
    rectangle.fill((255,255,255,alpha),special_flags=BLEND_RGBA_MAX)

    return surface.blit(rectangle,pos)
def opposite_color(board,position, color):
    white_pieces = ["♔", "♙", "♕", "♗", "♘", "♖"]
    black_pieces = ["♚", "♛", "♝", "♞", "♜", "♟︎"]
    if(color == "white"):
        if(board[position[0]][position[1]] not in white_pieces):
            return True
        else:
            return False
    elif(color == "black"):
        if(board[position[0]][position[1]] not in black_pieces):
            return True
        else:
            return False
def check(board, position, color):
    '''    if(color == "white"):
        pawn_checkable_positions = [(position[0]+1,position[1]+1), (position[0]+1,position[1]-1)]
        elif(color == "black"):'''
    pawn_checkable_positions = [(position[0]-1,position[1]+1), (position[0]-1,position[1]-1)]
    #adding horizontal moves
    count = 1
    rook_checkable_positions = []
    end = False
    #TODO: when a rook is right next to the king it does not work
    while position[1]+count <= 7 and board[position[0]][position[1] + count] == "0" :
        if(board[position[0]][position[1] + count] != "0"):
            end = True

        rook_checkable_positions.append((position[0],position[1]+count))

        if(end and opposite_color(board, (position[0],position[1]+count), color)):
            rook_checkable_positions.append((position[0],position[1]+count+1))
        count += 1
    end = False
    count = 1
    while position[1]-count >= 0 and board[position[0]][position[1]- count] == "0":
        if(board[position[0]][position[1] - count] != "0"):
            end = True


        rook_checkable_positions.append((position[0],position[1]-count))

        if(end and opposite_color(board, (position[0],position[1]-count), color)):
            rook_checkable_positions.append((position[0],position[1]-count+1))

        count += 1
    #vertical moves
    count = 1
    end = False
    while position[0]-count >= 0 and board[position[0]-count][position[1]] == "0":
        if(board[position[0]-count][position[1]] != "0"):
            end = True


        rook_checkable_positions.append((position[0]-count,position[1]))
        


        if(end and opposite_color(board, (position[0]-count,position[1]), color)):
            rook_checkable_positions.append((position[0]-count+1,position[1]))
        count += 1
    end = False
    count = 1
    while position[0]+count <= 7 and board[position[0]+count][position[1]] == "0":
        if(board[position[0]+count][position[1]] != "0"):
            end = True

        rook_checkable_positions.append((position[0]+count,position[1]))
        
        if(end and opposite_color(board, (position[0]+count,position[1]), color)):
            rook_checkable_positions.append((position[0]+count+1,position[1]))
        count += 1
    
    #diagonal movement
    end = False
    count = 1
    bish_checkable_positions = []
    while position[1]+count <= 7 and position[0]+count <= 7 and board[position[0]+count][position[1]+count] != "♔" and board[position[0]+count][position[1]+count] != "♚": 
        if(board[position[0]+count][position[1] + count] != "0"):
            end = True
        if(board[position[0]+count][position[1] + count] == "0" or (end and opposite_color(board, (position[0]+count,position[1]+count), color))):
            bish_checkable_positions.append((position[0]+count,position[1]+count))

        if(end):
            break
        count += 1
    end = False
    count = 1
    while position[1]+count <= 7 and position[0]-count >= 0 and board[position[0]-count][position[1]+count] != "♔" and board[position[0]-count][position[1]+count] != "♚":
        if(board[position[0]-count][position[1] + count] != "0"):
            end = True
        if(board[position[0]-count][position[1] + count] == "0" or (end and opposite_color(board, (position[0]-count,position[1]+count), color))):
            bish_checkable_positions.append((position[0]-count,position[1]+count))

        if(end):
            break
        count += 1
    end = False
    count = 1
    while position[1]-count >= 0 and position[0]+count <= 7 and board[position[0]+count][position[1]-count] != "♔" and board[position[0]+count][position[1]-count] != "♚":
        if(board[position[0]+count][position[1] - count] != "0"):
            end = True
        if(board[position[0]+count][position[1] - count] == "0" or (end and opposite_color(board, (position[0]+count,position[1]-count), color))):
            bish_checkable_positions.append((position[0]+count,position[1]-count))

        if(end):
            break

        count += 1
    end = False
    count = 1
    while position[1]-count >= 0 and position[0]-count >= 0 and board[position[0]-count][position[1]-count] != "♔" and board[position[0]-count][position[1]-count] != "♚":
        if(board[position[0]-count][position[1] - count] != "0"):
            end = True
        if(board[position[0]-count][position[1]-count] == "0" or (end and opposite_color(board, (position[0]-count,position[1]-count), color))):
            bish_checkable_positions.append((position[0]-count,position[1]-count))

        if(end):
            break

        count += 1

    
    horse_checkable_positions = [(position[0]+2,position[1]+1),(position[0]+1,position[1]+2),(position[0]+2,position[1]-1),(position[0]+1,position[1]-2),(position[0]-2,position[1]+1),(position[0]-1,position[1]+2),(position[0]-2,position[1]-1),(position[0]-1,position[1]-2)]
    list2 = []
    for o in range(len(horse_checkable_positions)):
        if((horse_checkable_positions[o][0] <=7 and horse_checkable_positions[o][0] >= 0) and (horse_checkable_positions[o][1] <=7 and horse_checkable_positions[o][1] >= 0)):
            
            list2.append(horse_checkable_positions[o])

    horse_checkable_positions = list2
    
    for x in range(len(rook_checkable_positions)):
        
        if(color == "white" and (board[rook_checkable_positions[x][0]][rook_checkable_positions[x][1]] =="♜" or board[rook_checkable_positions[x][0]][rook_checkable_positions[x][1]] == "♛")):
            return rook_checkable_positions, True
        elif(color == "black" and (board[rook_checkable_positions[x][0]][rook_checkable_positions[x][1]] == "♖" or board[rook_checkable_positions[x][0]][rook_checkable_positions[x][1]] == "♕")):
            return rook_checkable_positions, True
    
    for k in range(len(bish_checkable_positions)):
        if(color == "white" and (board[bish_checkable_positions[k][0]][bish_checkable_positions[k][1]] == "♝" or board[bish_checkable_positions[k][0]][bish_checkable_positions[k][1]] == "♛")):
            return bish_checkable_positions, True
        elif(color == "black" and (board[bish_checkable_positions[k][0]][bish_checkable_positions[k][1]] == "♗" or board[bish_checkable_positions[k][0]][bish_checkable_positions[k][1]] == "♕")):
            return bish_checkable_positions, True
    for z in range(len(horse_checkable_positions)):
        if(color == "white" and (board[horse_checkable_positions[z][0]][horse_checkable_positions[z][1]] == "♞")):
            
            return horse_checkable_positions, True
        elif(color == "black" and (board[horse_checkable_positions[z][0]][horse_checkable_positions[z][1]] == "♘")):
            return horse_checkable_positions, True
    for i in range(len(pawn_checkable_positions)):

        if(color == "white" and (board[pawn_checkable_positions[i][0]][pawn_checkable_positions[i][1]] == "♟︎")):
            return pawn_checkable_positions, True
        elif(color == "black" and (board[pawn_checkable_positions[i][0]][pawn_checkable_positions[i][1]] == "♙")):
            return pawn_checkable_positions, True
    return [], False

def same_color(board,position, color):
    white_pieces = ["♔", "♙", "♕", "♗", "♘", "♖"]
    black_pieces = ["♚", "♛", "♝", "♞", "♜", "♟︎"]
    if(color == "white"):
        if(board[position[0]][position[1]] in white_pieces):
            return True
        else:
            return False
    elif(color == "black"):
        if(board[position[0]][position[1]] in black_pieces):
            return True
        else:
            return False

def find(board, x):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(board[i][j]==x):
                return (i,j)
def piece_taken(board, x, color):
    f = []
    pieces = []
    print(x)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(board[i][j] != "0" and same_color(board, (i,j), color)):
                z = find_all_moves(board, (i,j))
                for k in range(len(z)):
                    if(z[k] in x):
                        f.append(z[k])
                        pieces.append((i,j))
    return f == [], f

def count(board):
    white_pieces = ["♔", "♙", "♕", "♗", "♘", "♖"]
    black_pieces = ["♚", "♛", "♝", "♞", "♜", "♟︎"]
    wcount = 0
    bcount = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(board[i][j] in white_pieces):
                wcount += 1
            if(board[i][j] in black_pieces):
                bcount += 1
    return (wcount,bcount)

def flip(arr):
    rows = len(arr)-1
    col = len(arr[0]) -1 
    temp = 0
    for i in range(0, rows):
        if(i < (rows-1) - i):
            for j in range(0,col):
                temp = arr[i][j]
                arr[i][j] = arr[(rows-1)-i][j]
                arr[(rows-1)-i][j] = temp
            
        else:
            break
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

board = create(8)
put_pieces(board)
pg.init()

BLACK = (232, 235, 239)
WHITE = (125, 135, 150)

Font=pg.font.SysFont('Corbel',  15)

letter1=Font.render("a", False, (0,0,0))
letter2=Font.render("b", False, (0,0,0))
letter3=Font.render("c", False, (0,0,0))
letter4=Font.render("d", False, (0,0,0))
letter5=Font.render("e", False, (0,0,0))
letter6=Font.render("f", False, (0,0,0))
letter7=Font.render("g", False, (0,0,0))
letter8=Font.render("h", False, (0,0,0))

number1=Font.render("1", False, (0,0,0))
number2=Font.render("2", False, (0,0,0))
number3=Font.render("3", False, (0,0,0))
number4=Font.render("4", False, (0,0,0))
number5=Font.render("5", False, (0,0,0))
number6=Font.render("6", False, (0,0,0))
number7=Font.render("7", False, (0,0,0))
number8=Font.render("8", False, (0,0,0))



screen = pg.display.set_mode((680, 680))
clock = pg.time.Clock()

colors = itertools.cycle((WHITE, BLACK))
tile_size = 60
width, height = 8*tile_size, 8*tile_size
background = pg.Surface((width, height))
x = count(board)
count1=Font.render("White Pieces - " + str(x[0]), False, (0,0,0))
count2=Font.render("Black Pieces - " + str(x[1]), False, (0,0,0))
check_list = []
list2 = []
for y in range(0, height, tile_size):
    for x in range(0, width, tile_size):
        rect = (x, y, tile_size, tile_size)
        #if((x,y) == (0,0)):
            #pg.draw.rect(background, next(colors), rect,  2, 3)
            #AAfilledRoundedRect(background,rect,next(colors), 1)
        #else:
        pg.draw.rect(background, next(colors), rect)
    next(colors)

game_exit = False
origin1 = (0,0)
v_moves = []
force_move_w = False
force_move_b = False
move = False
while not game_exit:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_exit = True
        if not force_move_w and not force_move_b:
            if event.type == pg.MOUSEBUTTONDOWN:
                if(event.button == 1):
                    pos = pg.mouse.get_pos()
                    print(pos)
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
                        move = True
        elif(force_move_w):
            if event.type == pg.MOUSEBUTTONDOWN:
                if(event.button == 1):
                    pos = pg.mouse.get_pos()
                    origin = encrypt(pos)
                    if(board[origin[0]][origin[1]] == "♔" or board[origin[0]][origin[1]] == "♚" or piece_taken(board, check_list,"white")):
                        origin1 = origin
                        list1 = find_all_moves(board, origin)
                        x, only_allow = piece_taken(board, check_list,"white")
                        v_moves = intersection(list1, only_allow)
                    else:
                        print("Checkmate")
                        game_exit = True
                elif(event.button == 3):
                    pos2 = pg.mouse.get_pos()
                    move = encrypt(pos2)
                    if(move in v_moves):
                        board[move[0]][move[1]] = board[origin1[0]][origin1[1]] 
                        board[origin1[0]][origin1[1]] = "0"
                        move = True
                    force_move_w = False
        elif(force_move_b):
            if event.type == pg.MOUSEBUTTONDOWN:
                if(event.button == 1):
                    pos = pg.mouse.get_pos()
                    origin = encrypt(pos)
                    if(board[origin[0]][origin[1]] == "♔" or board[origin[0]][origin[1]] == "♚" or piece_taken(board, check_list,"black")):
                        origin1 = origin
                        list1 = find_all_moves(board, origin)
                        x, only_allow = piece_taken(board, check_list,"black")
                        v_moves = intersection(list1, only_allow)
                    else:
                        print("Checkmate")
                        game_exit = True
                elif(event.button == 3):
                    pos2 = pg.mouse.get_pos()
                    move = encrypt(pos2)
                    if(move in v_moves):
                        board[move[0]][move[1]] = board[origin1[0]][origin1[1]] 
                        board[origin1[0]][origin1[1]] = "0"
                        move = True
                    force_move_w = False


    screen.fill((0 ,74, 158))

    screen.blit(background, (100, 100))

    background.blit(letter1, (5, 0))
    background.blit(letter2, (65, 0))
    background.blit(letter3, (125, 0))
    background.blit(letter4, (185, 0))
    background.blit(letter5, (245, 0))
    background.blit(letter6, (305, 0))
    background.blit(letter7, (365, 0))
    background.blit(letter8, (425, 0))

    background.blit(number8, (470, 40))
    background.blit(number7, (470, 100))
    background.blit(number6, (470, 160))
    background.blit(number5, (470, 220))
    background.blit(number4, (470, 280))
    background.blit(number3, (470, 340))
    background.blit(number2, (470, 400))
    background.blit(number1, (470, 460))


    if(move):
        board.reverse() 
        check_list, wcheck = check(board, find(board, "♔"), "white")
        list2, bcheck = check(board, find(board, "♚"), "black")
        x = count(board)
        count1=Font.render("Black Pieces - " + str(x[0]), False, (0,0,0))
        count2=Font.render("White Pieces - " + str(x[1]), False, (0,0,0))
        
        if(wcheck):
            print("checks")
            force_move_w = True
            pass
        elif(bcheck):
            print("BLACK CHECK")
            force_move_b = True
        move = False
        v_moves = []
    for i in range(len(v_moves)):
        pg.draw.circle(screen,(86, 182, 194),midpoint(decrypt(v_moves[i][1],v_moves[i][0])),15)
    

    
    screen.blit(count1, (170, 40))
    screen.blit(count2, (410, 40))
        
    paint(board, screen)
    
    pg.display.update()

    pg.display.flip()
    clock.tick(30)

pg.quit()