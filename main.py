# usar pygame p tocar sons
# setar o timbre para o piano
# nota = (nome da nota, duração)
# formula da frequencia: f0 * (2 ^ 1/12) ^ n, onde f0 é a frequencia do lá -> 440Hz e n é a distancia de semitons até o lá, que aceita valores negativos
# fazer a onda do som
# interface de um piano tocando as notas -> tecla pode estar abaixada ou levantada, ser preta ou branca
# interface deve ter as notas caindo, como se fosse um synthesia
# processamento: a pessoa ou deve inserir uma sequencia de notas que o piano tocará automaticamente ou tocar o piano
# fim: quando a pessoa fechar a janela da interface

import numpy as np
import sounddevice as sd
import pygame as pg
from poligono import Poligono

def gerar_onda_seno(frequencia: float, duracao: float, amplitude: float = 0.5, taxa_de_amostragem = 44100):
    vet = np.linspace(0, duracao, int(taxa_de_amostragem * duracao), endpoint = False)
    onda = amplitude * np.sin(2 * np.pi * frequencia * vet)
    return onda

def gerar_onda_serra(frequencia: float, duracao: float, amplitude: float = 0.5, taxa_de_amostragem = 44100, num_harmonicos = 40):
    vet = np.linspace(0, duracao, int(taxa_de_amostragem * duracao), endpoint = False)
    vet_serra = np.zeros_like(vet)
    for k in range(1, num_harmonicos + 1): 
        termo = (-1 ** k) * (np.sin(2 * np.pi * k * frequencia * vet) / k)
        vet_serra += termo
    return vet_serra * (2/np.pi)


def calcular_frequencia(nota: str) -> float:
    return 440 * ((2 ** (1/12)) ** (notas.index(nota) - notas.index("A4")))

notas: list = ["A0", "A#0", "B0", "C1", "C#1", "D1", "D#1", "E1", "F1", "F#1", "G1", "G#1", 
               "A1", "A#1", "B1", "C2", "C#2", "D2", "D#2", "E2", "F2", "F#2", "G2", "G#2", 
               "A2", "A#2", "B2", "C3", "C#3", "D3", "D#3", "E3", "F3", "F#3", "G3", "G#3", 
               "A3", "A#3", "B3", "C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4", "G#4", 
               "A4", "A#4", "B4", "C5", "C#5", "D5", "D#5", "E5", "F5", "F#5", "G5", "G#5", 
               "A5", "A#5", "B5", "C6", "C#6", "D6", "D#6", "E6", "F6", "F#6", "G6", "G#6", 
               "A6", "A#6", "B6", "C7", "C#7", "D7", "D#7", "E7", "F7", "F#7", "G7", "G#7", 
               "A7", "A#7", "B7", "C8"]

# nota = input("Digite a nota que deseja calcular a frequencia")
# print(calcular_frequencia_nota(nota))
# por enquanto essas linhas acima estão comentadas para realizarmos testes sobre como 
# modular a onda para fazer o timbre parecer com o de um piano

# aplicar transf. de fourier

nota: str = "A4" # final: input("Digite a nota que deseja calcular a frequência: ")
freq_nota = calcular_frequencia(nota)
amp_fundamental = 0.2
onda1 = gerar_onda_seno(freq_nota, 2.0, amplitude=amp_fundamental)
onda_serra = gerar_onda_serra(440.0, 2.0)


# testes
""" fator_decaimento = 1.8 if freq_nota > 100 else 1.5 #provavelmente estará em desuso quando aprendermor a aplicar a transformada inversa de fourier

sd.play(onda1, samplerate=44100)
sd.wait()
onda2 = gerar_onda_seno(freq_nota * (2 ** 1), 2.0, amplitude = amp_fundamental * 0.25)
onda3 = gerar_onda_seno(freq_nota * (2 ** 2), 2.0, amplitude = amp_fundamental * 0.45)
onda4 = gerar_onda_seno(freq_nota * (2 ** 3), 2.0, amplitude = amp_fundamental * 0.37)
onda5 = gerar_onda_seno(freq_nota * (2 ** 4), 2.0, amplitude = amp_fundamental * 0.29)
onda6 = gerar_onda_seno(freq_nota * (2 ** 5), 2.0, amplitude = amp_fundamental * 0.08)
onda7 = gerar_onda_seno(freq_nota * (2 ** 6), 2.0, amplitude = amp_fundamental * 0.15)


onda1 = onda1 + onda2 + onda3 + onda4 + onda5 + onda6 + onda7
onda1 /= 7"""


#sd.play(onda_serra, samplerate=44100)
#sd.wait()

#sd.play(onda_serra + onda1, samplerate=44100)

# interface pygame

pg.init()

screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()
running = True



# Define a posição inicial do sprite
eixo_x = 330
eixo_y = 200


font = pg.font.Font(None, 48)
texto_beta = font.render("Isso é uma BETA", True, (255, 0, 0))
font = pg.font.Font(None, 24)
texto_versao = font.render("Piano-Python 0.2", True, (255, 0, 0))
cor_borda = (146, 148, 150)


poli1 = Poligono(1, eixo_x, eixo_y)
eixo_x += poli1.inc_eixo_x()
poli2 = Poligono(2, eixo_x, eixo_y)
eixo_x += poli2.inc_eixo_x()
poli3 = Poligono(3, eixo_x, eixo_y)
eixo_x += poli3.inc_eixo_x()
poli4 = Poligono(2, eixo_x, eixo_y)
eixo_x += poli4.inc_eixo_x()
poli5 = Poligono(4, eixo_x, eixo_y)
eixo_x += poli5.inc_eixo_x()
poli6 = Poligono(1, eixo_x, eixo_y)
eixo_x += poli6.inc_eixo_x()

while running:
    # pg.QUIT() é quando o usuário fecha a janela
    for event in pg.event.get():
        # print(event)
        if event.type == pg.QUIT:
            running = False 


    screen.fill((166, 156, 149))

    pg.draw.polygon(screen, (255, 255, 255), poli1.get_pontos())
    pg.draw.polygon(screen, cor_borda, poli1.get_pontos(), width = 1)

    

    pg.draw.polygon(screen, (255, 255, 255), poli3.get_pontos())
    pg.draw.polygon(screen, cor_borda, poli3.get_pontos(), width = 1)


    pg.draw.polygon(screen, (255, 255, 255), poli5.get_pontos())
    pg.draw.polygon(screen, cor_borda, poli5.get_pontos(), width = 1)

    pg.draw.polygon(screen, (255, 255, 255), poli6.get_pontos())
    pg.draw.polygon(screen, cor_borda, poli6.get_pontos(), width = 1)

    pg.draw.polygon(screen, (0, 0, 0), poli4.get_pontos())

    pg.draw.polygon(screen, (0, 0, 0), poli2.get_pontos())

    # textos

    screen.blit(texto_beta, (540, 600))
    screen.blit(texto_versao, (30, 700))
    pg.display.flip()

    clock.tick(60)
pg.quit()



