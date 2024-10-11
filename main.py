import pygame
import sys

#to start pygame we need to initialize it
pygame.init()

#Constants and important numbers
Width = 800
Height = 600
FPS = 60

#for each colour need to specify its number
White = (255, 255, 255)
Black = (0, 0, 0)
Red = (255, 0, 0)
Blue = (0, 0, 255)

#properties for players
Player_width = 50
Player_height = 100
player_speed = 5

#Creating game window
window = pygame.displya.set_mode((Width, Height))
pygame.display.set_caption("name")

#define player class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface([Player_width, Player_height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.speed = player_speed

        def move(self, keys, left_key, right_key):
            if keys[left_key]:
                self.rect.x -= self.speed
                if keys[right_key]:
                    self.rect.x += self.speed

#create the two players
player1 = Player(100, Height - Player_height - 50, Red)
player2 = Player(Width - 150, Height - Player_height - 50, Blue)

#Group the sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(player1)
all_sprites.add(player2)

#game loop
def game_loop():
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

#Get keypress
keys = pygame.key.get_pressed()

#player 1 controls A and D
player1.move(keys, pygame.K_a, pygame.K_d)

#player 2 controls Left and Right arrow keys
player2.move(keys, pygame.K_LEFT, pygame.K_RIGHT)

screen.fill(White)

#draw all sprites
all_sprites.draw(screen)

#update the display
pygame.display.flip()

#control the framerate
clock.tick(FPS)

#Run game
if __name__ == "__main__":
    game_loop()