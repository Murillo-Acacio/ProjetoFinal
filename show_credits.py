from all_spritess import *
import pygame
pygame.init()

def run_credits():

    # função pra facilitar o carregamento da imagem
    def load_imagem(caminho):
        return pygame.image.load(caminho).convert_alpha()

    def redraw_background():
        screen.blit(background, (0, 0))

    width = 800
    height = 450
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Projeto Final')

    background = load_imagem(s_background_credits)

    run = True

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        redraw_background()

        pygame.display.flip()

