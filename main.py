import pygame
import os
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

## images
BG = pygame.transform.scale\
    (pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))
Corona = pygame.image.load(os.path.join("assets", "corona.png"))
Syringe = pygame.image.load(os.path.join("assets", "syringecorona.png"))
MPLAYER = pygame.transform.scale\
    (pygame.image.load(os.path.join("assets", "maleplayer.png")), (50, 50))


class Player: ## MAIN PLAYER CLASS
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.player_img = MPLAYER
        self.syringe_img = None
        self.syringe = []
        self.cdr = 0


    def draw(self, window):
        window.blit(self.player_img, (self.x, self.y))





def main():
    run = True
    FPS = 60
    wave = 1
    lives = 1
    game_font = pygame.font.SysFont("Lobster", 40)
    clock = pygame.time.Clock()

    player = Player(0, WIDTH/2) ## maybe wrong
    velocity =  4


    def draw_window():
        WIN.blit(BG, (0, 0))
        wave_label = game_font.render(f"Wave {wave}", 1, (255, 255, 255))
        WIN.blit(wave_label, (10, 10))
        player.draw(WIN)
        pygame.display.update()

    while run:
        clock.tick(FPS)
        draw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and ((player.y + velocity) > 0):
            player.y -= velocity

        elif keys[pygame.K_s] and ((player.y + velocity + 50) < HEIGHT):
            player.y += velocity

        elif keys[pygame.K_a] and ((player.x - velocity) > 0):
            player.x -= velocity

        elif keys[pygame.K_d] and ((velocity + player.x + 50) < WIDTH):
            player.x += velocity

main()

