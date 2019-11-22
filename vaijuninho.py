import pygame
import sprites
from all_sprites import *
pygame.init()


# função pra facilitar o carregamento da imagem
def load_imagem(caminho):
    return pygame.image.load(caminho).convert_alpha()


def redraw_background():
    screen.blit(background, (0, 0))


def redraw_knight(x, y):
    screen.blit(knight, (x, y))


def change_sprite(tipo, posição):
    knight = load_imagem(tipo[posição])
    return knight
# tipo: se refere a tipo de ação ou a própria lista de movimento
# posição: referente ao numero do sprite

largura = 800
altura = 450
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Projeto Final')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

global knight
knight = load_imagem(s_inicial)
background = load_imagem(s_background)

pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont(None, 55)
clock = pygame.time.Clock()
counter, text = 180000, ' 03:00'.rjust(3)

x, y = 0, 300  # posição inicial do personagem
x_speed = y_speed = 2
move_sprite = ViraVira = False
lado = "right"
pos = 0

pressed_up = pressed_down = pressed_left = pressed_right = False

run = init = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            counter -= 1000
            if counter >= 0:
                minutos = int(counter/60000)
                segundos = int((counter/1000)-minutos*60)

                minutos = str(minutos)
                segundos = str(segundos)

                if len(segundos) == 1:
                    segundos = '0'+segundos
                text = '0'+minutos+":"+segundos
            else:
                text = 'boom!'
                counter = 180000

        # aqui ele verifica se alguma tecla foi pressionado e muda a coordenada
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pressed_up = True
            if event.key == pygame.K_DOWN:
                pressed_down = True
            if event.key == pygame.K_LEFT:
                pressed_left = True
            if event.key == pygame.K_RIGHT:
                pressed_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                pressed_up = False
            if event.key == pygame.K_DOWN:
                pressed_down = False
            if event.key == pygame.K_LEFT:
                pressed_left = False
            if event.key == pygame.K_RIGHT:
                pressed_right = False

        # aqui ele sai do loop quando aperta no "X"
        if event.type == pygame.QUIT:
            run = False

    if pressed_up:
        y -= y_speed
        move_sprite = True

    if pressed_down:
        y += y_speed
        move_sprite = True

    if pressed_left:
        x -= x_speed
        if lado == "right":
            ViraVira = True
            lado = "left"
        move_sprite = True

    if pressed_right:
        x += x_speed
        if lado == "left":
            ViraVira = True
            lado = "right"
        move_sprite = True


    if move_sprite == True:  # verifica se teve movimento
        if pos == 48:
            pos = 0
            knight = change_sprite(sprite_walk, pos)
        else:
            if pos % 8 == 0:
                knight = change_sprite(sprite_walk, pos)
            pos += 1
    move_sprite = False


    if ViraVira == True:
        knight = pygame.transform.flip(knight, True, False)
        ViraVira = False

    redraw_background()  # redesenhando a tela de fundo
    redraw_knight(x, y)  # redesenhando o personagem na posição (x, y)

    screen.blit(font.render(text, True, WHITE), [600, 0])  # desenhando o cronometro na tela na posição (600, 0)

    pygame.display.flip()  # Atualizando a tela
    clock.tick(60)  # aqui eu garanto que o programa fique rodando a 60 fps

pygame.quit()
