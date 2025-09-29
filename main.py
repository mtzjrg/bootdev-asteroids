import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    # Initialize pygame, get default screen size
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create group types
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Assign groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # Create player/asteroids
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # Initialize game clock and delta time
    game_clock = pygame.time.Clock()
    dt = 0

    # Print screen info to terminal
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Screen background
        screen.fill(COLOR["black"])

        # Update/redraw
        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)

        # Store delta time, set game tick speed to 60fps
        dt = game_clock.tick(60) / 1000
        # Refresh screen
        pygame.display.flip()


if __name__ == "__main__":
    main()
