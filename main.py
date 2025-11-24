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

# - enemies
from scripts.enemies import *

# - rooms
from scripts.rooms import *

#endregion ################# imports  #################

#region ################# definição inicial  #################

# define a tela e titulo
screen = pygame.display.set_mode((config.width, config.height))
pygame.display.set_caption(config.title)

# define variavel de execução
running = True

# sprites
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# evento de criação de inimigo
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY,250)

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

        if event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        

    # detecta pressionar de teclas 
    pressed_keys = pygame.key.get_pressed()

    #endregion ################# detectar eventos  #################

    #region ################# atualizar obj  #################

    player.update(pressed_keys)

    enemies.update()

    all_sprites.add(blocks)

    #endregion ################# atualizar obj  #################


    #region ################# desenhar tela #################
                
    # preenche a tela com a cor de fundo
    screen.fill(config.bg_color)

    # desenha entidades na tela
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # atualiza a tela
        
    drawRoom(rooms["1"])

    pygame.display.flip()



    #endregion ################# desenhar tela #################

    #region ################# detectar colisões #################
    
    if pygame.sprite.spritecollideany(player,enemies):
        player.kill()
        running = False
    
    #endregion ################# detectar colisões #################
    
    #region ################# dinamic config #################
    
    clock = pygame.time.Clock()
    clock.tick(30)
    
    #endregion ################# dinamic config #################
    
    

# para a execução do codigo
pygame.quit()