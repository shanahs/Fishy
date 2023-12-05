import pygame
import sys

# Initialisation de Pygame
pygame.init()

# fenêtre
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Défilement du fond")

# joueur
player_image = pygame.image.load("images/canoe.png")
player_rect = player_image.get_rect()
player_rect.center = (width // 2, height // 2)

# fond
background_image = pygame.image.load("images/bang.png")
background_rect = background_image.get_rect()

# Vitesse de défilement du fond
scroll_speed = 1

# Vitesse de déplacement du joueur
player_speed = 2

# Angle de rotation initial
rotation_angle = 0

# Position initiale du fond
background_x = 0
background_y = 0

# Boucle principale
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Obtenir les touches pressées
    keys = pygame.key.get_pressed()

    # Rotation vers la gauche "q"
    if keys[pygame.K_q]:
        rotation_angle += 5  # vitesse

    # Rotation vers la droite "d"
    if keys[pygame.K_d]:
        rotation_angle -= 5  # vitesse

    # Déplacement du joueur en fonction de l'angle de rotation
    player_rect.x += player_speed * pygame.math.Vector2(1, 0).rotate(rotation_angle).y
    player_rect.y += player_speed * pygame.math.Vector2(1, 0).rotate(rotation_angle).x

    # Déplacement du fond en fonction de la position du joueur
    background_x -= scroll_speed * pygame.math.Vector2(1, 0).rotate(rotation_angle).x
    background_y -= scroll_speed * pygame.math.Vector2(1, 0).rotate(rotation_angle).y

    # Dessiner le fond
    screen.blit(background_image, (background_x, background_y))
    screen.blit(background_image, (background_x - background_rect.width, background_y))
    screen.blit(background_image, (background_x + background_rect.width, background_y))

    # Effectuer la rotation de l'image du joueur
    rotated_player = pygame.transform.rotate(player_image, rotation_angle)
    rotated_rect = rotated_player.get_rect(center=player_rect.center)

    # Dessiner l'image du joueur rotatée au centre de l'écran
    screen.blit(rotated_player, rotated_rect.topleft)

    pygame.display.flip()
    clock.tick(60)  # Limiter la fréquence d'images à 60 FPS
