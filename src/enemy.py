import pygame
import random
from display_overlays import enemy_img

class Enemy:
    def __init__(self):
        self.enemy_x = 400
        self.enemy_y = random.randint(75, 150)
        self.enemy_speed = 3

    def update(self, ticks):
        self.enemy_x -= self.enemy_speed
        if ticks % 50 == 0:
            self.enemy_x = 500
            self.enemy_y = random.randint(75, 150)

    def draw(self, screen):
        screen.blit(enemy_img, (self.enemy_x, self.enemy_y))


