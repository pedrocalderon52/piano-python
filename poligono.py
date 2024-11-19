import pygame as pg
class Poligono():
    def __init__(self, cod_poligono, x, y) -> None:
        self.cod_poligono = cod_poligono
        self.x = x
        self.y = y

    def get_pontos(self) -> list:
        pontos = {
            1: [(self.x, self.y), 
                (self.x, self.y + 200), 
                (self.x + 42 + 13, self.y + 200), 
                (self.x + 42 + 13, self.y + 115), 
                (self.x + 42, self.y + 115), 
                (self.x + 42, self.y)], #(42, 200)

            2: [(self.x, self.y), 
                (self.x + 26, self.y), 
                (self.x + 26, self.y + 114), 
                (self.x, self.y + 114)], #(26, 115), 

            3: [(self.x + 13, self.y), 
                (self.x + 13 + 29, self.y), 
                (self.x + 13 + 29, self.y + 115), 
                (self.x + 13 + 29 + 13, self.y + 115), 
                (self.x + 13 + 29 + 13, self.y + 200), 
                (self.x, self.y + 200), 
                (self.x, self.y + 115), 
                (self.x + 13, self.y + 115)], #(13,  85)

            4: [(self.x + 13, self.y), 
                (self.x + 13 + 42, self.y), 
                (self.x + 13 + 42, self.y + 200), 
                (self.x, self.y + 200), 
                (self.x, self.y + 115), 
                (self.x + 13, self.y + 115)], #(26, 200)

            5: [(self.x, self.y), 
                (self.x + 55, self.y), 
                (self.x + 55, self.y + 200), 
                (self.x, self.y + 200)] #(52, 200)
        }
        return pontos[self.cod_poligono]
    

    def inc_eixo_x(self) -> int:
        incremento = { # o quanto o eixo x é incrementado após cada tecla ser criada
            1: 42, 
            2: 13,
            3: 39, 
            4: 55,
            5: 55, 
        }
        return incremento[self.cod_poligono]


    def area_botoes(self):
        areas = {
            1: (((self.x, self.x + 55), (self.y + 115, self.y + 200)), ((self.x, self.x + 42), (self.y, self.y + 115))), 
            2: (((self.x, self.x + 26), (self.y, self.y + 114)), ((self.x, self.x + 26), (self.y, self.y + 114))), 
            3: (((self.x, self.x + 55), (self.y + 115, self.y + 200)), ((self.x + 13, self.x + 39), (self.y, self.y + 115))),
            4: (((self.x, self.x + 55), (self.y + 115, self.y + 200)), ((self.x + 13, self.x + 55), (self.y, self.y + 115))), 
            5: (((self.x, self.x + 55), (self.y, self.y + 200)), ((self.x, self.x + 55), (self.y, self.y + 200)))
        }
        return areas[self.cod_poligono]
    

    def print_info(self):
        print(f"{self.cod_poligono =} \n {self.x = } \n {self.y =}")
        

        
        
        
