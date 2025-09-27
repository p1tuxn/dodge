import pygame

from display_stuff import miles_img, miles2_img, jump_img

class Player:
    def __init__(self):
        self.Miles_x = 130
        self.Miles_y = 200
        self.initial_velocity = 0
        self.jump = False
        self.on_ground = True
        self.g = 0.8
        self.velocity = -13.9

    def update(self, keys):
        # jumping
        if keys[pygame.K_SPACE] and self.on_ground:
            self.initial_velocity = self.velocity
            self.on_ground = False
            self.jump = True

        if not self.on_ground:
            self.initial_velocity += self.g

        self.Miles_y += self.initial_velocity

        if self.Miles_y >= 200:
            self.Miles_y = 200
            self.initial_velocity = 0
            self.on_ground = True
            self.jump = False


    def draw(self, screen, ticks, pause, game_over):
        if game_over:
            if self.on_ground:
                screen.blit(miles_img, (self.Miles_x, self.Miles_y))
            elif not self.on_ground:
                screen.blit(jump_img, (self.Miles_x, self.Miles_y))
        if pause:
            if self.on_ground:
                screen.blit(miles_img, (self.Miles_x, self.Miles_y))
            elif not self.on_ground:
                screen.blit(jump_img, (self.Miles_x, self.Miles_y))
        elif not pause and not game_over:
            if not self.jump:
                if ticks % 3 == 0:
                    screen.blit(miles_img, (self.Miles_x, self.Miles_y))
                if ticks % 3 != 0:
                    screen.blit(miles2_img, (self.Miles_x, self.Miles_y))
            elif self.jump:
                screen.blit(jump_img, (self.Miles_x, self.Miles_y))


