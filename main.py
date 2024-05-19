import pygame
pygame.init()
from misc_files.game_launching import *
import sys
import math
from game_launching import game_launching



if __name__ == '__main__':
    while True:
        bg_music.play()
        next_action = main_menu()
        if next_action == "game":
            game_launching()
        elif next_action == "guide":
            guide_ui()

