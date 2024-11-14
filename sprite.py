import pygame as pg
class Sprite():
    def __init__(self, cod_sprite, x, y) -> None:
        self.cod_sprite = cod_sprite
        self.x = x
        self.y = y

        dimensoes = {
            1: (42, 200),
            2: (26, 115), 
            3: (13,  85),
            4: (26, 200),
            5: (52, 200)
        }

        self.largura = dimensoes[self.cod_sprite][0]
        self.altura = dimensoes[self.cod_sprite][1]

        match(cod_sprite):
            case 1:
                self.image = pg.image.load("sprite5.png") # gambiarra enquanto não tem o sprite1
            case 2:
                self.image = pg.image.load("sprite2.png")
            case 3:
                self.image = pg.image.load("sprite5.png") # idem
            case 4:
                self.image = pg.image.load("sprite5.png") # idem
            case 5:
                self.image = pg.image.load("sprite5.png")
            
        self.image = pg.transform.scale(self.image, (self.largura, self.altura))
        
        
