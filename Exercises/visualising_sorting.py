import math
from copy import copy

import pygame
import random

pygame.init()
running = True

screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

delay_ms = 25

number_of_elements = 100
if number_of_elements > int(screen_width / 2) - 100:
    raise ValueError("Number too large! A bar's width will be less than a pixel wide!")

range_of_numbers = len(range(1, screen_width))
input_list = random.sample(range(1, screen_width), number_of_elements)
input_list2 = copy(input_list)
width = ((screen_width - 200) / 2) / number_of_elements


def visualise(pos, list_to_visualise, color):
    for bar in range(0, len(list_to_visualise)):
        x = pos.x + bar * width
        height = int(list_to_visualise[bar]) * (100 / range_of_numbers) * math.pi
        y = screen.get_height() / 2 + 300
        pygame.draw.rect(screen, color, pygame.Rect((x, y - height), (width, height)))


def bubble_sort_step(list_to_visualise):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(0, len(list_to_visualise)):
            if i == 0:
                pass
            elif list_to_visualise[i-1] > list_to_visualise[i]:
                list_to_visualise[i], list_to_visualise[i-1] = list_to_visualise[i-1], list_to_visualise[i]
                is_sorted = False
                yield
            yield


def selection_sort_step(list_to_visualise):
    for n in range(len(list_to_visualise)):
        min_index = n

        for i in range(n+1, len(list_to_visualise)):
            if list_to_visualise[i] < list_to_visualise[min_index]:
                min_index = i
                yield

        if min_index != n:
            list_to_visualise[n], list_to_visualise[min_index] = list_to_visualise[min_index], list_to_visualise[n]
            visualise(pygame.Vector2(((screen_width / 2) + 50), screen_width - 100), input_list2, "red")
            yield
    yield


bubble_sort = bubble_sort_step(input_list)
selection_sort = selection_sort_step(input_list2)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    try:
        next(bubble_sort)
    except StopIteration:
        pass

    try:
        next(selection_sort)
    except StopIteration:
        pass

    # Visualize both lists
    visualise(pygame.Vector2(100, (screen_width / 2) - 50), input_list, "black")
    visualise(pygame.Vector2(((screen_width / 2) + 50), screen_width - 100), input_list2, "red")

    pygame.display.flip()
    pygame.time.delay(delay_ms)

pygame.quit()








