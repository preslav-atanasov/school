# Example file showing a circle moving on screen
import pygame


def gradually_squish_sprite(current_height, min_height, rate_of_squish):
    if current_height > min_height:
        new_height = current_height - rate_of_squish * dt
        if new_height < min_height:
            new_height = min_height
        return new_height
    return current_height


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
vertical_speed = 0
JUMP_STRENGTH = 5
width = 80
height = 80

squish_time = 10  # Number of frames for squish effect
squish_counter = 0  # Timer for squish duration
original_size = (80, 80)  # Original size of the sprite
squished_size = (80, 20)  # Squished size of the sprite

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_sprite = pygame.image.load("pompompurin.png").convert_alpha()
player_sprite = pygame.transform.scale(player_sprite, (width, height))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("darkslategray2")

    circle_radius = 40

    square_pos = pygame.Vector2(0, screen.get_height() / 2 + 100)
    ground = pygame.draw.rect(screen, color="forestgreen",
                              rect=pygame.Rect(square_pos, pygame.Vector2(screen.get_width(), 500)))

    if player_pos.y + circle_radius < ground.y:
        vertical_speed += 0.1
        grounded = False
        squish_counter = 0
    else:
        # If the sprite is about to hit the ground
        if player_pos.y + circle_radius + vertical_speed * dt >= ground.y:

            # Simulate the sprite landing (stop falling)
            player_pos.y = ground.y - circle_radius  # Adjust position to ground level
            if vertical_speed > 5:
                squish_counter = squish_time
            vertical_speed = 0  # Reset vertical speed after landing
            grounded = True  # Now the sprite is on the ground
        else:
            # Continue falling
            player_pos.y += vertical_speed * dt
            grounded = False

    if squish_counter > 0:
        # Interpolate between original and squished size
        squish_counter -= 50 * dt  # Reduce squish timer each frame

    keys = pygame.key.get_pressed()

    player_pos.y += vertical_speed

    if grounded:
        if keys[pygame.K_w]:
            vertical_speed -= JUMP_STRENGTH
            player_pos.y -= 1000 * dt

    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    sprite_rect = player_sprite.get_rect(center=(player_pos.x, player_pos.y))

    squish_factor = -((squish_counter - 5) / 1.6) ** 2 + 10

    sprite_rect.height -= squish_factor * 5
    sprite_rect.y += squish_factor * 5
    sprite_rect.y += 5
    current_sprite = pygame.transform.scale(player_sprite, sprite_rect.size)  # Restore to normal size
    screen.blit(current_sprite, sprite_rect.topleft)

    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(144) / 1000

pygame.quit()