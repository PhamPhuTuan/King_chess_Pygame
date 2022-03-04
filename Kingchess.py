# import
import pygame
import sys
from pygame.locals import*

pygame.display.set_caption('KING CHESS by PHU TUAN')
pygame.init()
display = pygame.display.set_mode((680, 680))
pos = pygame.image.load('pos.png')
FPS = 60
fpsClock = pygame.time.Clock()  # fpsClock.tick(FPS)

black = (46, 74, 165)
white = (77, 93, 242)
green = (137, 129, 129)
chu = (26, 55, 22)

# 1 - whitepawn   -1 - blackpawn   2 - whitebishop    -2 - blackbishop     3 - whiteknight    -3 - blackknight
# 4 - whitebishop -4 - blackbishop 5 - whiteking      -5 - blackking       6 - whitequeen     -6 - blackqueen
n = 9
matrix_display = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 4, 1, 0, 0, 0, 0, -1, -4],  
                  [0, 3, 1, 0, 0, 0, 0, -1, -3],  
                  [0, 2, 1, 0, 0, 0, 0, -1, -2],  
                  [0, 5, 1, 0, 0, 0, 0, -1, -5],  
                  [0, 6, 1, 0, 0, 0, 0, -1, -6],  
                  [0, 2, 1, 0, 0, 0, 0, -1, -2],
                  [0, 3, 1, 0, 0, 0, 0, -1, -3],
                  [0, 4, 1, 0, 0, 0, 0, -1, -4]]

# black
Blackpawn = pygame.image.load('blackpawn.png')
Blackqueen = pygame.image.load('blackqueen.png')
Blackking = pygame.image.load('blackking.png')
Blackrook = pygame.image.load('blackrook.png')
Blackknight = pygame.image.load('blackknight.png')
Blackbishop = pygame.image.load('blackbishop.png')
# white
Whitepawn = pygame.image.load('whitepawn.png')
Whitequeen = pygame.image.load('whitequeen.png')
Whiteking = pygame.image.load('whiteking.png')
Whiterook = pygame.image.load('whiterook.png')
Whiteknight = pygame.image.load('whiteknight.png')
Whitebishop = pygame.image.load('whitebishop.png')

chessmans = {1: Whitepawn,      -1: Blackpawn,
             2: Whitebishop,    -2: Blackbishop,
             3: Whiteknight,    -3: Blackknight,
             4: Whiterook,      -4: Blackrook,
             5: Whiteking,      -5: Blackking,
             6: Whitequeen,     -6: Blackqueen}

x_block = [0]
y_block = [0]


def Get_position_of_bishop(ChessmanType, x, y, xDi, yDi, matrix):
    result = []
    while True:
        x += xDi
        y += yDi
        if x == 0 or x == 9 or y == 0 or y == 9:
            break
        elif ChessmanType*matrix[x][y] > 0:
            break
        elif ChessmanType*matrix[x][y] < 0:
            result.append([x, y])
            break

        result.append([x, y])

    return result


def Get_position_of_knight(dic, ChessmanType, x, y, xDi, yDi, matrix):
    result = []
    x += xDi
    y += yDi
    if dic == 'NB':
        if y > 0 and y < 9:
            if x-1 != 0:
                if matrix[x-1][y] == 0 or matrix[x-1][y]*ChessmanType < 0:
                    result.append([x-1, y])
            if x+1 != 9:
                if matrix[x+1][y] == 0 or matrix[x+1][y]*ChessmanType < 0:
                    result.append([x+1, y])

    if dic == 'DT':
        if x > 0 and x < 9:
            if y-1 != 0:
                if matrix[x][y-1] == 0 or matrix[x][y-1]*ChessmanType < 0:
                    result.append([x, y-1])
            if y+1 != 9:
                if matrix[x][y+1] == 0 or matrix[x][y+1]*ChessmanType < 0:
                    result.append([x, y+1])
    return result


def Get_position_of_rook(ChessmanType, x, y, xDi, yDi, matrix):
    result = []
    while True:
        x += xDi
        y += yDi
        if x == 0 or x == 9 or y == 0 or y == 9:
            break
        elif ChessmanType*matrix[x][y] > 0:
            break
        elif ChessmanType*matrix[x][y] < 0:
            result.append([x, y])
            break

        result.append([x, y])

    return result


