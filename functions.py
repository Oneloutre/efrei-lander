import pygame
import random

def generer_plateforme(screen, plateformes_compteur=2):
    couleur_blanc = (230, 140, 190)
    couleur_verte = (100, 230, 30)
    largeur_plateforme = 100
    hauteur_plateforme = 5  # Hauteur fixe
    x1 = random.randint(0, screen.get_width() - largeur_plateforme)
    y1 = random.randint(620, screen.get_height() - hauteur_plateforme)
    pygame.draw.rect(screen, couleur_blanc, [x1, y1, largeur_plateforme, hauteur_plateforme])

    x2 = random.randint(0, screen.get_width() - largeur_plateforme)
    while abs(x2 - x1) < largeur_plateforme+85:
        x2 = random.randint(0, screen.get_width() - largeur_plateforme)
    y2=random.randint(620, screen.get_height() - hauteur_plateforme)
    while abs(y2 - y1) < hauteur_plateforme:
        y2 = random.randint(620, screen.get_height() - hauteur_plateforme)
    pygame.draw.rect(screen, couleur_verte, [x2, y2, largeur_plateforme, hauteur_plateforme])
    return x1, x2, largeur_plateforme
