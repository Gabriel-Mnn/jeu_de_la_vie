import pyxel as px
from game_of_life import Jeudelavie

class App:
    def __init__(self):
        self.jeu = Jeudelavie(150,150)

    def run(self):
        """
        lance le jeu de la vie
        """
        px.init(self.jeu.largeur, self.jeu.hauteur)
        px.run(self.update, self.draw)

    def update(self):
        """
        met a jour le jeu de la vie 
        """
        if px.frame_count % 1 == 0:
            self.jeu.tour()


    def draw(self):
        """
        dessine le jeu de la vie les pixels vivants et morts et le compteur de tour
        """
        px.cls(7)
        for h in range (self.jeu.hauteur):
            for l in range (self.jeu.largeur):
                if self.jeu.tab[h+1][l+1] == 1:
                    px.rect(l, h, 1, 1, 0)
        chaine = f"count:{self.jeu.compteur}"
        px.rect(0,0,len(chaine)*4,6,0)
        px.text(0,0,f"count:{self.jeu.compteur}",8)
a = App()
a.jeu.hasard(0.10)
a.run()