def Get_position_of_king(ChessmanType, x, y, matrix):
    result = []
    xR, yR = (x, y)
    x, y = (xR, yR-1)
    if x != 0 and x != 9 and y != 0 and y != 9:
        if ChessmanType*matrix[x][y] < 0 or matrix[x][y] == 0:
            result.append([x, y])

    x, y = (xR, yR+1)
    if x != 0 and x != 9 and y != 0 and y != 9:
        if ChessmanType*matrix[x][y] < 0 or matrix[x][y] == 0:
            result.append([x, y])

    x, y = (xR-1, yR)
    if x != 0 and x != 9 and y != 0 and y != 9:
        if ChessmanType*matrix[x][y] < 0 or matrix[x][y] == 0:
            result.append([x, y])

    x, y = (xR+1, yR)
    if x != 0 and x != 9 and y != 0 and y != 9:
        if ChessmanType*matrix[x][y] < 0 or matrix[x][y] == 0:
            result.append([x, y])

    x, y = (xR-1, yR-1)
    if x != 0 and x != 9 and y != 0 and y != 9:
        if ChessmanType*matrix[x][y] < 0 or matrix[x][y] == 0:
            result.append([x, y])

    x, y = (xR+1, yR-1)
    if x != 0 and x != 9 and y != 0 and y != 9:
        if ChessmanType*matrix[x][y] < 0 or matrix[x][y] == 0:
            result.append([x, y])

    x, y = (xR-1, yR+1)
    if x != 0 and x != 9 and y != 0 and y != 9:
        if ChessmanType*matrix[x][y] < 0 or matrix[x][y] == 0:
            result.append([x, y])

    x, y = (xR+1, yR+1)
    if x != 0 and x != 9 and y != 0 and y != 9:
        if ChessmanType*matrix[x][y] < 0 or matrix[x][y] == 0:
            result.append([x, y])

    return result


def fill_color():
    display.fill(green)

    pygame.draw.rect(display, black, (20, 20, 640, 640))
    for i in range(0, 8):
        for j in range(0, 8):
            if i % 2 == 1 and j % 2 == 1:
                x = i*80 + 20
                y = j*80 + 20
                pygame.draw.rect(display, white, (x, y, 80, 80))
            if i % 2 == 0 and j % 2 == 0:
                x = i*80 + 20
                y = j*80 + 20
                pygame.draw.rect(display, white, (x, y, 80, 80))

    font = pygame.font.SysFont("bahnschrift", 15)
    textSurface = font.render('1', True, chu)
    display.blit(textSurface, (6, 50))

    textSurface = font.render('2', True, chu)
    display.blit(textSurface, (6, 130))

    textSurface = font.render('3', True, chu)
    display.blit(textSurface, (6, 210))

    textSurface = font.render('4', True, chu)
    display.blit(textSurface, (6, 290))

    textSurface = font.render('5', True, chu)
    display.blit(textSurface, (6, 370))

    textSurface = font.render('6', True, chu)
    display.blit(textSurface, (6, 450))

    textSurface = font.render('7', True, chu)
    display.blit(textSurface, (6, 530))

    textSurface = font.render('8', True, chu)
    display.blit(textSurface, (6, 610))

    textSurface = font.render('A', True, chu)
    display.blit(textSurface, (50, 662))

    textSurface = font.render('B', True, chu)
    display.blit(textSurface, (130, 662))

    textSurface = font.render('C', True, chu)
    display.blit(textSurface, (210, 662))

    textSurface = font.render('D', True, chu)
    display.blit(textSurface, (290, 662))

    textSurface = font.render('E', True, chu)
    display.blit(textSurface, (370, 662))

    textSurface = font.render('F', True, chu)
    display.blit(textSurface, (450, 662))

    textSurface = font.render('G', True, chu)
    display.blit(textSurface, (530, 662))

    textSurface = font.render('H', True, chu)
    display.blit(textSurface, (610, 662))


def get_adress_of_block():
    global x_block, y_block
    lx = 20
    ly = 20

    for x in range(1, n):
        x_block.append(lx)
        lx += 80
    for y in range(1, n):
        y_block.append(ly)
        ly += 80


def show_chessman():
    for x in range(n):
        for y in range(n):
            if matrix_display[x][y] != 0:
                display.blit(chessmans[matrix_display[x]
                             [y]], (x_block[x], y_block[y]))


def block_mouse_stay():
    if (20 <= xmouse <= 660) and (20 <= ymouse <= 660):
        for x in range(1, 9):
            for y in range(1, 9):
                if (x_block[x] <= xmouse <= x_block[x] + 80) and (y_block[y] <= ymouse <= y_block[y] + 80):
                    return[x, y]

    return [0, 0]


