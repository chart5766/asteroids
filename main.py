import pygame 
from player import *
from constants import *
from asteroidfield import *


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroid_group = pygame.sprite.Group()
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroid_group, updatable, drawable)
AsteroidField.containers = (updatable,)
def main ():
    pygame.init()
    time_clock = pygame.time.Clock()
    dt = 0


    player_instant = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_instance = AsteroidField()
   
   



    print('Starting asteroids!')
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True: 
        screen.fill((0,0,0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = time_clock.tick(60) / 1000

        # player_instant.update(dt)

        # player_instant.draw(screen)

        for update in updatable:
            update.update(dt)
        # for draw in drawable:
        drawable.draw(screen)
        pygame.display.flip()
    
    
    
    

if __name__ == "__main__":
    
    main()

    pygame.display.quit()
    pygame.quit()   

    