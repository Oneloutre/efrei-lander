import pygame
pygame.init()
from misc_files.game_launching import *


if __name__ == '__main__':
    while True:
        next_action = main_menu()
        if next_action == "game":
            game_launching()
        elif next_action == "guide":
            guide_ui()
