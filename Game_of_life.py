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
        self.tab = np.zeros((hauteur+1, largeur+1))
    
#     def calcul_cellule(self,h,l):
#         """
#         Met à jour une cellule du tableau en hauteur h et largeur l
#         tout en respectant les règles du jeu de la vie.
#         """
#         voisins = self.get_voisins(h,l)
#         if self.tab[h][l] == 1 and voisins in [2,3]:
#             self.tab[h][l] = 1
#         elif self.tab[h][l] == 0 and voisins == 3:
#             self.tab[h][l] = 1
#         else:
#             self.tab[h][l] = 0
            
    def calcul_cellule(self,h,l):
        """
        Met à jour une cellule du tableau en hauteur h et largeur l
        tout en respectant les règles du jeu de la vie.
        """
        voisins = self.get_voisins(h,l)
        if self.tab[h][l] == 1 and voisins in [2,3]:
            return 1
        elif self.tab[h][l] == 0 and voisins == 3:
            return 1
        else:
            return 0
    
    def tour(self):
        """
        Met à jour toutes les cellules du tableau en respectant les règles
        du jeu de la vie.
        """
        new_tab = []
        for h in range (self.hauteur):
            new_ligne = []
            for l in range (self.largeur):
                new_ligne.append(self.calcul_cellule(h+1,l+1))
            new_tab.append(new_ligne)
        for h in range (self.hauteur):
            for l in range (self.largeur):
                self.tab[h+1][l+1] = new_tab[h][l]
                    
        
        
    def get_voisins(self, hauteur, largeur):
        """
        renvoie le nombre de voisins d'une cellule
        """
        sous_matrice = self.tab[hauteur-1:hauteur+2,largeur-1:largeur+2]
        if self.tab[hauteur][largeur] == 1:
            return np.sum(sous_matrice)-1
        else:
            return np.sum(sous_matrice)
    
    


########## test de "get_voisins" #################

g = Jeudelavie(5,5)        
        
expected = 0
result = g.get_voisins(2,3)
assert result == expected, f"le resultat devrait être \n {expected}\n mais vaut \n{result}\n"

g.tab[2][4] = 1
expected = 0
result = g.get_voisins(2,4)
assert result == expected, f"le resultat devrait être \n {expected}\n mais vaut \n{result}\n"

g.tab[3][4] = 1
g.tab[1][3] = 1
expected = 2
result = g.get_voisins(2,4)
assert result == expected, f"le resultat devrait être \n {expected}\n mais vaut \n{result}\n"

########## test de "tour" #################


g = Jeudelavie(3,3)        
       
g.tab[1][1] = 1
expected = np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
g.tour()
result = g.tab
assert np.array_equal(result,expected) == True, f"le resultat devrait être \n {expected}\n mais vaut \n{result}\n"

g.tab[2][1] = 1
g.tab[1][1] = 1
expected = np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
g.tour()
result = g.tab
assert np.array_equal(result,expected) == True, f"le resultat devrait être \n {expected}\n mais vaut \n{result}\n"

g.tab[2][2] = 1
g.tab[1][2] = 1
g.tab[3][2] = 1
expected = np.array([[0,0,0,0],[0,0,0,0],[0,1,1,1],[0,0,0,0]])
g.tour()
result = g.tab
assert np.array_equal(result,expected) == True, f"le resultat devrait être \n {expected}\n mais vaut \n{result}\n"

for _ in range (4):
    print (g.tab)
    g.tour()




















