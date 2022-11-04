import sys
import math
import numpy as np
import pygame
BLUE=(0,0,255)
BLACK=(0,0,0)
YELLOW=(255,255,0)
RED=(139,0,0)
ROW_COUNT=6
COL_COUNT=7

def create_board():
    board=np.zeros((ROW_COUNT,COL_COUNT))
    return  board


#checks if the column has any spotss left
def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0

#Goes to next row when there is no spots in previous one
def next_row(board, col):
    for i in range(ROW_COUNT):
        if board[i][col] == 0:
            return i
#change the orientation of board
def print_board(board):
    print(np.flip(board,0))
#Piece goes to selected place
def drop_piece(board, row, col, piece):
    board[row][col] = piece

#check if win
def win(board,piece):
    #Horizontal check
    for c in range(COL_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    #Vertical check
    for r in range(ROW_COUNT-3):
        for c in range(COL_COUNT):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    #Check diognals positive
    for r in range(ROW_COUNT-3):
        for c in range(COL_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
    #Negative diognals
    for r in range(3, ROW_COUNT):
        for c in range(COL_COUNT-3):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True


#Passing board to GUI
def draw_board(board):
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARSIZE, r*SQUARSIZE+SQUARSIZE, SQUARSIZE, SQUARSIZE))
            pygame.draw.circle(screen,BLACK,(c*SQUARSIZE+SQUARSIZE/2, r*SQUARSIZE+SQUARSIZE+SQUARSIZE/2), RADIUS)
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (c*SQUARSIZE+SQUARSIZE/2, height-int(r*SQUARSIZE+SQUARSIZE/2)), RADIUS )
                pygame.display.flip()
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW,(c * SQUARSIZE + SQUARSIZE / 2, height- int(r * SQUARSIZE + SQUARSIZE / 2)), RADIUS)
                pygame.display.flip()
board=create_board()
print_board(board)
Game_is_on=True
turn=0
pygame.init()
SQUARSIZE=80
RADIUS=int((SQUARSIZE/2)-5)
width=COL_COUNT*SQUARSIZE
height=(ROW_COUNT+1)*SQUARSIZE
size=(width,height)
screen=pygame.display.set_mode(size)
draw_board(board)
pygame.display.flip()
myfont=pygame.font.SysFont("monospace", 74, "bold")
while Game_is_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen,BLACK,(0,0, width, SQUARSIZE))
            posx=event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen,RED,(posx, int(SQUARSIZE/2)), RADIUS)
            else:
                pygame.draw.circle(screen,YELLOW,(posx, int(SQUARSIZE/2)), RADIUS)
        pygame.display.flip()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARSIZE))
            #Ask Player1 for input
            if turn == 0:
                posx=event.pos[0]
                col = int(math.floor(posx/SQUARSIZE))
                if is_valid_location(board,col):
                    row=next_row(board, col)
                    drop_piece(board,row,col, 1)
                    if win(board, 1):
                        label = myfont.render("P1 Wins!!!",1,RED)
                        screen.blit(label, (40,10))
                        Game_is_on=False
            #Ask Player2 for input
            else:
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARSIZE))
                if is_valid_location(board,col):
                    row=next_row(board, col)
                    drop_piece(board,row,col, 2)
                    if win(board, 2):
                        label=myfont.render("P2 wins!!!", 1 ,YELLOW)
                        screen.blit(label, (40, 10))
                        Game_is_on=False

            print_board(board)
            draw_board(board)
            turn+=1
            turn = turn%2

            if not Game_is_on:
                pygame.time.wait(3000)