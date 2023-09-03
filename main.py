import pygame
import constants
# initialization pygame mode
pygame.init()
# This our surface
screen = pygame.display.set_mode(constants.size)
# This an icon (SHTO)
icon = pygame.image.load("jokerge.jpg")
pygame.display.set_icon(icon)

pygame.display.set_caption("Game of TheNaturals  Pre-Alpha")
# flag of the circle
done = False
# FPS
clock = pygame.time.Clock()
def move(start) -> list:
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_UP]:
        start[1] -= 5
    elif keystate[pygame.K_DOWN]:
        start[1] += 5
    elif keystate[pygame.K_LEFT]:
        start[0] -= 5
    elif keystate[pygame.K_RIGHT]:
        start[0] += 5
    else:
        return start


start_pos = [400, 200]
while not done:
    clock.tick(constants.FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(constants.BLACK)

    move(start_pos)
    pygame.draw.circle(screen, constants.WHITE, start_pos, 14)
    pygame.display.flip()

pygame.quit()
#pisipopi