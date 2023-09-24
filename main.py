import math
import os.path
import random
import sys
import pygame
import constants as const

file_game = os.path.dirname(__file__)
music = True


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.Surface([50, 50])
        self.image.fill(const.VIOLET)
        self.rect = self.image.get_rect()
        pygame.sprite.Sprite.__init__(self)
        self.rect.y = random.randint(50, const.SCREEN_Y-50)
        self.rect.x = random.randint(50, const.SCREEN_X-50)

    def spawn(self):
        self.rect.y = random.randint(50, const.SCREEN_Y - 50)
        self.rect.x = random.randint(50, const.SCREEN_X - 50)


class Player(pygame.sprite.Sprite):
    """
    create a new person, move on person.
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # player_image = pygame.image.load(os.path.join(file_game, "hero.jpg")).convert()
        # self.image = player_image
        # self.rect = self.image.get_rect()
        self.image = pygame.Surface((20, 20))
        self.image.fill(const.BLUE)
        self.rect = self.image.get_rect()
        self.wins = 0
        self.rect.y = 1500 // cell_size
        self.rect.x = 1500 // cell_size


    def spawn(self):
        # TODO spawn not in player.
        self.rect.y = random.randint(100, const.SCREEN_Y - 100) // cell_size
        self.rect.x = random.randint(100, const.SCREEN_X - 100) // cell_size

    def update(self):
        """
        update, it's method sprites. player move diagonally, horizontally and vertically
        :return:
        """
        player_block = 10

        prev_y = self.rect.y
        prev_x = self.rect.x
        x, y = 0, 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:

                prev_y += player_block
                if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    prev_x -= player_block
                elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    prev_x += player_block
                y = round(prev_y / 30)
                x = round(prev_x / 30)
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
                prev_y -= player_block
                if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    prev_x -= player_block
                elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    prev_x += player_block
                y = prev_y // 30
                x = prev_x // 30
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
                prev_x -= player_block
                if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                    prev_y -= player_block
                elif keys[pygame.K_UP] or keys[pygame.K_w]:
                    prev_y += player_block
                y = prev_y // 30
                x = prev_x // 30
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                prev_x += player_block
                if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                    prev_y -= player_block
                elif keys[pygame.K_UP] or keys[pygame.K_w]:
                    prev_y += player_block
                y = round(prev_y / 30)
                x = round(prev_x / 30)

        if world[y][x] == ' ':
            self.rect.x = prev_x
            self.rect.y = prev_y
        else:
            return

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, height, width):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(const.GREY)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.win = GameWindow()


class GameWindow:
    """
    Window in the game, contains windows objects.
    """

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((const.SCREEN_X, const.SCREEN_Y))
        # This an icon (SHTO)
        icon = pygame.image.load("jokerge.jpg")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Game of TheNaturals  Pre-Alpha")


class GameView:
    """
    Show game objects without player.
    """

    def __init__(self):
        self.font_style = pygame.font.SysFont("particular", 40)
        self.win = GameWindow()
    def show(self):
        pass

    def message(self, text, color, y_move, x_move):
        msg = self.font_style.render(text, True, color)
        self.win.screen.blit(msg, (x_move, y_move))

    def display(self, color):
        self.win.screen.fill(color)

    def draw(self, enemies, players):
        """
        draw the groups
        :param enemies: pygame.sprite.Sprite()
        :param players: pygame.sprite.Sprite()
        :return: None
        """
        enemies.draw(self.win.screen)
        players.draw(self.win.screen)


def main_menu() -> None:

    global music
    view = GameView()
    clock = pygame.time.Clock()
    while 1:
        clock.tick(const.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(1)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if music:
                        pygame.mixer_music.unpause()
                        return
                    else:
                        return
                elif event.key == pygame.K_q:
                    sys.exit(1)
                elif event.key == pygame.K_m:
                    music = not music

        view.display(const.BLACK)
        view.message("Enter - return ", const.RED, 350, 400)
        view.message("Q - exit ", const.RED, 400, 400)
        if music:
            view.message("M - pause music ", const.RED, 450, 400)
        else:
            view.message("M - unpause music ", const.RED, 450, 400)
        pygame.display.flip()


def is_game_over() -> None:
    pygame.mixer_music.stop()
    view = GameView()
    clock = pygame.time.Clock()
    while 1:
        clock.tick(const.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(1)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return
                if event.key == pygame.K_q:
                    sys.exit(1)

        view.display(const.GREY)
        view.message("R - restart Q - quit", const.VIOLET, const.SCREEN_Y / 2, 400)
        pygame.display.flip()

def game_loop() -> None:
    """
    main loop in the Game. Controls and calls methods Classes.
    :return: None
    """
    win = GameWindow()
    player = Player()
    p_sprite = pygame.sprite.Group()
    p_sprite.add(player)

    clock = pygame.time.Clock()
    while 1:
        clock.tick(const.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    pygame.mixer_music.pause()
                    main_menu()

        win.screen.fill(const.BLACK)
        # draw map
        for row in range(world_height):
            for col in range(world_width):
                x = row * cell_size
                y = col * cell_size
                if world[row][col] == '#':
                    pygame.draw.rect(win.screen, const.BLACK, (x, y, cell_size, cell_size), 1)
                else:
                    pygame.draw.rect(win.screen, const.WHITE, (x, y, cell_size, cell_size), 1)
        p_sprite.update()
        p_sprite.draw(win.screen)

        pygame.display.flip()

world = []
cell_size = 30
world_height = const.SCREEN_Y // cell_size
world_width = const.SCREEN_X // cell_size
print(world_height, world_width)
def main():
    for row in range(world_height):
        line = []
        for col in range(world_width):
            if (row == 0 or row == world_height - 1 or
                    col == 0 or col == world_width - 1):
                line.append('#')
            else:
                line.append(' ')
        world.append(line)

    print(world)
    game_loop()

main()