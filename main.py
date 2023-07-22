# Import and initialize the pygame library
import pygame
from pygame.joystick import Joystick, get_count

# Run little fish pygame program
from fish import Fish
from motion_controller import MotionController

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Init
pygame.init()

# Set up the drawing window in full screen mode
screen = pygame.display.set_mode((800, 600), pygame.FULLSCREEN)

# Create a fish
fish = Fish(screen)

# Init motion controller
joysticks = [Joystick(x) for x in range(get_count())]
motion_controller = MotionController()

# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        motion_controller.update(event)

    # Fill the background with white
    screen.fill((255, 255, 255))

    fish.update(motion_controller.get_fish_direction())
    fish.display()

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.joystick.quit()
pygame.quit()
