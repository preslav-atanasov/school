import random
import time

import pygame

listOfDiscs = []
selected_disc = None
selected_tower = None
selected_disc_value = None


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0


def move_disk(from_tower, to_tower):
    if from_tower.isEmpty():
        return False

    if to_tower.isEmpty() or from_tower.peek() < to_tower.peek():
        disk_moved = from_tower.pop()
        to_tower.push(disk_moved)
        return True
    return False


def visualisation_and_logic(tower_index, pos, tower):
    global listOfDiscs, selected_disc, selected_tower, selected_disc_value

    # Draw tower
    rect = pygame.draw.rect(screen, "gray35", pygame.Rect((pos.x - 10, pos.y), (20, width * disks_number + 10)))

    # Check if tower is clicked to place a disc
    left, middle, right = pygame.mouse.get_pressed()
    if rect.collidepoint(pygame.mouse.get_pos()) and left and selected_disc is not None:
        # Try to move disc to this tower
        if selected_tower is not None:
            if move_disk(towers[selected_tower], tower):
                selected_disc = None
                selected_tower = None
                selected_disc_value = None

    # Draw discs for this tower
    tower_discs = []
    for i, disk_value in enumerate(tower.stack):
        disk_width = width * disk_value
        height = 30

        x = pos.x - (disk_width / 2)
        y = pos.y + (width * disks_number + 10) - (i + 1) * height  # Stack from bottom up

        disc = pygame.Rect((x, y), (disk_width, height))
        tower_discs.append((disc, disk_value, i))

    # Draw discs and check for selection (only top disc can be selected)
    for i, (disc, disk_value, stack_position) in enumerate(reversed(tower_discs)):
        color = pastel_colors[disk_value % len(pastel_colors)]

        # Only the top disc can be selected
        if stack_position == len(tower.stack) - 1:
            if disc.collidepoint(pygame.mouse.get_pos()) and left and selected_disc is None:
                selected_disc = disc
                selected_tower = tower_index
                selected_disc_value = disk_value

        # Change color if this is the selected disc
        if selected_disc == disc:
            color = "crimson"

        pygame.draw.rect(
            screen,
            color,
            disc,
            border_radius=15
        )

    return tower_discs


def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        yield from_rod, to_rod
    else:
        yield from TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
        move_disk(from_rod, to_rod)
        print("moved disk")
        yield from_rod, to_rod
        yield from TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)


width = 40

pastel_colors = [
    pygame.Color("lightblue"),
    pygame.Color("lightcoral"),
    pygame.Color("lightgreen"),
    pygame.Color("lightpink"),
    pygame.Color("lightsalmon"),
    pygame.Color("lightseagreen"),
    pygame.Color("lightskyblue"),
    pygame.Color("lightsteelblue")
]

random.shuffle(pastel_colors)

tower1 = Stack()
tower2 = Stack()
tower3 = Stack()
towers = [tower1, tower2, tower3]

disks_number = 10

# Initialize tower1 with discs (largest at bottom)
for i in range(disks_number, 0, -1):
    tower1.push(i)

pygame.init()
running = True
screen_width, screen_height = 1200, 800  # Reasonable window size
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tower of Hanoi")
FPS_CLOCK = pygame.time.Clock()

# Add a font for messages
font = pygame.font.SysFont(None, 36)

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Add escape key to exit fullscreen
                running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                if selected_disc is not None and selected_tower is not None:
                    pass

    # Clear screen
    screen.fill("antiquewhite1")

    # Tower positions
    tower_positions = [
        pygame.Vector2(screen_width / 4, 200),
        pygame.Vector2(screen_width / 2, 200),
        pygame.Vector2(3 * screen_width / 4, 200)
    ]

    # Draw towers and handle disc logic
    tower1_discs = visualisation_and_logic(0, tower_positions[0], tower1)
    tower2_discs = visualisation_and_logic(1, tower_positions[1], tower2)
    tower3_discs = visualisation_and_logic(2, tower_positions[2], tower3)

    # Check for win condition
    if len(tower3.stack) == disks_number:
        text = font.render("Congratulations! You solved the puzzle!", True, (0, 128, 0))
        screen.blit(text, (screen_width / 2 - text.get_width() / 2, 100))

    try:
        next(TowerOfHanoi(disks_number, tower1, tower3, tower2))
    except StopIteration:
        pass

    # Instructions
    instructions = font.render("Click on a disc to select it, then click on a tower to move it", True, (0, 0, 0))
    screen.blit(instructions, (screen_width / 2 - instructions.get_width() / 2, 50))

    pygame.display.update()
    pygame.time.delay(10)
    FPS_CLOCK.tick(60)

pygame.quit()
