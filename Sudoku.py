import pygame, sys, numpy as np
pygame.init()

SMALL_LINE_WIDTH = 6
BIG_LINE_WIDTH = 6
SQUARE_SIZE = 100 
MAX = SQUARE_SIZE * 9 + BIG_LINE_WIDTH *4 + SMALL_LINE_WIDTH * 6
BIG_DIST = 3 * SQUARE_SIZE + BIG_LINE_WIDTH + 2 * SMALL_LINE_WIDTH
SMALL_DIST = SMALL_LINE_WIDTH + SQUARE_SIZE
BIG_LINE_COLOR = (66, 66, 86)
SMALL_LINE_COLOR = (66, 166, 176)
num = 1

screen = pygame.display.set_mode(( MAX, MAX )) 
pygame.display.set_caption("SUDOKU")
screen.fill("WHITE")
pic = []
for i in range(9):
    t = i+1
    pic.append(pygame.image.load("c:\\temp\\"+ str(t) +".png")) 
    pic[i] = pygame.transform.scale(pic[i], (SQUARE_SIZE, SQUARE_SIZE))


board = np.zeros((9, 9))
board1 = [[0, 0, 4, 7, 1, 0, 0, 0, 0], [0, 7, 2, 8, 0, 6, 5, 0, 0], [0, 0, 0, 0, 0, 5, 0, 0, 7], [0, 1, 0, 6, 9, 0, 2, 0, 0], [3, 9, 0, 0, 5, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 8, 5], [0, 0, 1, 2, 3, 0, 8, 0, 4], [0, 0, 3, 5, 0, 4, 0, 0, 2], [2, 4, 0, 9, 0, 0, 0, 0, 0]]

def draw_big_lines():
    for i in range(4):
        pygame.draw.line( screen, BIG_LINE_COLOR,  (i * BIG_DIST + BIG_LINE_WIDTH / 2 -1, 0), (i * BIG_DIST + BIG_LINE_WIDTH / 2 -1, MAX), BIG_LINE_WIDTH)
        pygame.draw.line( screen, BIG_LINE_COLOR,  (0, i * BIG_DIST + BIG_LINE_WIDTH / 2 -1), (MAX, i * BIG_DIST + BIG_LINE_WIDTH / 2 -1), BIG_LINE_WIDTH)
def draw_small_lines():
    for i in range(10):
        pygame.draw.line( screen, SMALL_LINE_COLOR,  (i * SMALL_DIST + BIG_LINE_WIDTH / 2 -1, 0), (i * SMALL_DIST + BIG_LINE_WIDTH / 2 -1, MAX), BIG_LINE_WIDTH)
        pygame.draw.line( screen, SMALL_LINE_COLOR,  (0, i * SMALL_DIST + BIG_LINE_WIDTH / 2 -1), (MAX, i * SMALL_DIST + BIG_LINE_WIDTH / 2 -1), BIG_LINE_WIDTH)
def mark_square(rowX, rowY, num):
    found = False
    bigX = rowX // 3
    bigY = rowY // 3
    for i in range(9):
        if board[rowX][i] == num:
            found = True
        if board[i][rowY] == num:
            found = True
    for i in range(3):
        for j in range(3):
            if board[i + bigX *3][j + bigY *3] == num:
                found = True
    if not found: 
        board[rowX][rowY] = num
        screen.blit(pic[num-1],(rowY * SMALL_DIST + SMALL_LINE_WIDTH, rowX * SMALL_DIST + SMALL_LINE_WIDTH))
def check_win():
    finished = True
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                finished = False
    if finished == True:
        print("End")
def check_color():
    pass 

for i in range(9):
    for j in range(9):
        mark_square(i, j, board1[i][j])

draw_small_lines()
draw_big_lines()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key >= 49 and event.key <= 57:
                num = event.key - 48
                

        if event.type == pygame.MOUSEBUTTONDOWN:
            inputX = event.pos[1]
            inputY = event.pos[0]

            rowX = int(inputX // SMALL_DIST)
            rowY = int(inputY // SMALL_DIST)

            mark_square(rowX, rowY, num)
            check_win()
            check_color()
    pygame.display.update()