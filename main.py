# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
flags = 0  # controlan opciones de la pantalla
fontImagePath = "/home/blanco/Documentos/game-project/assets/img/font.jpg"

screen = pygame.display.set_mode((800, 600), flags)
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    background = pygame.image.load(fontImagePath)
    backgroundPosX = screen.get_height() - background.get_height()
    backgroundPosY = screen.get_width() - background.get_width() / 2

    screen.blit(background, (backgroundPosX, backgroundPosY))

    pygame.draw.circle(screen, "red", player_pos, 10)
    pygame.mouse.set_visible(False)
    mousePosX, mousePosY = pygame.mouse.get_pos()

    player_pos.x = mousePosX
    player_pos.y = mousePosY

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
