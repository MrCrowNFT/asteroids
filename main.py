import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt= 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable =pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    Player.containers = (drawable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots_group, updatable, drawable)


    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    player.shots_group = shots_group

    asteroid_field = AsteroidField()  



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for sprite in drawable:
            sprite.draw(screen)
        
        for shot in shots_group:
            shot.draw(screen)

        updatable.update(dt)
        player.update(dt, player.shots_group)

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                exit()

        pygame.display.flip()
        time_passed=clock.tick(60)
        dt = time_passed/1000

        
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()