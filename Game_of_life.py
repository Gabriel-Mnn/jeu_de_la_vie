import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Jeudelavie:
    def __init__(self, hauteur, largeur):
        """
        Affecte un tableau à deux dimensions à l’attribut tableau

        :param tableau: tableau à deux dimensions
        0.0 = cellule morte
        1.0 = cellule vivante
        """
        self.largeur = largeur
        self.hauteur = hauteur
        self.tab = np.zeros((hauteur, largeur))
        
    
    def tour(self):
        """
        Met à jour toutes les cellules du tableau en respectant les règles
        du jeu de la vie.
        """
        for h in range (self.hauteur):
            for l in range (self.largeur):
                voisins = get_voisins(h,l)
                if self.tab[h][l] == 1.0 and voisins == 2 or voisins == 3:
                    self.tab[h][l] = 1.0
                elif self.tab[h][l] == 0.0 and voisins == 3:
                    self.tab[h][l] = 1.0
                else:
                    self.tab[h][l] = 0.0
        
        
        
    def get_voisins(self, hauteur, largeur):
        """
        renvoie le nombre de voisins d'une cellule
        """
        sous_matrice = self.tab[hauteur-1:hauteur+2,largeur-1:largeur+2]
        if self.tab[hauteur][largeur] == 1.0:
            return np.sum(sous_matrice)-1
        else:
            return np.sum(sous_matrice)
    
    


########## test de "get_voisins" #################

g = Jeudelavie(5,5)        
        
expected = 0
result = g.get_voisins(2,3)
assert result == expected, f"le resultat devrait être {expected} mais vaut {result}."

g.tab[2][4] = 1
expected = 0
result = g.get_voisins(2,4)
assert result == expected, f"le resultat devrait être {expected} mais vaut {result}."

g.tab[3][4] = 1
g.tab[1][3] = 1
expected = 2
result = g.get_voisins(2,4)
assert result == expected, f"le resultat devrait être {expected} mais vaut {result}."

########## test de "tour" #################


g = Jeudelavie(2,2)        
        
# expected = 0
# result = g.get_voisins(2,3)
# assert result == expected, f"le resultat devrait être {expected} mais vaut {result}."
# 
# g.tab[2][4] = 1
# expected = 0
# result = g.get_voisins(2,4)
# assert result == expected, f"le resultat devrait être {expected} mais vaut {result}."
# 
# g.tab[3][4] = 1
# g.tab[1][3] = 1
# expected = 2
# result = g.get_voisins(2,4)
# assert result == expected, f"le resultat devrait être {expected} mais vaut {result}."
# 


