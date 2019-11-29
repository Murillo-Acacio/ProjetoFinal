from vaijuninho import game
from show_credits import run_credits
from all_spritess import *
import sprites
import pygame
pygame.init()

width = 800
height = 450
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Projeto Final')


# função pra facilitar o carregamento da imagem
def load_imagem(image):
    return pygame.image.load(image).convert_alpha()


button_play = load_imagem(s_play)
button_credits = load_imagem(s_credits)
back_menu = load_imagem(s_background_menu)


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()


def menu():
    global play_press, credits_press
    screen.blit(back_menu, (0, 0))
    play_press = screen.blit(button_play, (300, 200))
    credits_press = screen.blit(button_credits, (285, 350))


run = True
initial = True
button_pressed = False

while run:

    if initial:
        menu()

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            button_pressed = True

        if event.type == pygame.QUIT:
            run = False

    if button_pressed: # aqui eu verifico se o play foi
        mouse = pygame.mouse.get_pos()
        if mouse[0] > 314 and mouse[0] < 481:
            if mouse[1] > 214 and mouse[1] < 274:
                game()
        if mouse[0] > 294 and mouse[0] < 502:
            if mouse[1] > 361 and mouse[1] < 407:
                run_credits()
        button_pressed = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
