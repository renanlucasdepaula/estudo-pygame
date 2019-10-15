# Módulos para importação
from typing import Tuple

import pygame
import sys

#iniciar o modulo do pygame para usar as funções dele

pygame.init()

#importar fonte

fonte = pygame.font.SysFont(None, 55)

#definir cor teste

WHITE = (255, 255, 255)

#Comando para abrir a janela do jogo / menu

screen = pygame.display.set_mode((640,480))


#Função para renderizar o texto

saida = fonte.render('Delete o gandalf!', True, WHITE)

#definir o titulo do display

pygame.display.set_caption("GANDALF NA DANCINHA")

#renderizar na tela o texto

screen.blit(saida, [10, 10])

#carregar imagens

gandalf = pygame.image.load("gandalf.png")
gandalf2 = pygame.image.load("gandalf2.png")

#desenhar

pygame.draw.line(screen, WHITE, [0, 100], [800, 5], 1)

screen.blit(gandalf, (10, 100))

#a cereja do bolo = musica tocando infinitamente até sair do programa

pygame.mixer.music.load('song.mp3')
pygame.mixer.music.play(-1)

pygame.display.flip()

quit = False

while not quit:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            pygame.display.flip()
            screen.blit(gandalf2,(10,100))
        elif event.type == pygame.KEYDOWN:
            pygame.display.flip()
            screen.blit(gandalf,(10,100))
            if event.key == pygame.K_DELETE:
                sys.exit()






    









