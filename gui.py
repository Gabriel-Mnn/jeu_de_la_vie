import pyxel as px
import pygame, sys
from game_of_life import Jeudelavie
pygame.init()

clock = pygame.time.Clock()

class Pyxel_app:
    def __init__(self):
        self.game = Jeudelavie(150,150)

    def run(self):
        """
        lance le jeu de la vie
        """
        px.init(self.game.largeur, self.game.hauteur)
        px.run(self.update, self.draw)

    def update(self):
        """
        met a jour le jeu de la vie 
        """
        if px.frame_count % 1 == 0:
            self.game.tour()


    def draw(self):
        """
        dessine le jeu de la vie les pixels vivants, morts et le compteur de tour
        """
        px.cls(7)
        for h in range (self.game.hauteur):
            for l in range (self.game.largeur):
                if self.game.tab[h+1][l+1] == 1:
                    px.rect(l, h, 1, 1, 0)
        chaine = f"count:{self.game.compteur}"
        largeur_compteur = len(chaine)*4
        if largeur_compteur * 5 < self.game.largeur:
            px.rect(0,0,largeur_compteur,6,0)
            px.text(0,0,f"count:{self.game.compteur}",8)
        

class Pygame_app:
    def __init__(self):
        self.game = Jeudelavie(50,50)
        self.screen = pygame.display.set_mode([self.game.largeur*6,self.game.hauteur*6])
        
    def run(self):
        """
        lance le jeu de la vie
        """
        compteur = 0
        while True:
            self.draw()
            self.update()
            compteur += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print(compteur)
                    pygame.display.quit()
                    sys.exit()
                    
        

    def update(self):
        """
        met a jour le jeu de la vie 
        """
        pygame.display.flip()
        clock.tick(60)
        self.game.tour()


    def draw(self):
        """
        dessine le jeu de la vie les pixels vivants et morts et le compteur de tour
        """
        self.screen.fill([255,255,255])
        for h in range (self.game.hauteur):
            for l in range (self.game.largeur):
                if self.game.tab[h+1][l+1] == 1:
                    pygame.draw.rect(self.screen,[0,0,0],(l*6,h*6,6,6)) 
        
    
a = Pyxel_app()
a.game.hasard(0.1)
a.run()