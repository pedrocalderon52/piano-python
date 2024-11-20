# Código que implementa um piano interativo com pygame, numpy e sounddevice
import pygame as pg
from poligono import Poligono


# interface pygame

pg.init() # iniciando pygame

screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock() # define a taxa de FPS
running: bool = True



# Define a posição inicial do piano
eixo_x: float = 173
eixo_y: int = 200


font = pg.font.Font(None, 48)
texto_beta = font.render("BETA", True, (255, 0, 0))
font = pg.font.Font(None, 24)
texto_versao = font.render("Piano-Python 0.2", True, (255, 0, 0))

cor_borda: tuple = (146, 148, 150)

teclas_brancas: list[Poligono] = []
padrao_codigos_branco: list[int] = [1, 3, 4, 1, 3, 3, 4] # padrão de códigos do polígono
for i in range(17):
    teclas_brancas.append(Poligono(padrao_codigos_branco[i % len(padrao_codigos_branco)], eixo_x, eixo_y))
    eixo_x += 55

teclas_pretas: list[Poligono] = []
padrao_inc_preto: list[int] = [56, 108.5, 56, 56, 108.5]

eixo_x = 173 + 42 # redefine o eixo x, com um pequeno incremento para realizar o ajuste das teclas pretas


for i in range(12):
    teclas_pretas.append(Poligono(2, eixo_x, eixo_y))
    eixo_x += padrao_inc_preto[i % len(padrao_inc_preto)]


while running:
    mouse = pg.mouse.get_pos()
    # pg.QUIT() é quando o usuário fecha a janela
    for event in pg.event.get():
        # print(event)
        if event.type == pg.QUIT:
            running = False 
        
        #if event.type == pg.MOUSEBUTTONDOWN:
            #ataque 
            #decaimento
            #loop de sustentação e relaxamento


    screen.fill((176, 176, 106))

    for i in range(len(teclas_brancas)):
        area1, area2 = teclas_brancas[i].area_botoes()
        
        if (area1[0][0] < mouse[0] < area1[0][1] and area1[1][0] < mouse[1] < area1[1][1]) or (area2[0][0] < mouse[0] < area2[0][1] and area2[1][0] < mouse[1] < area2[1][1]):
            pg.draw.polygon(screen, (225, 225, 225), teclas_brancas[i].get_pontos())
        else:
            pg.draw.polygon(screen, (255, 255, 255), teclas_brancas[i].get_pontos())

        pg.draw.polygon(screen, cor_borda, teclas_brancas[i].get_pontos(), width = 1)

    for i in range(len(teclas_pretas)):
        area1, area2 = teclas_pretas[i].area_botoes() #escrever função para isso depois 
        if (area1[0][0] < mouse[0] < area1[0][1] and area1[1][0] < mouse[1] < area1[1][1]) or (area2[0][0] < mouse[0] < area2[0][1] and area2[1][0] < mouse[1] < area2[1][1]):
            pg.draw.polygon(screen, (100, 100, 110), teclas_pretas[i].get_pontos())
        else:
            pg.draw.polygon(screen, (0, 0, 0), teclas_pretas[i].get_pontos())

    

    # textos

    screen.blit(texto_beta, (540, 600))
    screen.blit(texto_versao, (30, 700))
    pg.display.flip()

    clock.tick(60)
pg.quit()



