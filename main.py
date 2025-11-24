#region ################# imports  #################
# - pygame
import pygame
pygame.init()

# - config
from scripts.config import Config
config = Config()

# - player
from scripts.player import *
player = Player()

#endregion ################# imports  #################

#region ################# definição inicial  #################

# define a tela e titulo
screen = pygame.display.set_mode((config.width, config.height))
pygame.display.set_caption(config.title)

# define variavel de execução
running = True

#endregion ################# definição inicial  #################



# enquanto tal variavel estiver verdadeira roda o jogo
while running:

    #region ################# detectar eventos  #################

    # detecta se evento de desligamento ocorre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # detecta se pressionado tecla
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    # detecta pressionar de teclas 
    pressed_keys = pygame.key.get_pressed()

    #endregion ################# detectar eventos  #################

    #region ################# atualizar obj  #################

    player.update(pressed_keys)

    #endregion ################# atualizar obj  #################


    #region ################# desenhar tela #################
                
    # preenche a tela com a cor de fundo
    screen.fill(config.bg_color)

    # desenha o player na tela
    screen.blit(player.surf, player.rect)

    # atualiza a tela
    pygame.display.flip()

    #endregion ################# desenhar tela #################

    

# para a execução do codigo
pygame.quit()