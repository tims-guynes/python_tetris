from settings import *
from sys import exit

#components
from game import Game
from score import Score
from preview import Preview

class Main:
    def __init__(self) -> None:
        
        #general
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        pygame.display.set_caption('Tetris-clone') #game title
        self.clock = pygame.time.Clock()

        #components
        self.game = Game()
        self.score = Score()
        self.preview = Preview()

    def run(self):
        #exit program
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            #display
            self.display_surface.fill(GREY)

            #components
            self.game.run()
            self.score.run()
            self.preview.run()
            
            #update gaem
            pygame.display.update()
            self.clock.tick(60)

if __name__ == '__main__':
    main = Main()
    main.run()