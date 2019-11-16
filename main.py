import pygame
pygame.init()

largura = 800
altura = 450
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Projeto Final')

background = pygame.image.load("sprites/background-menu(800:450).jpg").convert_alpha()

def redraw_background():
    screen.blit(background, (0, 0))

run = init = True

while run:
    redraw_background()

    # aqui ele sai do loop quando aperta no "X"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()