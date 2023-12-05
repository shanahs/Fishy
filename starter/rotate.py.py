import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définir la fenêtre
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rotation du joueur")

# Charger l'image du joueur

player_image = pygame.image.load("images/canoe.png")

player_rect = player_image.get_rect()
player_rect.center = (width // 2, height // 2)

# Angle de rotation initial
rotation_angle = 0

# Boucle principale
clock = pygame.time.Clock()
while True:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Obtenir les touches pressées
    keys = pygame.key.get_pressed()

    # Rotation vers la gauche en appuyant sur la touche "q"
    if keys[pygame.K_q]:
        rotation_angle += 5  # Ajustez la vitesse de rotation selon vos besoins

    # Rotation vers la droite en appuyant sur la touche "d"
    if keys[pygame.K_d]:
        rotation_angle -= 5  # Ajustez la vitesse de rotation selon vos besoins

    # Effectuer la rotation de l'image du joueur
    rotated_player = pygame.transform.rotate(player_image, rotation_angle)
    rotated_rect = rotated_player.get_rect(center=player_rect.center)

    # Dessiner l'image du joueur rotatée sur l'écran
    screen.blit(rotated_player, rotated_rect.topleft)

    pygame.display.flip()
    clock.tick(60)  # Limiter la fréquence d'images à 60 FPS
