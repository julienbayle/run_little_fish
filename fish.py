from pygame.sprite import Sprite
from pygame import Surface
from pygame import draw

# Define a Fish object by extending pygame.sprite.Sprite
class Fish(Sprite):
    def __init__(self, screen: Surface):
        super(Fish, self).__init__()
        self.screen = screen

        # Define fish surface
        self.surf = Surface((100, 50))
        self.rect = self.surf.get_rect()

        # Draw the fish
        self.surf.fill((150, 150, 150))
        draw.circle(self.surf, (0, 200, 0), (25, 25), 20)
        
    def display(self):
        self.screen.blit(self.surf, self.rect)

    # Move the sprite based on user keypresses
    def update(self, fish_direction):
        self.rect.move_ip(fish_direction["X"], fish_direction["Y"])

        # Keep the fish on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.screen and self.rect.right > self.screen.get_width():
            self.rect.right = self.screen.get_width()
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.screen and self.rect.bottom >= self.screen.get_height():
            self.rect.bottom = self.screen.get_height()
