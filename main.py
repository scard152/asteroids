import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    #Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    #Assigning groups to classes
    Player.containers=(updatable, drawable)
    Asteroid.containers=(asteroids, updatable, drawable)
    AsteroidField.containers=(updatable)
    Shot.containers=(shots, updatable, drawable)
    
    #Objects
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()


    #Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0))

        updatable.update(dt)
        for a in asteroids:
            if a.collides_with(player):
                print("Game over!")
                return
        for a in asteroids:
            for s in shots:
                if a.collides_with(s):
                    a.split()
                    s.kill()
        for d in drawable:
            d.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60)/1000



if __name__ == "__main__":
    main()
