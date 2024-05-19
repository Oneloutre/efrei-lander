import pygame
import random
import pygame.gfxdraw
from variables import *

# Get variables from variables.json
# Variables have been mooved to be dinamically reloaded on changes.

#Simple functions to dinamically reload colors even during the game
def platform_reloading():
    r_platform = get_var("platform_color_r")
    g_platform = get_var("platform_color_g")
    b_platform = get_var("platform_color_b")
    couleur_blanc = (r_platform, g_platform, b_platform)
    return couleur_blanc

def mountain_reloading():
    r_mountain = get_var("mountain_color_r")
    g_mountain = get_var("mountain_color_b")
    b_mountain = get_var("mountain_color_g")
    couleur_montagne = (r_mountain, g_mountain, b_mountain)
    return couleur_montagne

#End of simple functions to dinamically reload colors even during the game.


def platform_properties():
    largeur_plateforme = get_var("platform_width")
    hauteur_plateforme = get_var("platform_height")
    return largeur_plateforme, hauteur_plateforme

def spaceship_properties():
    spaceship_mass = get_var("spaceship_mass")
    spaceship_fuel = get_var("spaceship_fuel")
    spaceship_thrust = get_var("spaceship_thrust")
    return spaceship_mass, spaceship_fuel, spaceship_thrust

#          ----------------------------------------------------------------------------



def ptOnCurve(b, t):
    q = b.copy()
    for k in range(1, len(b)):
        for i in range(len(b) - k):
            q[i] = (1-t) * q[i][0] + t * q[i+1][0], (1-t) * q[i][1] + t * q[i+1][1]
    return round(q[0][0]), round(q[0][1])


def bezier(surf, b, samples, color):
    hauteur_plateforme = platform_properties()[1]
    pts = [ptOnCurve(b, i/samples) for i in range(samples+1)]
    pygame.draw.lines(surf, color, False, pts, hauteur_plateforme)


def generer_plateforme(screen):
    couleur_blanc = platform_reloading()
    largeur_plateforme, hauteur_plateforme = platform_properties()
    # Generate x1 and x2 such that x1 is always less than x2
    x1 = random.randint(0, screen.get_width() - 3 * largeur_plateforme - 85)
    x2 = random.randint(x1 + largeur_plateforme + 85, screen.get_width() - 2*largeur_plateforme)

    y1 = random.randint(620, screen.get_height() - hauteur_plateforme)


    y2=random.randint(620, screen.get_height() - hauteur_plateforme)
    while abs(y2 - y1) < hauteur_plateforme:
        y2 = random.randint(620, screen.get_height() - hauteur_plateforme)


    return x1, x2, y1, y2, hauteur_plateforme


def dessiner_plateforme(x1, x2, y1, y2, hauteur_plateforme,screen):
    pygame.draw.rect(screen, couleur_blanc, [x1, y1, largeur_plateforme, hauteur_plateforme])
    pygame.draw.rect(screen, couleur_blanc, [x2, y2, largeur_plateforme, hauteur_plateforme])

def generer_montagne(screen, x1, x2, y1, y2):
    couleur_montagne = mountain_reloading()
    largeur_plateforme, hauteur_plateforme = platform_properties()
    points = [(x1+largeur_plateforme, y1), ((x1 + x2) // 2, min(y1, y2) - 50), (x2, y2)]

    # dessiner courbe de bézier
    pygame.gfxdraw.bezier(screen, points, 1000, couleur_montagne)


def fill_mountain(screen):
    for i in range(screen.get_width()-1):
        pixel_xy = i, screen.get_height()-1
        couleur_montagne = mountain_reloading()
        couleur_blanc = platform_reloading()
        while (screen.get_at(pixel_xy) != couleur_montagne) and (screen.get_at(pixel_xy) != couleur_blanc):
            pixel_xy = pixel_xy[0], pixel_xy[1]-1
        pygame.draw.line(screen, couleur_montagne, pixel_xy, (i, screen.get_height()-1))


def get_relief_coord(screen):
    relief_coord=[]
    for i in range(screen.get_width()-1):
        pixel_xy = i, screen.get_height()-1
        couleur_montagne = mountain_reloading()
        couleur_blanc = platform_reloading()
        while (screen.get_at(pixel_xy) == couleur_montagne) or (screen.get_at(pixel_xy) == couleur_blanc):
            pixel_xy = pixel_xy[0], pixel_xy[1]-1
        relief_coord.append(pixel_xy[1]+1)
    return relief_coord
