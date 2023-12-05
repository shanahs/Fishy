import pygame
import sys
import os

# Initialisation de Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SPEED = 2
ROTATION_SPEED = 5
SCROLL_SPEED = 1

# Chemins des images
current_path = os.path.dirname(__file__)
images_path = os.path.join(current_path, "images")
player_image_path = os.path.join(images_path, "/home/shaney/Bureau/devGame/fish_type/images/canoe.png")
background_image_path = os.path.join(images_path, "/home/shaney/Bureau/devGame/fish_type/images/bang.png")

# Fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Défilement du fond")

# Joueur
player_image = pygame.image.load(player_image_path)
player_rect = player_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Fond
background_image = pygame.image.load(background_image_path)
background_rect = background_image.get_rect()

# Angle de rotation initial
rotation_angle = 0

# Position initiale du fond
background_x, background_y = 0, 0

# Boucle principale
clock = pygame.time.Clock()

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def update_game_state():
    global rotation_angle, background_x, background_y

    keys = pygame.key.get_pressed()

    # Rotation vers la gauche "q"
    if keys[pygame.K_q]:
        rotation_angle += ROTATION_SPEED

    # Rotation vers la droite "d"
    if keys[pygame.K_d]:
        rotation_angle -= ROTATION_SPEED

    # Déplacement du joueur en fonction de l'angle de rotation
    player_rect.x += PLAYER_SPEED * pygame.math.Vector2(1, 0).rotate(rotation_angle).y
    player_rect.y += PLAYER_SPEED * pygame.math.Vector2(1, 0).rotate(rotation_angle).x

    # Déplacement du fond en fonction de la position du joueur
    background_x -= SCROLL_SPEED * pygame.math.Vector2(1, 0).rotate(rotation_angle).x
    background_y -= SCROLL_SPEED * pygame.math.Vector2(1, 0).rotate(rotation_angle).y

    # Faire en sorte que le fond défile de manière infinie
    background_x %= background_rect.width
    background_y %= background_rect.height

def draw():
    # Afficher le fond en boucle
    for i in range(-1, int(WIDTH / background_rect.width) + 2):
        for j in range(-1, int(HEIGHT / background_rect.height) + 2):
            screen.blit(background_image, (background_x + i * background_rect.width, background_y + j * background_rect.height))

    # Effectuer la rotation de l'image du joueur
    rotated_player = pygame.transform.rotate(player_image, rotation_angle)
    rotated_rect = rotated_player.get_rect(center=player_rect.center)

    # Dessiner l'image du joueur rotatée au centre de l'écran
    screen.blit(rotated_player, rotated_rect.topleft)

# Boucle principale
while True:
    handle_events()
    update_game_state()
    screen.fill((0, 0, 0))  # Effacer l'écran à chaque itération
    draw()
    pygame.display.flip()
    clock.tick(60)  # Limiter la fréquence d'images à 60 FPS
