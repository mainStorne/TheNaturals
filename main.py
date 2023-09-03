# hello player

# import os
# import time
#
#
# def delay(text: str, t=0.25):
#     for char in text:
#         print(char, end='', flush=True)
#         time.sleep(t)
#
#
# welcome_text = ("Hello player! You will play soon!\n"
#                 "Please write your name: ")
#
# delay(welcome_text, 0.05)
# name_player = input()
# delay(name_player)
# os.system('cls')
# print('Success! Welcome to this World!')

# def foo(*args):
#     for arg in args:
#         print("arg is", arg)

# myTuple = (1, 1.2, "st", True)
#
# print(type(myTuple), *myTuple)
# foo(myTuple)

# myList = [2, 2.3, "on", False]
#
# print(type(myList), *myList)
#
# foo(myList)
# myList.copy()
#
# print(myList)

#myDict = {3: "hello", "st": True}

#mySet = {3, 3.4, "e", True, False}

import pygame
# initialization pygame mode
pygame.init()
# size of screen
size = [800, 600]
FPS = 10
# This our surface
screen = pygame.display.set_mode(size)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 82, 123)
#pygame.display.пу
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

import random


start_pos = [400, 200]
print("start", start_pos)
while not done:
    clock.tick(FPS)
    print(start_pos)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)

    move(start_pos)
    pygame.draw.circle(screen, WHITE, start_pos, 14)

    pygame.display.flip()

pygame.quit()
