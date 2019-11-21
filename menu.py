import pygame
pygame.init()

def load_imagem(caminho):
    return pygame.image.load(caminho).convert_alpha()

def redraw_background():
    screen.blit(background, (0, 0))

largura = 800
altura = 450
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Projeto Final')

background = load_imagem("sprites/background-menu(800:450).jpg")

run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    redraw_background()

    pygame.display.flip()