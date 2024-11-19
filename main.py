# usar pygame p tocar sons
# setar o timbre para o piano
# nota = (nome da nota, duração)
# formula da frequencia: f0 * (2 ^ 1/12) ^ n, onde f0 é a frequencia do lá -> 440Hz e n é a distancia de semitons até o lá, que aceita valores negativos
# fazer a onda do som
# interface de um piano tocando as notas -> tecla pode estar abaixada ou levantada, ser preta ou branca
# interface deve ter as notas caindo, como se fosse um synthesia
# processamento: a pessoa ou deve inserir uma sequencia de notas que o piano tocará automaticamente ou tocar o piano
# fim: quando a pessoa fechar a janela da interface

import pygame as pg
from poligono import Poligono

# interface pygame

pg.init()

screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()
running = True



# Define a posição inicial do sprite
eixo_x = 173
eixo_y = 200


font = pg.font.Font(None, 100)
texto_beta = font.render("Isso é um BETA", True, (255, 0, 0))
font = pg.font.Font(None, 50)
texto_versao = font.render("Piano-Python 0.2", True, (255, 0, 0))
cor_borda = (146, 148, 150)

teclas_brancas = []
padrao_codigos_branco = [1, 3, 4, 1, 3, 3, 4]
for i in range(17):
    teclas_brancas.append(Poligono(padrao_codigos_branco[i % len(padrao_codigos_branco)], eixo_x, eixo_y))
    print(type(teclas_brancas[i]))
    eixo_x += 55

teclas_pretas = []
padrao_inc_preto = [56, 108.5, 56, 56, 108.5]
print(eixo_x)
eixo_x = 173 + 42
eixo_y = 200

for i in range(12):
    teclas_pretas.append(Poligono(2, eixo_x, eixo_y))
    eixo_x += padrao_inc_preto[i%len(padrao_inc_preto)]


while running:
    mouse = pg.mouse.get_pos()
    # pg.QUIT() é quando o usuário fecha a janela
    for event in pg.event.get():
        # print(event)
        if event.type == pg.QUIT:
            running = False 


    screen.fill((176, 176, 106))

    for i in range(len(teclas_brancas)):
        area1, area2 = teclas_brancas[i].area_botoes()
        
        if (area1[0][0] < mouse[0] < area1[0][1] and area1[1][0] < mouse[1] < area1[1][1]) or (area2[0][0] < mouse[0] < area2[0][1] and area2[1][0] < mouse[1] < area2[1][1]):
            pg.draw.polygon(screen, (225, 225, 225), teclas_brancas[i].get_pontos())
        else:
            pg.draw.polygon(screen, (255, 255, 255), teclas_brancas[i].get_pontos())

        pg.draw.polygon(screen, cor_borda, teclas_brancas[i].get_pontos(), width = 1)

    for i in range(len(teclas_pretas)):
        area1, area2 = teclas_pretas[i].area_botoes()
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



