import pygame

# Display
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400

#images
crouch_img = pygame.image.load("assets/images/Mancrouch.png")
crouch2_img = pygame.image.load("assets/images/Mancrouch2.png")
miles_img = pygame.image.load("assets/images/Man.png")
miles2_img = pygame.image.load("assets/images/Man2.png")
jump_img = pygame.image.load("assets/images/Manjump.png")

enemy_img = pygame.image.load("assets/images/policeman.png")

#masks
crouch_rect = crouch_img.get_rect()
crouch2_rect = crouch2_img.get_rect()
miles_rect = miles_img.get_rect()
miles2_rect = miles2_img.get_rect()
jump_rect = jump_img.get_rect()
enemy_rect = enemy_img.get_rect()

crouch_mask = pygame.mask.from_surface(crouch_img)
crouch2_mask =pygame.mask.from_surface(crouch2_img)
miles_mask = pygame.mask.from_surface(miles_img)
miles2_mask = pygame.mask.from_surface(miles2_img)
jump_mask = pygame.mask.from_surface(jump_img)
enemy_mask = pygame.mask.from_surface(enemy_img)

