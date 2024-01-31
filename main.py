import pygame
import random
pygame.init()
gamescreen = pygame.display.set_mode((900, 900))
pygame.display.set_caption("Particle Accelerator")
clock = pygame.time.Clock()

gameOver = False

xpos = []  # position
ypos = []
xVel = []
yVel = []  # velocity\

# particles
for i in range(10):
    xpos.append(450)
    ypos.append(450)
    xVel.append(random.randint(-2, 2))
    yVel.append(random.randint(-2, 3))

while not gameOver:
    clock.tick(60)

    # Event Handle
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

    # physics
    for i in range(10):
        # update pos
        xpos[i] += xVel[i]
        ypos[i] += yVel[i]

      # boundary check
        if xpos[i] < 0 or xpos[i] > 900:
            xVel[i] *= -1
        if ypos[i] < 0 or ypos[i] > 900:
            yVel[i] *= -1

    # render
    gamescreen.fill((0, 0, 0))
    pygame.draw.circle(gamescreen, (255, 255, 255), (xpos[i], ypos[i]), 5)
    pygame.display.flip()

# end of game
pygame.quit()
