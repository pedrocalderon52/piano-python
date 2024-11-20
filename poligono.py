import pygame as pg
class Poligono():
    def __init__(self, cod_poligono, x, y) -> None:
        self.cod_poligono = cod_poligono
        self.x = x
        self.y = y


    def get_pontos(self) -> list[tuple]:
        """ retorna uma lista de pontos (relativos) que o polígono possui, com base no código identificador dele"""
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
    

    def area_botoes(self) -> tuple[tuple]:
        """divide cada polígono em 2 retângulos e retorna os delimitadores de área, para realizar a implementação de um botão """
        areas = {
            1: (((self.x, self.x + 55), (self.y + 115, self.y + 200)), ((self.x, self.x + 42), (self.y, self.y + 115))), 
            2: (((self.x, self.x + 26), (self.y, self.y + 114)), ((self.x, self.x + 26), (self.y, self.y + 114))), 
            3: (((self.x, self.x + 55), (self.y + 115, self.y + 200)), ((self.x + 13, self.x + 39), (self.y, self.y + 115))),
            4: (((self.x, self.x + 55), (self.y + 115, self.y + 200)), ((self.x + 13, self.x + 55), (self.y, self.y + 115))), 
            5: (((self.x, self.x + 55), (self.y, self.y + 200)), ((self.x, self.x + 55), (self.y, self.y + 200)))
        }
        return areas[self.cod_poligono]
    

    def print_info(self):
        """printa na tela as informações do polígono, para facilitar o debugging
        cod_polígono = 
        x =
        y =
        """
        print(f"{self.cod_poligono =} \n {self.x = } \n {self.y =}")
        

        
        
        
