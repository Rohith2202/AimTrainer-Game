import pygame
import random

pygame.init()
pygame.font.init()
screensize = width, height = 1400, 800
screen = pygame.display.set_mode((screensize))

score_initital = 0
font = pygame.font.Font('freesansbold.ttf', 32)
scorex = 10
scorey = 750

headshotx = 100
headshoty = 750

accuracyx = 600
accuracyy = 750


def accuracy(x, y, i):
    accurate = font.render("Accuracy:" + " " + str(i) + "%", True, (255, 0, 255))
    screen.blit(accurate, (x, y))


def display(x, y):
    score = font.render("Score:" + " " + str(score_initital), True, (255, 0, 0))
    screen.blit(score, (x, y))


def PerfectHeadshots(x, y):
    headshot = font.render("Headshot", True, (0, 0, 0))
    screen.blit(headshot, x, y)
    pygame.display.update()


pygame.display.set_caption("Aim Trainer")
icon = pygame.image.load("Icon.png")
pygame.display.set_icon(icon)

ballimage = pygame.image.load("Aimball.png")
ballimageX = random.randint(0, 1368)
ballimageY = random.randint(0, 700)


def player(ballimageX, ballimageY):
    screen.blit(ballimage, (ballimageX, ballimageY))


def change(ballimageX, clickX, ballimageY, clickY):
    if ballimageX < clickX <= (ballimageX + 32) and ballimageY < clickY <= (ballimageY + 32):
        return True
    else:
        return False


i = 0

running = True
while running:
    screen.fill((192, 192, 192))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                i += 1
                clickX, clickY = pygame.mouse.get_pos()
                collision = change(ballimageX, clickX, ballimageY, clickY)
                if collision:
                    if clickX == (ballimageX / 2) and clickY == (ballimageY / 2):
                        PerfectHeadshots(headshotx, headshoty)
                    ballimageX = random.randint(0, 1368)
                    ballimageY = random.randint(0, 700)
                    score_initital = score_initital + 1
        if i == 0:
            target = 0.0
        else:
            target = (score_initital / i) * 100

    player(ballimageX, ballimageY)
    display(scorex, scorey)
    accuracy(accuracyx, accuracyy, target)
    pygame.display.update()
