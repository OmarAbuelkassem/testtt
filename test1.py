import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
game_Active = True
clock = pygame.time.Clock()

while game_Active:
    # Quiting Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_Active = False
    pygame.display.update()
    clock.tick(60)

pygame.quit()
