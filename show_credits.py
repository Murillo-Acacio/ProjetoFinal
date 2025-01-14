from all_spritess import *
import pygame
import sys
pygame.init()

def run_credits():

    # função pra facilitar o carregamento da imagem
    def load_image(image):
        return pygame.image.load(image).convert_alpha()

    def redraw_background():
        screen.blit(background, (0, 0))

    width = 800
    height = 450
    screen = pygame.display.set_mode((width, height))

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    background = load_image(s_background_menu)
    button_back = load_image(s_back)
    pygame.mouse. set_visible(False)
    cursor = load_image(s_cursor)
    muri = load_image(murillo)
    fer = load_image(fernanda)
    van = load_image(vanessa)

    font = pygame.font.SysFont(None, 23)

    archive = open('credi.txt', 'r')
    text = archive.readlines()
    archive.close()

    run = True
    mouse_pressed = False

    while run:

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pressed = True

            if event.type == pygame.QUIT:
                run = False
                sys.exit()
                pygame.quit()

        if mouse_pressed is True:
            mouse = pygame.mouse. get_pos()
            if mouse[0] > 20 and mouse[0] < 100:
                if mouse[1] > 21 and mouse[1] < 48:
                    run = False
            mouse_pressed = False
        
        screen.fill(BLACK) # deixa o fundo preto

        if height < -680:
            height = 450

        if (height > -680):
            for i in range(len(text)):
                screen.blit(font.render(text[i].rstrip("\n"), True, WHITE), [150, (height + 20 + (i*40))])
            screen.blit(muri, [130, (height + 550)])
            screen.blit(fer, [350, (height + 550)])
            screen.blit(van, [570, (height + 550)])
            height -= 0.1

        screen.blit(button_back, [0, 0])

        if pygame.mouse. get_focused():
            mouse = pygame.mouse.get_pos()
            screen.blit(cursor, mouse)

        pygame.display.flip()
