import pygame, ctypes, os, sys

from data.scripts.font import Font

class Game:
    def __init__(self):
        # initialize sdl settings for the game
        user32 = ctypes.windll.user32
        os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0'
        pygame.init()
        # get the width and height of the monitor and also set resolutions
        self.screenWidth = user32.GetSystemMetrics(0)
        self.screenHeight = user32.GetSystemMetrics(1)
        self.xResolution = 1920
        self.yResolution = 1080
        # initialize the sdl screen and display
        self.screen = pygame.display.set_mode(size=(self.screenWidth, self.screenHeight), flags=pygame.NOFRAME)
        self.display = pygame.Surface((self.xResolution, self.yResolution))
        # time related vars
        self.clock = pygame.time.Clock()
        self.fps = 60
        # initialize font class
        self.font = Font('data/visuals/font.png')
        # initialize the game
        self.MainMenu()

    def MainMenu(self):

        titleScale = 5
        titleText = 'boolean'
        titleSurface = pygame.Surface(self.font.size(titleText, titleScale))
        titleSurface.set_colorkey((0, 0, 0))
        self.font.render(titleSurface, titleText, (0, 0), titleScale)
        titleRect = pygame.Rect((0, 0), (titleSurface.get_size()))
        titleRect.center = self.xResolution / 2, self.yResolution / 2

        # initiliaze main menu loop
        running = True
        while running:

            # handle events
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.Exit()

            # update the display
            self.display.fill((0, 10, 10))
            self.display.blit(titleSurface, titleRect)

            # update the screen and run at the fps 
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))
            pygame.display.flip()
            self.clock.tick(self.fps)

    def Play(self):
        pass

    def Settings(self):
        pass

    def Exit(self):
        pygame.quit()
        sys.exit()

Game()