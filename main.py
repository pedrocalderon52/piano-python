# Código que implementa um piano interativo com pygame, numpy e sounddevice
import pygame as pg
from poligono import Poligono
from onda_sonora import Nota

# tirar daqui depois
notas: list = ["C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4", "G#4", 
                "A4", "A#4", "B4", "C5", "C#5", "D5", "D#5", "E5", "F5", "F#5", "G5", "G#5", 
                "A5", "A#5", "B5", "C6", "C#6", "D6", "D#6", "E6"]


def esta_dentro_botao(mouse: tuple, poli: Poligono):
    area1, area2 = poli.area_botoes()
    if (area1[0][0] < mouse[0] < area1[0][1] and area1[1][0] < mouse[1] < area1[1][1]) or (area2[0][0] < mouse[0] < area2[0][1] and area2[1][0] < mouse[1] < area2[1][1]):
        return True
    else:
        return False


def desenhar_poligono(surface, cor_tecla: tuple, cor_hover: tuple, poli: Poligono, branco = True):

    cor_borda: tuple = (146, 148, 150)
        
    if esta_dentro_botao(mouse, poli):
        pg.draw.polygon(surface, cor_hover, poli.get_pontos())
    else:
        pg.draw.polygon(surface, cor_tecla, poli.get_pontos())
    
    if branco:
        pg.draw.polygon(screen, cor_borda, poli.get_pontos(), width = 1)


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


padrao_cores_tecla = [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0] # 0 significa branco e 1 significa preto

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


lista_negra: list[Poligono] = teclas_pretas.copy()
lista_branca: list[Poligono] = teclas_brancas.copy()
lista_geral: list[Poligono] = []

for i in range(len(lista_negra) + len(lista_branca)):
    if not padrao_cores_tecla[i % len(padrao_cores_tecla)]:
        lista_geral.append(lista_branca[0])
        del lista_branca[0]
    else: 
        lista_geral.append(lista_negra[0])
        del lista_negra[0]

del lista_branca
del lista_negra

######################################################################################
#################                   MAIN                    ##########################
######################################################################################


while running:
    mouse = pg.mouse.get_pos()
    # pg.QUIT() é quando o usuário fecha a janela
    for event in pg.event.get():
        # print(event)
        if event.type == pg.QUIT:
            running = False 

        if event.type == pg.MOUSEBUTTONDOWN:
            i_nota = -1
            for i, tecla in enumerate(lista_geral):
                if esta_dentro_botao(mouse, tecla):
                    i_nota = i
            if i_nota != -1: #depois arrumar um jeito de colocar as notas dentro da classe, se vira mlk
                nota_ataque = Nota(notas[i_nota], 0.25, 0.5, 44100)
                nota_ataque.tocar_nota(nota_ataque.gerar_onda_seno())
        
    screen.fill((176, 176, 106))
    
    for tecla in teclas_brancas:
        desenhar_poligono(screen, (255, 255, 255), (225, 225, 225), tecla)

    for tecla in teclas_pretas:
        desenhar_poligono(screen, (0, 0, 0), (100, 100, 110), tecla, branco = False)

    # textos

    screen.blit(texto_beta, (540, 600))
    screen.blit(texto_versao, (30, 700))
    pg.display.flip()

    clock.tick(60)
pg.quit()



