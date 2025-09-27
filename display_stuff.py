import os

import pygame

# Display
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 294
bg = pygame.image.load("assets/images/parallax-forest-back-trees.png")

#images

miles_img = pygame.image.load("assets/images/run1.png")
miles2_img = pygame.image.load("assets/images/run2.png")
miles3_img = pygame.image.load("assets/images/run3.png")
jump_img = pygame.image.load("assets/images/jump1.png")
jump2_img = pygame.image.load("assets/images/jump2.png")
enemy_img = pygame.image.load("assets/images/enemy1.png")

#masks

miles_mask = pygame.mask.from_surface(miles_img)
miles2_mask = pygame.mask.from_surface(miles2_img)
jump_mask = pygame.mask.from_surface(jump_img)
enemy_mask = pygame.mask.from_surface(enemy_img)

#fonts

font = os.path.join(os.path.dirname(__file__), 'assets\Fonts\MinecraftTen-VGORe.ttf')
