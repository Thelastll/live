import pygame
from random import choice
pygame.init()

class Line(pygame.sprite.Sprite):
    def __init__(self, sc, pos1vx, pos1vy, pos2vx, pos2vy, color = (0, 0, 0)):
        pygame.sprite.Sprite.__init__(self)
        self.sc = sc
        self.pos1vx = pos1vx
        self.pos1vy = pos1vy
        self.pos2vx = pos2vx
        self.pos2vy = pos2vy
        self.color = color

    def update(self):
       pygame.draw.line(self.sc, self.color, (self.pos1vx, self.pos1vy), (self.pos2vx, self.pos2vy))

class Cells(pygame.sprite.Sprite):
    def __init__(self, sc, n, x, y, color = (0, 0, 0)):
        pygame.sprite.Sprite.__init__(self)
        self.sc = sc
        self.x = x
        self.y = y
        self.n = n
        self.color = color
        
    def update(self):
       pygame.draw.rect(self.sc, self.color, (self.x, self.y, n, n))
       


side = 801
sc = pygame.display.set_mode((side, side), pygame.RESIZABLE)

n = 16
color = (10, 130, 155)
cellcor = []

for i in range(0, side, n):
    for j in range(0, side, n):
        cellcor += [[i, j, choice([0]*9+[1])]]

cellcor_new = cellcor

line = pygame.sprite.Group()
cell = pygame.sprite.Group()
clock = pygame.time.Clock()
pat = [-51, -50, -49, -1, 1, 49, 50, 51]
ch = 0
fps = 10

for i in range(side//n+1):
    line.add(Line(sc, n*i, 0, n*i, side, color),
        Line(sc, 0, n*i, side, n*i, color))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    sc.fill((0, 0, 0))
    line.update()

    for i in cellcor:
        if i[2] == 1:
            cell.add(Cells(sc, n, i[0], i[1], color))

    cell.update()

    cell = pygame.sprite.Group()

    for i in range((side//n)**2):
        for ii in pat:
            if 0 <= cellcor[i][0] <= 800 and 0 <= cellcor[i][1] <= 800 and cellcor[i+ii][2] == 1:
                ch += 1

        if ch < 2 or ch > 3:
            cellcor_new[i][2] = 0

        elif ch == 3:
            cellcor_new[i][2] = 1

        ch = 0

    cellcor = cellcor_new

    clock.tick(fps)
    pygame.display.update()