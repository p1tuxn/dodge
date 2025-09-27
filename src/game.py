import pygame

from display_stuff import SCREEN_WIDTH, SCREEN_HEIGHT, enemy_mask, miles_mask, bg, font
from src.enemy import Enemy
from src.player import Player

pygame.init()
pygame.mixer.init()

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("dodge")
        self.icon = pygame.image.load("assets/images/run1.png")
        pygame.display.set_icon(self.icon)
        self.clock = pygame.time.Clock()
        self.running = True
        self.score_value = 1
        self.pause = False
        self.game_over = False

        # load music
        pygame.mixer.music.load("assets/music/original-tetris-theme-tetris-soundtrack.wav")
        pygame.mixer.music.play(-1)
        self.pause_font = pygame.font.Font(font, 32)
        self.font = pygame.font.Font(font, 20)
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

    def draw_gameover_screen(self):
        highscore = str(self.score_value)
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.fill((255, 105, 97))
        overlay.set_alpha(128)
        self.screen.blit(overlay, (0, 0))
        pause_text = self.pause_font.render("Game Over", True, (255, 255, 255))
        self.screen.blit(pause_text, (176, 123))
        retry_text = self.font.render("Press R to Restart", True, (255, 255, 255))
        self.screen.blit(retry_text, (162, 160))
        quit_text = self.font.render("Press Q to Quit", True, (255, 255, 255))
        self.screen.blit(quit_text, (183, 180))
        score_text = self.font.render(f"highscore: {highscore}", True, (255, 255, 255))
        self.screen.blit(score_text, (188, 94))

    def draw_bg(self):
        self.screen.blit(bg, (0, 0))

    def draw_score(self):
        score = self.font.render('score:' + str(self.score_value), True, (0, 0, 0))
        self.screen.blit(score, (380, 20))

    def draw_pause_menu(self):
        # Pause menu overlay
        overlay = pygame.Surface((200, 200))
        overlay.fill((0, 0, 0))
        overlay.set_alpha(128)
        self.screen.blit(overlay, (150, 55))
        pause_text = self.pause_font.render("PAUSED", True, (255, 255, 255))
        self.screen.blit(pause_text, (185,123))
        resume_text = self.font.render("Press P to Resume", True, (255, 255, 255))
        self.screen.blit(resume_text, (158, 160))
        quit_text = self.font.render("Press Q to Quit", True, (255, 255, 255))
        self.screen.blit(quit_text, (172, 183))

    def run(self):
        while self.running:
            self.clock.tick(45)
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
                    if self.game_over:
                        if event.key == pygame.K_q:
                            self.running = False
                        if event.key == pygame.K_r:
                            ticks = 0
                            self.game_over = False
                            self.pause = False


            keys = pygame.key.get_pressed()

            if not self.pause and not self.game_over:
                self.score_value += 1
                self.player.update(keys)
                self.enemy.update(ticks)
                self.collision()

            self.draw_bg()
            self.enemy.draw(self.screen)
            self.player.draw(self.screen, ticks, self.pause, self.game_over)
            self.draw_score()
            if self.pause:
                self.draw_pause_menu()
            if self.game_over:
                self.draw_gameover_screen()

            pygame.display.update()

        pygame.quit()

