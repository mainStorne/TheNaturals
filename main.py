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


 # class Player(pygame.sprite.Sprite):
 #    """
 #    create a new person, move on person.
 #    """
 #
 #    def __init__(self):
 #        pygame.sprite.Sprite.__init__(self)
 #        player_image = pygame.image.load(os.path.join(file_game, "hero.jpg")).convert()
 #        self.image = player_image
 #        self.rect = self.image.get_rect()
 #        self.wins = 0
 #        self.rect.y = 150 #random.randint(100, const.SCREEN_Y - 100)
 #        self.rect.x = 200 #random.randint(100, const.SCREEN_X - 100)

class Player(pygame.sprite.Sprite):
    """
    create a new person, move on person.
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        player_image = pygame.image.load(os.path.join(file_game, "hero.jpg")).convert()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.wins = 0
        self.rect.y = 150 #random.randint(100, const.SCREEN_Y - 100)
        self.rect.x = 150 #random.randint(100, const.SCREEN_X - 100)


    def spawn(self):
        # TODO spawn not in player.
        self.rect.y = random.randint(100, const.SCREEN_Y - 100)
        self.rect.x = random.randint(100, const.SCREEN_X - 100)

    def update(self, player, walls):
        """
        update, it's method sprites. player move diagonally, horizontally and vertically
        :return:
        """
        player_block = 10
        prev_y = self.rect.y
        prev_x = self.rect.x
        y = self.rect.y // 50
        x = self.rect.x // 50
        station = None

        keys = pygame.key.get_pressed()
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and world[y+1][x] == '_':
            prev_y += player_block
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                prev_x -= player_block
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                prev_x += player_block
        elif (keys[pygame.K_UP] or keys[pygame.K_w]) and world[y][x] == '_':
            prev_y -= player_block
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                prev_x -= player_block
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                prev_x += player_block
        elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and world[y][x] == '_':
            prev_x -= player_block
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                prev_y -= player_block
            elif keys[pygame.K_UP] or keys[pygame.K_w]:
                prev_y += player_block
        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and world[y][x+1] == '_':
            prev_x += player_block
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                prev_y -= player_block
            elif keys[pygame.K_UP] or keys[pygame.K_w]:
                prev_y += player_block


        self.rect.x = prev_x
        self.rect.y = prev_y

# def handler_collision(player, walls):
#
#     kick = pygame.sprite.spritecollide(player, walls, False)
#     if kick:
#         # self.rect.x =
#
#         return
#     else:
#         rect.x = prev_x
#         rect.y = prev_y
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, height, width):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(const.GREY)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.win = GameWindow()


    # def generate(self):
    #     for i in range(self.size_wall):
    #         for j in range(self.size_wall):
    #             if (i == 0 or i == 9 or
    #                     j == 0 or j == 9):
    #                 self.wall[i][j] = '#'
    #             else:
    #                 self.wall[i][j] = '-'
    #     print(self.wall)
    def draw(self):
        # for i in range(self.size_wall):
        #     for j in range(self.size_wall):
        #         if self.wall[i][j] == '#':
        pass


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


world = []
cell_size = 50
world_height = const.SCREEN_Y // cell_size
world_width = const.SCREEN_X // cell_size


for row in range(world_height):
    line = []
    for col in range(world_width):
        if (row == 0 or row == world_height - 1 or
                col == 0 or col == world_width - 1):
            line.append('#')
        else:
            line.append('_')
    world.append(line)

print(world)

def game_loop() -> None:
    """
    main loop in the Game. Controls and calls methods Classes.
    :return: None
    """
    # TODO create delayed spawn enemy.

    #pygame.mixer.init()
    #pygame.mixer_music.load("Revenge-_feat.-Cazok_.wav")
    #pygame.mixer_music.set_volume(0.05)
    #pygame.mixer_music.play()

    # game helpers
    win = GameWindow()
    # view = GameView()
    # # game characters
    player = Player()
    # enemy = Enemy()
    # # make groups
    # enemies = pygame.sprite.Group()
    # enemies.add(enemy)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    walls = pygame.sprite.Group()

    for row in range(world_height):
        for col in range(world_width):
            x = row * cell_size
            y = col * cell_size
            if world[row][col] == 1:
                w = Wall(x, y, cell_size, cell_size)
                walls.add(w)
            else:
                pass
    # TODO create delayed spawn enemy.

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
                    pygame.draw.rect(win.screen, const.BLACK, (x, y, cell_size, cell_size))
                else:
                    pygame.draw.rect(win.screen, const.WHITE, (x, y, cell_size, cell_size), 1)

        all_sprites.draw(win.screen)



        all_sprites.update(player, walls)

        # all_sprites.update()
        # enemies.update()
        # view.display(const.BEIGE)
        # view.draw(enemies, all_sprites)
        # view.message(f'Score: {player.wins}', const.VIOLET, 40, 10)
        # # view.message("esc - main menu", const.ORANGE, 10, 10)
        # for w in walls:
        #     w.draw()

        pygame.display.flip()




game_loop()
# wall = Wall()
# wall.generate()
# pisipopi
