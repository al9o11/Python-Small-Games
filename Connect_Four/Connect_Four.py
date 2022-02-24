import numpy as np
import pygame
import sys
import math
row_count=6
column_count=7
blue = (0,0,255)
black = (0,0,0)
red = (255,0,0)
yellow = (255,255,0)
def create_board():
    board = np.zeros((row_count,column_count))
    return board

def drop_piece(board,row,col,piece):
    board[row][col]=piece
    
def is_valid_location(board,col):
    return board[row_count-1][col]==0
def get_next_open_row(board,col):
    for r in range(row_count):
        if board[r][col]==0:
            return new_func(r)
def new_func(r):
    return r

def winning_move(board,piece):
    for c in range(column_count-3):
        for r in range(row_count):
            if board[r][c]==piece and board[r][c+1]==piece and board[r][c+2]==piece and board[r][c+3]==piece:
                return True
    for c in range(column_count):
        for r in range(row_count-3):
            if board[r][c]==piece and board[r+1][c]==piece and board[r+2][c]==piece and board[r+3][c]==piece:
                return True
    for c in range(column_count-3):
        for r in range(row_count-3):
            if board[r][c]==piece and board[r+1][c+1]==piece and board[r+2][c+2]==piece and board[r+3][c+3]==piece:
                return True
    for c in range(column_count-3):
        for r in range(3,row_count):
            if board[r][c]==piece and board[r-1][c+1]==piece and board[r-2][c+2]==piece and board[r-3][c+3]==piece:
                return True
def drow_board(board):
    for c in range(column_count):
        for r in range(row_count):
            pygame.draw.rect(screen,blue,(c*square_size,r*square_size+square_size,square_size,square_size))
            pygame.draw.circle(screen,black,(c*square_size+square_size/2,r*square_size+square_size+square_size/2),radius)
            
    for c in range(column_count):
        for r in range(row_count):
            if board[r][c]==1:
                pygame.draw.circle(screen,red,(c*square_size+square_size/2,height-(r*square_size+square_size/2)),radius)
            elif board[r][c]==2:
                pygame.draw.circle(screen,yellow,(c*square_size+square_size/2,height-(r*square_size+square_size/2)),radius)
    pygame.display.update()
board = create_board()
game_over = False
turn = 0
pygame.init()
square_size = 100
width = column_count*square_size
height = (row_count+1)*square_size
size = (width,height)
radius = int(square_size/2-5)
screen = pygame.display.set_mode(size)
drow_board(board)
pygame.display.update()
myfont = pygame.font.SysFont("monospace",75)
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.MOUSEMOTION:
            pygame.draw.rect(screen,black,(0,0,width,square_size))
            posx = event.pos[0]
            if turn==0:
                pygame.draw.circle(screen,red,(posx,int(square_size/2)),radius)
            else:
                pygame.draw.circle(screen,yellow,(posx,int(square_size/2)),radius)
            pygame.display.update()
        if event.type==pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen,black,(0,0,width,square_size))
            if turn ==0:
                posx = event.pos[0]
                col = int(math.floor(posx/square_size))
                if is_valid_location(board,col):
                    row = get_next_open_row(board,col)
                    drop_piece(board,row,col,1)
                    if winning_move(board,1):
                        lable = myfont.render("Player 1 Wins!!!",1,red)
                        screen.blit(lable,(40,10))
                        game_over = True
        
            else:
                posx = event.pos[0]
                col = int(math.floor(posx/square_size))
                if is_valid_location(board,col):
                    row = get_next_open_row(board,col)
                    drop_piece(board,row,col,2)
                    if winning_move(board,2):
                        lable = myfont.render("Player 2 Wins!!!",1,yellow)
                        screen.blit(lable,(40,10))
                        game_over = True
            drow_board(board)
            turn+=1
            turn = turn % 2
            if game_over:
                pygame.time.wait(2000)