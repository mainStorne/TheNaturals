import pygame
import constants as const


class GameWindow:
    """
    Window in the game, contains windows objects.
    """
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((const.SCREEN_X, const.SCREEN_Y))
        self.font_style = pygame.font.SysFont(None, 40)
        # This an icon (SHTO)
        icon = pygame.image.load("jokerge.jpg")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Game of TheNaturals  Pre-Alpha")


class Player:
    """
    create a new person, move 'moves' on person and show him.
    """
    def __init__(self, name, x, y):
        self.win = GameWindow()
        self.name = name
        self.x = x
        self.y = y

    def move(self, direction, step):
        """
        move player on step and depend on direction
        :param direction: the key on the input
        :param step: move on step player
        :return: None
        """
        if (direction == pygame.K_UP and
                self.y - step > 0):
            self.y -= step
        elif (direction == pygame.K_DOWN and
                self.y + step < const.SCREEN_Y):
            self.y += step
        elif (direction == pygame.K_RIGHT and
                self.x + step < const.SCREEN_X):
            self.x += step
        elif (direction == pygame.K_LEFT and
                self.x - step > 0):
            self.x -= step
        else:
            pass

    def show(self):
        """
        show player
        :return: None
        """
        pygame.draw.circle(self.win.screen, const.WHITE, (self.x, self.y), 15)



class HandlerGame:
    def __init__(self):
        self.window = GameWindow()
        self.view = GameView()

    def main_menu(self, clock):
        while 1:
            clock.tick(const.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            self.window.screen.fill(const.BLACK)
            self.view.message("Write the arrows! Please tap Enter.", const.RED)
            pygame.display.flip()



class GameManager:
    """
    General class, make game.
    """
    def __init__(self):
        self.window = GameWindow()
        self.player = Player("Dima", 200, 400)
        self.view = GameView()
        self.handler_key = HandlerGame()

    def lop(self):
        """
        main loop in the Game. Controls and calls methods Classes.
        Handler key-words and draw objects in the game
        :return: None
        """
        clock = pygame.time.Clock()
        finish = False
        while not finish:
            clock.tick(const.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finish = True
                elif event.type == pygame.KEYDOWN:
                    self.player.move(event.key, 100)
                    if event.key == pygame.K_ESCAPE:
                        self.handler_key.main_menu(clock)

            self.window.screen.fill(const.BLACK)
            self.player.show()
            pygame.display.flip()

        pygame.quit()


class GameView:
    """
    Show game objects without player.
    """
    def __init__(self):
        self.win = GameWindow()

    def show(self):
        pass

    def message(self, text, color):
        msg = self.win.font_style.render(text, True, color)
        self.win.screen.blit(msg, (const.SCREEN_X/3, const.SCREEN_Y/2))


game = GameManager()
game.lop()



# pisipopi