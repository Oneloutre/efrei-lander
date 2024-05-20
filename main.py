import pygame
pygame.init()
from misc_files.game_launching import *
import sys
import math
bg_music = pygame.mixer.Sound("Assets/music_bg.wav")



if __name__ == '__main__':
    music_playing = False
    while True:
        if not music_playing:
            bg_music.play()
            music_playing = True
        next_action = main_menu()
        if next_action == "game":
            action = game_launching()
            if action == "crash":
                crash()
            elif action == "success":
                success()
        elif next_action == "guide":
            guide_ui()

