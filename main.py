import pygame 
from constants import *


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main ():
    pygame.init()
    time_clock = pygame.time.Clock()
    dt = 0
   



    print('Starting asteroids!')
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True: 
        screen.fill((0,0,0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = time_clock.tick(60) / 1000
    
    
    
    

if __name__ == "__main__":
    
    main()


pygame.quit()   

    