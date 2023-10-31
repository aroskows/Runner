
'''
Author: Alexa Roskowski
Date Created: 10/27/23

Description: A endless runner 2d game similair to the google DinoGame using pygame

'''

import pygame
from pygame.locals import *
import sys
import random

pygame.init()


HEIGHT = 300
WIDTH = 500

FPS = 60




class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()

        self.ySpeed = 0;
        self.gravity = 1


        #used for animation
        self.images_running = [] 
        self.images_jumping = [] 

        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128, 255, 40))
        self.rect = self.surf.get_rect(center = (45, 270))


        #self.rect = pygame.Rect(5, 350, 100, 100)

    def move(self, y):
        self.rect.move_ip(0, y)





    def update(self):
        x = 0
        y = 0

        ground = pygame.sprite.spritecollideany(self, platforms)
        pressed = pygame.key.get_pressed()

        if pressed[K_SPACE]:
            print("space")


        if pressed[K_SPACE] and ground:
            #self.jump()
            self.ySpeed = -16
            print("jumped");


        if y < 10 and not ground:
            self.ySpeed += self.gravity

        if self.ySpeed > 0 and ground:
            self.ySpeed = 0

        self.move(self.ySpeed)

class platform(pygame.sprite.Sprite):
    def __init__(self, width, height, Center):
        super().__init__()
        self.surf = pygame.Surface((width, height))
        self.surf.fill((0, 0, 255))
        self.rect = self.surf.get_rect(center = Center)



class enemy(pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.surf = pygame.Surface((10, 60))
        self.surf.fill((200, 0, 150))
        self.rect = self.surf.get_rect(center = (WIDTH - 45, HEIGHT - 45))

    def update(self):
        self.rect.move_ip(-2, 0)

        if self.rect.right < 0:
            #gone off the screen:
            self.kill()

def deathscreen():
    while True:
            font = pygame.font.Font(None, 24)
            replay = font.render("press any button to replay", True, (255, 255, 255))
            font = pygame.font.Font(None, 36)

            win = font.render("YOU DIED!", True, (255, 255, 255))


            for event in pygame.event.get():
                #print("EVENT!!", event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    print("pressed")
                    return
            #text = font.render("hi", True, (255, 255, 255))
            screen.fill((190, 0, 0))
            pygame.draw.rect(screen, (0, 0, 0), [WIDTH/2-75, 100, 145, 35])
            pygame.draw.rect(screen, (0, 0, 0), [WIDTH/2-125, HEIGHT/2-10, 250, 35])
            screen.blit(replay ,(WIDTH/2-100, HEIGHT/2) )
            screen.blit(win ,(WIDTH/2-60, 105) )

            pygame.display.update()









screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("JUMP")
FramePerSec = pygame.time.Clock()






platforms = pygame.sprite.Group()
PT1 = platform(WIDTH, 20, (WIDTH/2, HEIGHT - 10))
platforms.add(PT1)

ADDENEMY = pygame.USEREVENT + 2

pygame.time.set_timer(ADDENEMY, random.randint(300, 10000))

enemies = pygame.sprite.Group()
E = enemy()
enemies.add(E)


player = Player()
all_sprites = pygame.sprite.Group()

all_sprites.add(PT1)
all_sprites.add(player)
all_sprites.add(E)



while True:
    #winscreen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == ADDENEMY:
            new_e = enemy()
            enemies.add(new_e)
            all_sprites.add(new_e)
        

    screen.fill((0, 0, 0))
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    enemies.update()

    player.update()

    if pygame.sprite.spritecollideany(player, enemies):
        #we had a collision
        for e in enemies:
            e.kill()
            #enemies.remove(e)
        deathscreen()

    #pygame.display.flip()

    pygame.display.update()
    FramePerSec.tick(FPS)



