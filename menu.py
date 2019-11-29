import pygame
import sprites
pygame.init()

width = 800
height = 450
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Projeto Final')

# função pra facilitar o carregamento da imagem
def load_imagem(image):
    return pygame.image.load(image).convert_alpha()

button_play = load_imagem("sprites/play.png")

button_credits = load_imagem("sprites/credits.png")

back_menu = load_imagem("sprites/background.jpg")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# aqui eu estou setando um tempo de 1000 milisegundos para esse evento
# ser chamado a cada segundo
# pygame.time.set_timer(pygame.USEREVENT, 1000)

# aqui eu defino uma fonte
# font = pygame.font.SysFont(None, 55)

#3 minutos equivale a 180.000 milisegundos
clock = pygame.time.Clock()
# counter, text = 180000, ' 03:00'.rjust(3)


def menu(screen):
	global play_press, credits_press

	screen.blit(back_menu, (0,0))
	play_press = screen.blit(button_play, (300, 200))
	credits_press = screen.blit(button_credits, (285, 350))

run = True
initial = True

while run:

    if initial:
        menu(screen)

    for event in pygame.event.get():
        # aqui ele sai do loop quando aperta no "X"
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip() # Atualizando a tela
    clock.tick(60) # aqui eu garanto que o programa fique rodando a 60 fps (ui que xiqui !!)

pygame.quit()