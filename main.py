import pygame
import sys

from constants import *
from logger import log_state
from player import Player, Shot
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
    shots = pygame.sprite.Group()

    # Assign groups
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
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
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Screen background
        screen.fill(COLOR["black"])
        # Update
        updatable.update(dt)
        # Bullet collision
        for a in asteroids:
            for s in shots:
                if s.is_colliding(a):
                    s.kill()
                    a.split()
        # End game if collision detected
        for a in asteroids:
            if a.is_colliding(player):
                print("Game over!")
                sys.exit()
        # Redraw
        for obj in drawable:
            obj.draw(screen)

        # Store delta time, set game tick speed to 60fps
        dt = game_clock.tick(60) / 1000
        # Refresh screen
        pygame.display.flip()


if __name__ == "__main__":
    main()
