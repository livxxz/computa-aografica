import pygame
import random
import sys

# inicializar o Pygame
pygame.init()

#Dimensões da tela
largura = 600
altura = 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('jogo da cobrinha')

# Definindo cores
verde = (0, 255, 0)
vermelho = (255, 0, 0)
preto = (0, 0, 0)

#Configurações do jogo
tamanho_celula = 20
velocidade = 5
relogio = pygame.time.clock()

# função para gerar a comida em posição aleatória
def gerar_comida():
    x_comida = random.randrange(0, largura, tamanho_celula)
    y_camida = random.randrange(0, altura, tamanho_celula)
    return x_comida, y_comida

# função para desenhar a cobrinha
def desenhar_cobrinha(cobra):
    for parte in cobra:
        pygame.draw.rect(tela, verde, (parte[0], parte[1], tamanho_celula, tamanho_celula))

        #função principal
        def jogo():
            x = largura // 2
            y = altura // 2
            x_velocidade = 0
            y_velocidade = 0
            cobra = [(x, y)]
            comprimento_cobra = 1

            x_comida, y_comida = gerar_comida()

            while true:
                #Detecta eventos
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                        # captura as teclas para mover a cobrinha
                        if evento.type == pygame.KEYDOWN:
                            if eventos.key == pygame.K_LEFT and x_velocidade == 0:
                                x_velocidade = -tamanho_celula
                                y_velocidade = 0
                            elif evento.key == pygame.K_RIGHT and x_velocidade == 0:
                                x_velocidade = tamanho_celula
                                y_velocidade = 0
                            elif evento.key == pygame.K_UP and y_velocidade == 0:
                                y_velocidade = -tamanho_celula
                                x_velocidade = 0
                            elif evento.key == pygame.K_DOWN and y_velocidade == 0:
                                y_velocidade = tamanho_celula


                                # Atualiza a posição da cobrinha
                                x += x_velocidade
                                x += y_velocidade 
                                cobra.append((x, y))
                                
                                # Mantém o tamanho da cobrinha
                                if len(cobra) > comprimento_cobra:
                                    del cobra[0]

                                    # Detecta colisão com as bordas ou com o próprio corpo
                                    if x < 0 or x >= largura or y < 0 or y >= altura or (x,y) in cobra[:-1]:
                                        break

                                    #detecta se a cobrinha comeu a comida
                                    if x == x_comida and y == y_comida:
                                        comprimento_cobra += 1
                                        x_comida, y_comida = gerar_comida()

                                    # Atualiza a tela
                                    tela.fill(preto)
                                    desenhar_cobrinha(cobra)
                                    pygame.draw.rect(tela, vermelho, (x_comida, y_comida, tamanho_celula, tamanho_celula))
                                    pygame.display.flip()

relogio.tick(velocidade)

#iniciar o jogo
jogo()
