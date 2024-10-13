import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
FPS = 60
BLOCK_WIDTH = 50
BLOCK_HEIGHT = 50

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Player properties
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_SPEED = 5

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Blocks")

# Define Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([PLAYER_WIDTH, PLAYER_HEIGHT])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2 - PLAYER_WIDTH // 2
        self.rect.y = HEIGHT - PLAYER_HEIGHT - 10
        self.score = 0

    def move(self, keys):
        if keys[pygame.K_a] and self.rect.x > 0:  # Move left
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_d] and self.rect.x < WIDTH - PLAYER_WIDTH:  # Move right
            self.rect.x += PLAYER_SPEED

# Create a block class
class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([BLOCK_WIDTH, BLOCK_HEIGHT])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - BLOCK_WIDTH)
        self.rect.y = -BLOCK_HEIGHT  # Start off-screen

    def update(self):
        self.rect.y += 5  # Move the block down
        if self.rect.y > HEIGHT:  # Reset if it goes off screen
            self.rect.y = -BLOCK_HEIGHT
            self.rect.x = random.randint(0, WIDTH - BLOCK_WIDTH)

# Create player and block groups
player = Player()
blocks = pygame.sprite.Group()
for _ in range(5):  # Create multiple blocks
    block = Block()
    blocks.add(block)

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(blocks)

# Game loop
def game_loop():
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Get keypress
        keys = pygame.key.get_pressed()
        player.move(keys)

        # Update blocks
        blocks.update()

        # Check for collisions
        collided_blocks = pygame.sprite.spritecollide(player, blocks, False)
        for block in collided_blocks:
            player.score += 1  # Increase score
            block.rect.y = -BLOCK_HEIGHT  # Reset block to the top

        # Fill the screen
        screen.fill(WHITE)

        # Draw all sprites
        all_sprites.draw(screen)

        # Display score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {player.score}', True, BLACK)
        screen.blit(score_text, (10, 10))

        # Update the display
        pygame.display.flip()

        # Control the frame rate
        clock.tick(FPS)

# Run game
if __name__ == "__main__":
    game_loop()
