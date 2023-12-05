import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
width, height = 800, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jeu Pygame")

# Paramètres du joueur
player_size = 50
player_x = width // 2 - player_size // 2
player_y = height // 2 - player_size // 2

# Charger l'image du cube
cube_image = pygame.image.load("images/boat.png")

# Dictionnaire des images pour différentes directions
player_images = {
    "left": pygame.image.load("images/bag.png"),
    "right": pygame.image.load("images/bag.png"),
    "up": pygame.image.load("images/canoe.png"),
    "down": pygame.image.load("images/canoe.png"),
}

current_direction = "down"  # Direction initiale du joueur

# Boucle principale du jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Gestion des mouvements du joueur
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        player_x -= 5
        current_direction = "left"
    if keys[pygame.K_d]:
        player_x += 5
        current_direction = "right"
    if keys[pygame.K_z]:
        player_y -= 5
        current_direction = "up"
    if keys[pygame.K_s]:
        player_y += 5
        current_direction = "down"

    # Dessiner le joueur
    win.fill((255, 255, 255))  # Effacer l'écran
    win.blit(player_images[current_direction], (player_x, player_y))

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Limiter la fréquence d'images pour ne pas surcharger le processeur
    pygame.time.Clock().tick(30)

player_x = width // 2 - player_size // 2
player_y = height // 2 - player_size // 2

# Charger l'image du joueur
player_image = pygame.image.load("images/canoe.png")
player_rect = player_image.get_rect(center=(player_x, player_y))

# Angle de rotation initial
angle = 0

# Boucle principale du jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Gestion des mouvements du joueur
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        player_x -= 5
        angle = 90  # Rotation vers la gauche
    elif keys[pygame.K_d]:
        player_x += 5
        angle = -90  # Rotation vers la droite

    # Dessiner le joueur
    win.fill((255, 255, 255))  # Effacer l'écran
    rotated_player = pygame.transform.rotate(player_image, angle)
    new_rect = rotated_player.get_rect(center=player_rect.center)
    win.blit(rotated_player, new_rect.topleft)

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Limiter la fréquence d'images pour ne pas surcharger le processeur
    pygame.time.Clock().tick(30)