def possiblePosition(chessman, x, y):
    result = []
    if chessman < 0:
        chessman *= -1

    if chessman == 1:
        if chessmanType < 0 and y != 1:
            if matrix_display[x][y-1] == 0:
                result.append([x, y-1])
                if (y == 7) and (matrix_display[x][y-2] == 0):
                    result.append([x, y-2])
            if x != 1 and matrix_display[x - 1][y - 1] > 0:
                result.append([x - 1, y - 1])
            if x != 8 and matrix_display[x+1][y-1] > 0:
                result.append([x+1, y-1])

        elif chessmanType > 0 and y != 8:
            if matrix_display[x][y+1] == 0:
                result.append([x, y+1])
                if y == 2 and matrix_display[x][y+2] == 0:
                    result.append([x, y+2])
            if x != 1 and matrix_display[x-1][y+1] < 0:
                result.append([x-1, y+1])
            if x != 8 and matrix_display[x+1][y+1] < 0:
                result.append([x+1, y+1])

    if chessman == 2:
        res = [Get_position_of_bishop(chessmanType, x, y, -1, -1, matrix_display),
               Get_position_of_bishop(
                   chessmanType, x, y, 1, -1, matrix_display),
               Get_position_of_bishop(
                   chessmanType, x, y, -1, 1, matrix_display),
               Get_position_of_bishop(
                   chessmanType, x, y, 1, 1, matrix_display),
               ]
        for i in res:
            for index in i:
                result.append(index)

    if chessman == 3:
        res = [Get_position_of_knight('NB', chessmanType, x, y, 0, -2, matrix_display),
               Get_position_of_knight(
                   'NB', chessmanType, x, y, 0, 2, matrix_display),
               Get_position_of_knight(
                   'DT', chessmanType, x, y, 2, 0, matrix_display),
               Get_position_of_knight(
                   'DT', chessmanType, x, y, -2, 0, matrix_display),
               ]
        for i in res:
            for index in i:
                result.append(index)

    if chessman == 4:
        res = [Get_position_of_rook(chessmanType, x, y, 0, -1, matrix_display),
               Get_position_of_rook(
                   chessmanType, x, y, 0, 1, matrix_display),
               Get_position_of_rook(
                   chessmanType, x, y, 1, 0, matrix_display),
               Get_position_of_rook(chessmanType, x, y, -1, 0, matrix_display), ]

        for i in res:
            for index in i:
                result.append(index)

    if chessman == 5:
        res = Get_position_of_king(chessmanType, x, y, matrix_display)
        for index in res:
            result.append(index)

    if chessman == 6:
        res = [Get_position_of_bishop(chessmanType, x, y, -1, -1, matrix_display),
               Get_position_of_bishop(
                   chessmanType, x, y, 1, -1, matrix_display),
               Get_position_of_bishop(
                   chessmanType, x, y, -1, 1, matrix_display),
               Get_position_of_bishop(
                   chessmanType, x, y, 1, 1, matrix_display),
               Get_position_of_rook(
                   chessmanType, x, y, 0, -1, matrix_display),
               Get_position_of_rook(
                   chessmanType, x, y, 0, 1, matrix_display),
               Get_position_of_rook(
                   chessmanType, x, y, 1, 0, matrix_display),
               Get_position_of_rook(chessmanType, x, y, -1, 0, matrix_display), ]

        for i in res:
            for index in i:
                result.append(index)

    return result


def show_possiblePosition(listposition):
    for i in range(len(listposition)):
        x = listposition[i][0]
        y = listposition[i][1]
        display.blit(pos, (x_block[x], y_block[y]))


this_chessmanIMG = 0
after = 0
before = 0
wchessman, hchessman = Whiteking.get_size()
chessmanType = 0
listposition = []


def move_chessman():
    global chessmanType, after, before, this_chessmanIMG, listposition
    if click != [0, 0] and change:
        if click[0]:
            before = Block_current
            chessmanType = matrix_display[before[0]][before[1]]
            this_chessmanIMG = chessmans[chessmanType]
            matrix_display[before[0]][before[1]] = 0
            listposition = possiblePosition(chessmanType, before[0], before[1])
        else:
            after = Block_current
            matrix_display[after[0]][after[1]] = chessmanType
            this_chessmanIMG = 0
            fill_color()
            show_chessman()

    if this_chessmanIMG != 0:
        fill_color()
        show_possiblePosition(listposition)
        show_chessman()
        a = xmouse - wchessman//2
        b = ymouse - wchessman//2
        display.blit(this_chessmanIMG, (a, b))


get_adress_of_block()

fill_color()
show_chessman()
i_click = -1
Block_current = [0, 0]
click = [0, 0]
xmouse = 0
ymouse = 0
run = True
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        elif event.type == MOUSEMOTION:
            xmouse, ymouse = event.pos

    block = block_mouse_stay()
    isClick, nothing1, nothing2 = pygame.mouse.get_pressed()
    if block != [0, 0]:
        Block_current = block_mouse_stay()

    change = False
    if isClick and 20 <= xmouse <= 660 and 20 <= ymouse <= 660:
        if click[0] == 1 or matrix_display[Block_current[0]][Block_current[1]] != 0:
            pygame.event.wait()
            i_click += 1
            click[i_click % 2] = 1
            click[(i_click+1) % 2] = 0
            change = True
        elif isClick:
            pygame.event.wait()
            click = [0, 0]

    move_chessman()

    fpsClock.tick(FPS)
    pygame.display.update()

pygame.quit()
