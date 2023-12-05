import pygame
import sys
import math

pygame.init()

# Initialisation de Pygame
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Background Control")

clock = pygame.time.Clock()

# Chargement de l'image du background
background_image = pygame.image.load("images/bang.png")
background_rect = background_image.get_rect(center=(width // 2, height // 2))

# Chargement de l'image du joueur
player_image = pygame.image.load("images/canoe.png")
player_rect = player_image.get_rect()
player_rect.center = (width // 2, height // 2)

# Position et vitesse du background
background_speed = 5
rotation_speed = 2
background_angle = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_z]:
        # Déplacement du joueur vers le haut
        player_rect.y -= background_speed

    if keys[pygame.K_q]:
        # Rotation du background vers la gauche
        background_angle += rotation_speed

    if keys[pygame.K_d]:
        # Rotation du background vers la droite
        background_angle -= rotation_speed

    # Mise à jour de la position du fond en fonction de l'angle de rotation
    rotated_background = pygame.transform.rotate(background_image, background_angle)
    rotated_rect = rotated_background.get_rect(center=player_rect.center)

    screen.fill((255, 255, 255))
    screen.blit(rotated_background, rotated_rect.topleft)

    # Affichage du joueur
    screen.blit(player_image, player_rect.topleft)

    pygame.display.flip()
    clock.tick(30)
