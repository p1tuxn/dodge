import pygame
from display_overlays import miles_img, miles2_img, crouch_img, crouch2_img, jump_img

class Player:
    def __init__(self):
        self.Miles_x = 130
        self.Miles_y = 78
        self.initial_velocity = 0
        self.jump = False
        self.on_ground = True
        self.g = 0.8
        self.velocity = -13.9
        self.crouch = False

    def update(self, keys):
        # jumping
        if keys[pygame.K_SPACE] and self.on_ground:
            self.initial_velocity = self.velocity
            self.on_ground = False
            self.jump = True

        if not self.on_ground:
            self.initial_velocity += self.g

        self.Miles_y += self.initial_velocity

        if self.Miles_y >= 78:
            self.Miles_y = 78
            self.initial_velocity = 0
            self.on_ground = True
            self.jump = False

        # crouch
        if keys[pygame.K_c] and self.on_ground:
            self.crouch = True
        if not keys[pygame.K_c] and self.on_ground:
            self.crouch = False

    def draw(self, screen, ticks, pause):
        if pause:
            if not self.crouch and self.on_ground:
                screen.blit(miles_img, (self.Miles_x, self.Miles_y))
            if self.crouch:
                screen.blit(crouch_img, (self.Miles_x, self.Miles_y))
            else:
                screen.blit(jump_img, (self.Miles_x, self.Miles_y))
        else:
            # When not paused: Original animation logic
            if self.crouch and not self.jump and ticks % 2 == 0:
                screen.blit(crouch_img, (self.Miles_x, self.Miles_y))
            elif self.crouch and not self.jump and ticks % 2 != 0:
                screen.blit(crouch2_img, (self.Miles_x, self.Miles_y))
            elif not self.jump and not self.crouch and ticks % 2 == 0:
                screen.blit(miles_img, (self.Miles_x, self.Miles_y))
            elif not self.jump and not self.crouch and ticks % 2 != 0:
                screen.blit(miles2_img, (self.Miles_x, self.Miles_y))
            elif self.jump and not self.crouch:
                screen.blit(jump_img, (self.Miles_x, self.Miles_y))

