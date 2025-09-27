import pygame
from display_overlays import SCREEN_WIDTH, SCREEN_HEIGHT, miles_img, miles2_img, crouch_img, crouch2_img, jump_img, enemy_mask, miles_mask, miles2_mask, jump_mask,crouch_mask,crouch2_mask
from src.player import Player
from src.enemy import Enemy

pygame.init()
pygame.mixer.init()

class Game():
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("dodge")
        self.icon = pygame.image.load("assets/images/Man.png")
        pygame.display.set_icon(self.icon)
        self.clock = pygame.time.Clock()
        self.running = True
        self.score_value = 1
        self.pause = False
        self.game_over = False

        # load music
        pygame.mixer.music.load("assets/music/original-tetris-theme-tetris-soundtrack.wav")
        pygame.mixer.music.play(-1)

        self.font = pygame.font.Font("freesansbold.ttf", 20)
        self.pause_font = pygame.font.Font("freesansbold.ttf", 32)
        self.player = Player()
        self.enemy = Enemy()

    def collision(self):
        player_x = self.player.Miles_x
        player_y = self.player.Miles_y
        enemy_x = self.enemy.enemy_x
        enemy_y = self.enemy.enemy_y
        offset = (enemy_x - player_x, enemy_y - player_y)
        if miles_mask.overlap(enemy_mask, offset):
            self.game_over = True

    def draw_bg(self):
        height = self.screen.get_height()
        for y in range(height):
            ratio = y / height
            r = int(0 * (1 - ratio) + 0 * ratio)
            g = int(255 * (1 - ratio) + 0 * ratio)
            b = int(255 * (1 - ratio) + 0 * ratio)
            pygame.draw.line(self.screen, (r, g, b), (0, y), (self.screen.get_width(), y))

    def draw_ground(self):
        pygame.draw.line(self.screen, (255, 255, 255), (0, 170), (SCREEN_WIDTH, 170))

    def draw_score(self):
        score = self.font.render('score:' + str(self.score_value), True, (0, 0, 0))
        self.screen.blit(score, (270, 20))

    def draw_pause_menu(self):
        # Pause menu overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.fill((0, 0, 0))
        overlay.set_alpha(128)
        self.screen.blit(overlay, (0, 0))
        pause_text = self.pause_font.render("PAUSED", True, (255, 255, 255))
        self.screen.blit(pause_text, (130, 30))
        resume_text = self.font.render("Press P to Resume", True, (255, 255, 255))
        self.screen.blit(resume_text, (100, 70))
        quit_text = self.font.render("Press Q to Quit", True, (255, 255, 255))
        self.screen.blit(quit_text, (100, 100))

    def run(self):
        while self.running:
            self.clock.tick(60)
            ticks = int(pygame.time.get_ticks() / 100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p and not self.game_over:
                        self.pause = not self.pause
                        if self.pause:
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.unpause()
                    if self.pause:
                        if event.key == pygame.K_q:
                            self.running = False

            keys = pygame.key.get_pressed()

            if not self.pause and not self.game_over:
                self.score_value += 1
                self.player.update(keys)
                self.enemy.update(ticks)
                self.collision()

            self.draw_bg()
            self.draw_ground()
            self.enemy.draw(self.screen)
            self.player.draw(self.screen, ticks, self.pause)
            self.draw_score()
            if self.pause:
                self.draw_pause_menu()

            pygame.display.update()

        pygame.quit()


