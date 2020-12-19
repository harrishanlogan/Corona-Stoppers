import pygame
import os
import time
import random

pygame.font.init()

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

## images
BG = pygame.transform.scale \
    (pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))
Corona = pygame.transform.scale \
    (pygame.image.load(os.path.join("assets", "corona.png")), (30, 30))
Syringe = pygame.image.load(os.path.join("assets", "syringecorona.png"))
MPLAYER = pygame.transform.scale \
    (pygame.image.load(os.path.join("assets", "maleplayer.png")), (50, 50))


class Player:  ## MAIN PLAYER CLASS
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.player_img = MPLAYER
        self.syringe_img = None
        self.syringe = []
        self.cdr = 0

    def draw(self, window):
        window.blit(self.player_img, (self.x, self.y))

    def get_width(self):
        return self.player_img.get_width()

    def get_height(self):
        return self.player_img.get_height()


class Enemy:
    def __init__(self, x, y, health=10):
        self.x = x
        self.y = y
        self.health = health
        self.enemy_img = None
        self.cdr = 0

    def create(self, spawn):
        spawn.blit(self.enemy_img, (self.x, self.y))


class Virus(Enemy):
    def __init__(self, x, y, health=10):
        super().__init__(x, y, health)
        self.enemy_img = Corona
        self.mask = pygame.mask.from_surface(self.enemy_img)
        self.max_health = health

    def move(self, vel):
        self.x += vel


def main():
    run = True
    FPS = 60
    wave = 1
    lives = 1
    game_font = pygame.font.SysFont("Lobster", 40)

    enemies = []
    wave_length = 5
    virus_vel = 2

    clock = pygame.time.Clock()

    player = Player(700, WIDTH / 2)  ## maybe wrong
    velocity = 4

    def draw_window():
        WIN.blit(BG, (0, 0))
        wave_label = game_font.render(f"Wave {wave}", 1, (255, 255, 255))
        WIN.blit(wave_label, (10, 10))

        for enemy in enemies:
            enemy.create(WIN)

        player.draw(WIN)

        pygame.display.update()


    while run:
        clock.tick(FPS)
        draw_window()

        if len(enemies)==0:
            wave += 1
            virus_vel += 0.25
            wave_length += 5
            for i in range(wave_length):
                enemy = Virus(random.randrange(-2000, 100), random.randrange(50, HEIGHT-100))
                enemies.append(enemy)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and ((player.y + velocity) > 0):
            player.y -= velocity

        elif keys[pygame.K_s] and ((player.y + velocity + player.get_height()) < HEIGHT):
            player.y += velocity

        elif keys[pygame.K_a] and ((player.x - velocity) > 0):
            player.x -= velocity

        elif keys[pygame.K_d] and ((velocity + player.x + player.get_width()) < WIDTH):
            player.x += velocity

        for rona in enemies:
            rona.move(virus_vel)



main()
