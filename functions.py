import pygame
import random
import pygame.gfxdraw

global couleur_blanc
couleur_blanc = (230, 140, 190)
global couleur_verte
couleur_verte = (100, 230, 30)
global largeur_plateforme
largeur_plateforme = 100
global hauteur_plateforme
hauteur_plateforme = 5  # Hauteur fixe

def ptOnCurve(b, t):
    q = b.copy()
    for k in range(1, len(b)):
        for i in range(len(b) - k):
            q[i] = (1-t) * q[i][0] + t * q[i+1][0], (1-t) * q[i][1] + t * q[i+1][1]
    return round(q[0][0]), round(q[0][1])

def bezier(surf, b, samples, color):
    pts = [ptOnCurve(b, i/samples) for i in range(samples+1)]
    pygame.draw.lines(surf, color, False, pts, hauteur_plateforme)

def generer_plateforme(screen):
    # Generate x1 and x2 such that x1 is always less than x2
    x1 = random.randint(0, screen.get_width() - 2 * largeur_plateforme - 85)
    x2 = random.randint(x1 + largeur_plateforme + 85, screen.get_width() - largeur_plateforme)

    y1 = random.randint(620, screen.get_height() - hauteur_plateforme)
    pygame.draw.rect(screen, couleur_blanc, [x1, y1, largeur_plateforme, hauteur_plateforme])

    y2=random.randint(620, screen.get_height() - hauteur_plateforme)
    while abs(y2 - y1) < hauteur_plateforme:
        y2 = random.randint(620, screen.get_height() - hauteur_plateforme)

    pygame.draw.rect(screen, couleur_verte, [x2, y2, largeur_plateforme, hauteur_plateforme])
    return x1, x2, y1, y2, hauteur_plateforme




def generer_montagne(screen, x1, x2, y1, y2):
    points = [(x1+largeur_plateforme, y1), ((x1 + x2) // 2, min(y1, y2) - 50), (x2, y2)]

    # Draw the bezier curve
    pygame.gfxdraw.bezier(screen, points, 100, couleur_verte)