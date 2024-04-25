import pygame,sys,random
from pygame.math import Vector2
from object import *


class PLAYER():
    def __init__(self):
        self.death_sound = pygame.mixer.Sound('Sound/crash.mp3')
        self.background_music = pygame.mixer.Sound('Sound/bg_music_1.mp3')
        self.play_background_music()
            
    def play_death_sound(self):
        self.death_sound.play()
        self.death_sound.set_volume(0.5)
    def play_background_music(self):
         self.background_music.play()
         self.background_music.set_volume(0.2)


    def show_game_over(self, snake_length, screen):
        self.snake_length = snake_length
        self.screen = screen
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game is over! Your score is {self.snake_length}", True, (255, 255, 255))
        self.screen.blit(line1, (200, 300))
        line2 = font.render("To play again press Enter. To exit press Escape!", True, (255, 255, 255))
        self.screen.blit(line2, (200, 350))
        pygame.display.flip()