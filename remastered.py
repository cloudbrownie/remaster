import pygame, ctypes, os, sys

from data.scripts.font import Font
from data.scripts.gui_elems import TextButton

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
        # ratios for differing screen size and resolution
        self.xRatio = self.screenWidth / self.xResolution
        self.yRatio = self.screenHeight / self.yResolution
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

        titleScale = 6
        titleText = 'boolean'
        titleSurface = pygame.Surface(self.font.size(titleText, titleScale))
        titleSurface.set_colorkey((0, 0, 0))
        self.font.render(titleSurface, titleText, (0, 0), titleScale)
        titleRect = pygame.Rect((0, 0), (titleSurface.get_size()))
        titleRect.center = self.xResolution * .5, self.yResolution * .3

        buttonScale = 4
        playButton = TextButton('play', (self.xResolution *.5, self.yResolution * .5), buttonScale)
        settingsButton = TextButton('settings', (self.xResolution * .5, self.yResolution * .65), buttonScale)
        exitButton = TextButton('exit', (self.xResolution * .5, self.yResolution * .8), buttonScale)

        # initiliaze main menu loop
        running = True
        while running:

            # mouse positions for events and other objects
            mx, my = pygame.mouse.get_pos()
            mousepos = mx / self.xRatio, my / self.yRatio

            # handle events
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.Exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if playButton.rect.collidepoint(mousepos):
                            self.Play()
                        elif settingsButton.rect.collidepoint(mousepos):
                            self.Settings()
                        elif exitButton.rect.collidepoint(mousepos):
                            self.Exit()

            # update the display
            self.display.fill((0, 10, 10))
            self.display.blit(titleSurface, titleRect)
            playButton.draw(self.display, mousepos)
            settingsButton.draw(self.display, mousepos)
            exitButton.draw(self.display, mousepos)

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