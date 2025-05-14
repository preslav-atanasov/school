import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
vertical_speed = 0  # Initial vertical speed (start at 0)
gravity = 300  # How strong gravity is
jump_strength = -300  # How strong the jump is

# Squish effect variables
squish_time = 1000  # Number of frames for squish effect
squish_counter = 0  # Timer for squish duration
original_size = (80, 80)  # Original size of the sprite
squished_size = (80, 50)  # Squished size of the sprite

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_sprite = pygame.image.load("pompompurin.png").convert_alpha()
player_sprite = pygame.transform.scale(player_sprite, original_size)
current_sprite = player_sprite  # Keeps track of the current displayed sprite

ground_y = screen.get_height() / 2 + 100  # Ground Y position
