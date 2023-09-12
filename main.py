import os.path
import sys
import pygame
import constants as const

file_game = os.path.dirname(__file__)


class GameWindow:
    """
    Window in the game, contains windows objects.
    """
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((const.SCREEN_X, const.SCREEN_Y))
        self.font_style = pygame.font.SysFont("particular", 40)
        # This an icon (SHTO)
        icon = pygame.image.load("jokerge.jpg")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Game of TheNaturals  Pre-Alpha")


class Player(pygame.sprite.Sprite):
    """
    create a new person, move on person.
    """
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        player_image = pygame.image.load(os.path.join(file_game, "hero.jpg")).convert()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.center = (const.SCREEN_X / 2, const.SCREEN_Y / 2 + 50)
        self.name = name

    def update(self):
        """
        update it's method sprites.
        :return:
        """
        player_block = 10
        prev_y = self.rect.y
        prev_x = self.rect.x

        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            prev_y += player_block
        elif keys[pygame.K_UP]:
            prev_y -= player_block
        elif keys[pygame.K_LEFT]:
            prev_x -= player_block
        elif keys[pygame.K_RIGHT]:
            prev_x += player_block

        if (prev_x <= -10 or prev_x > const.SCREEN_X - 45 or
                prev_y <= -10 or prev_y > const.SCREEN_Y - 45):
            print("Game Over")
            return


        self.rect.x = prev_x
        self.rect.y = prev_y


class HandlerGame:
    # TODO make this class useful!
    def __init__(self):
        self.window = GameWindow()
        self.view = GameView()

    def main_menu(self, clock):
        while 1:
            clock.tick(const.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return
            self.window.screen.fill(const.BLACK)
            self.view.message("Tap Enter.", const.RED, 4, 2)
            pygame.display.flip()
    def death_p(self):
        clock = pygame.time.Clock()
        while 1:
            clock.tick(const.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return

        self.window.screen.fill(const.BLACK)
        self.view.message("R - restart Q - quit", 1, 2)
        pygame.display.flip()


class GameView:
    """
    Show game objects without player.
    """
    def __init__(self):
        self.win = GameWindow()

    def show(self):
        pass

    def message(self, text, color, x_move, y_move):
        msg = self.win.font_style.render(text, True, color)
        self.win.screen.blit(msg, (const.SCREEN_X/x_move, const.SCREEN_Y/y_move))

def game_loop():
        # main loop in the Game. Controls and calls methods Classes.
        # Handler key-words and draw objects in the game

        win = GameWindow()
        player = Player("Dima")
        view = GameView()
        handler_key = HandlerGame()

        clock = pygame.time.Clock()
        all_sprites = pygame.sprite.Group()
        all_sprites.add(player)
        while 1:
            clock.tick(const.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        handler_key.main_menu(clock)

            all_sprites.update()
            win.screen.fill(const.BEIGE)
            all_sprites.draw(win.screen)
            view.message("Tab escape {HA-HA-HA}", const.ORANGE, 4, 2)
            pygame.display.flip()



game_loop()


# pisipopi
