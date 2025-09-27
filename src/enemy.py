import random

from display_stuff import enemy_img

class Enemy:
    def __init__(self):
        self.enemy_x = 0
        self.enemy_y = random.randint(190, 294)
        self.enemy_speed = 10

    def update(self, ticks):
        self.enemy_x -= self.enemy_speed
        if ticks % 25 == 0:
            self.enemy_y = random.randint(190, 254)
            self.enemy_x = 500

    def draw(self, screen):
        screen.blit(enemy_img, (self.enemy_x, self.enemy_y))


