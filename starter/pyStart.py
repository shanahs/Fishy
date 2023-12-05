import pygame

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mon Premier Jeu Pygame")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mettez à jour l'état du jeu ici

    # Dessinez les éléments à l'écran ici

    pygame.display.flip()

pygame.quit()
