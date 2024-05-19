from functions import *
import pygame
import sys
import math

size_x = get_var("screen_width")
size_y = get_var("screen_height")

print(type(size_x))
screen = pygame.display.set_mode((size_x, size_y))
#Assets
background_image = pygame.image.load("Assets/space.png").convert()
fuel_image = pygame.image.load("Assets/fuel.png").convert_alpha()
main_bg = pygame.image.load("Assets/menu bg.png").convert()
guide_img = pygame.image.load("Assets/guide.png").convert()
#text
font = pygame.font.Font("Assets/ethnocentric rg.otf",16)
font_play = pygame.font.Font("Assets/ethnocentric rg.otf",30)
font_menu = pygame.font.Font("Assets/ethnocentric rg.otf",60)
icon = pygame.image.load("Assets/lander.png")

def game_launching():
    pygame.display.set_caption("Efrei Lander")
    #Pour les étoiles
    etoiles = [(random.randint(0, size_x), random.randint(0, size_y)) for _ in range(100)]
    # Coordonnées de la lune
    x_lune = size_x
    y_lune = size_y
    # Rayon de la lune
    rayon_lune = get_var("moon_radius")
    #fuel du vaisseau
    fuel = get_var("spaceship_fuel")
    #angle de départ
    angle = 0
    #vitesse de départ
    speed = 5
    #gravité
    gravity = get_var("gravity")
    #icon rect
    icon_rect = icon.get_rect()
    icon_rect.center = (size_x // 2, size_y // 2)
    #clock initialization
    clock = pygame.time.Clock()
    #Pre-valls
    user_impact = 0
    right_pressed = False
    left_pressed = False
    up_pressed = False
    z_pressed = False
    velocity_x = 0
    velocity_y = 0

    image_lune = pygame.image.load('Assets/planet.png').convert_alpha()
    image_lune = pygame.transform.scale(image_lune, (rayon_lune*2, rayon_lune*2))  # Ajuster la taille de l'image
    running = True
    screen.blit(background_image, (0, 0))
    x1, x2, y1, y2, hauteur_plateforme = generer_plateforme(screen)
    mountain_coords = get_relief_coord(screen)
    print(mountain_coords)
    largeur_plateforme = get_var("platform_width")

    while running:

        screen.blit(background_image, (0, 0))

        screen.blit(image_lune, (x_lune - rayon_lune, y_lune - rayon_lune))

        dessiner_plateforme(x1, x2, y1, y2, screen)
        generer_montagne(screen, x1, x2, y1, y2)
        generer_montagne(screen, x2, 1280, y2, 650)
        generer_montagne(screen, 0 - largeur_plateforme, x1, 500, y1)

        fill_mountain(screen)
        rotated_icon = pygame.transform.rotate(icon, angle)
        rotated_rect = rotated_icon.get_rect(center=icon_rect.center)

        screen.blit(fuel_image, (40, 40))
        screen.blit(rotated_icon, rotated_rect)
        text_fuel = font.render(str(fuel), True, (255, 255, 255))
        fuel_rect = text_fuel.get_rect()
        fuel_rect.topleft = (140, 60)
        screen.blit(text_fuel, fuel_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    right_pressed = True
                elif event.key == pygame.K_LEFT:
                    left_pressed = True
                elif event.key == pygame.K_UP:
                    z_pressed = True
                    up_pressed = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    right_pressed = False
                elif event.key == pygame.K_LEFT:
                    left_pressed = False
                elif event.key == pygame.K_UP:
                    z_pressed = False
                    up_pressed = False

        if z_pressed and fuel != 0:
            fuel -= 1
            pygame.time.delay(100)
        pygame.display.update()
        if left_pressed:
            angle += 1
        if right_pressed:
            angle -= 1

        if up_pressed:
            velocity_x = -speed * math.sin(math.radians(angle))
            velocity_y = -speed * math.cos(math.radians(angle))
            print(math.sin(math.radians(angle)))
            user_impact = 0.2

        velocity_y += gravity
        icon_rect.x += velocity_x
        icon_rect.y += velocity_y

        pygame.display.flip()
        clock.tick(60)



    pygame.quit()


def main_menu():
    menu_running = True

    while menu_running:
        # background
        screen.blit(main_bg, (0, 0))

        # title

        # play_text
        play_text = font_play.render("Play", True, (255, 255, 255))
        play_rect = play_text.get_rect()
        play_rect.topleft = (580, size_y / 2)
        screen.blit(play_text, play_rect)

        # guide_text
        guide_text = font_play.render("Guide", True, (255, 255, 255))
        guide_rect = guide_text.get_rect()
        guide_rect.topleft = (575, 450)
        screen.blit(guide_text, guide_rect)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        if play_rect.collidepoint((mouse_x, mouse_y)):
            play_text = font_play.render("Play", True, (17, 119, 182))
            play_rect = play_text.get_rect()
            play_rect.topleft = (580, size_y / 2)
            screen.blit(play_text, play_rect)

        if guide_rect.collidepoint((mouse_x, mouse_y)):
            guide_text = font_play.render("Guide", True, (17, 119, 182))
            guide_rect = guide_text.get_rect()
            guide_rect.topleft = (575, 450)
            screen.blit(guide_text, guide_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint((mouse_x, mouse_y)):
                    return "game"
                elif guide_rect.collidepoint((mouse_x, mouse_y)):
                    return "guide"

        pygame.display.update()


def guide_ui():
    running = True

    while running:
        screen.blit(guide_img, (0, 0))


        play_text = font_play.render("Back", True, (0, 0, 0))
        play_rect = play_text.get_rect()
        play_rect.topleft = (100, 600)
        screen.blit(play_text, play_rect)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        if play_rect.collidepoint((mouse_x, mouse_y)):
            play_text = font_play.render("Back", True, (17, 119, 182))
            play_rect = play_text.get_rect()
            play_rect.topleft = (100, 600)
            screen.blit(play_text, play_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint((mouse_x, mouse_y)):
                    return
        pygame.display.update()
