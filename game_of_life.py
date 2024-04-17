import numpy as np
import random

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
        self.tab = np.zeros((hauteur+3, largeur+3))
        self.compteur = 0
        
    def calcul_cellule(self,h,l):
        """
        retourne 1 ou 0 pour une cellule du tableau en hauteur h et largeur l
        en fonction des règles du jeu de la vie.
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
            for l in range (self.largeur):# on boucle sur chaque "cellule" et mémorise dans new_tab ce qu'elle doit devenir
                new_ligne.append(self.calcul_cellule(h+1,l+1))
            new_tab.append(new_ligne)
        for h in range (self.hauteur):
            for l in range (self.largeur):# on boucle sur chaque "cellule" et utilise new_tab pour mettre dans la vrai matrice les bonnes valeurs
                self.tab[h+1][l+1] = new_tab[h][l]
        self.compteur += 1
                    
                    
    def tour2(self):
        """
        Met à jour toutes les cellules du tableau en respectant les règles
        du jeu de la vie.
        """
        new_tab = []
        for h in range (self.hauteur+2):
            new_ligne = []
            for l in range (self.largeur+2):# on boucle sur chaque "cellule" et mémorise dans new_tab ce qu'elle doit devenir
                new_ligne.append(self.calcul_cellule(h+1,l+1))
            new_tab.append(new_ligne)
        for h in range (self.hauteur+2):
            for l in range (self.largeur+2):# on boucle sur chaque "cellule" et utilise new_tab pour mettre dans la vrai matrice les bonnes valeurs
                if h == 0 or h == self.hauteur+1 or l == 0 or l == self.largeur+1:
                    if new_tab[h][l] == 1:
                        if h == self.hauteur+1:
                            self.tab[self.hauteur-h+3][self.largeur-l+2] = 1
                        elif l == self.largeur+1:
                            self.tab[self.hauteur-h+2][self.largeur-l+3] = 1
                        elif h == 0:
                            self.tab[self.hauteur+1][self.largeur-l+2] = 1
                        elif l == 0:
                            self.tab[self.hauteur-h+2][self.largeur-l+2] = 1
                else:
                    self.tab[h+1][l+1] = new_tab[h][l]
        self.compteur += 1
                    
        
        
    def get_voisins(self, hauteur, largeur):
        """
        renvoie le nombre de voisins d'une cellule
        """
        sous_matrice = self.tab[hauteur-1:hauteur+2,largeur-1:largeur+2]
        if self.tab[hauteur][largeur] == 1:
            return np.sum(sous_matrice)-1
        else:
            return np.sum(sous_matrice)

    def hasard(self,taux = 0.5):
        """
        met des cellules vivantes au hasards en fonction du taux (0.75 = 75                                                                                                                                                                                                                                                                                                      % des cellules vivantes)
        """   
        for h in range (self.hauteur):
            for l in range (self.largeur):
                if random.randint(0,100) < taux*100:
                    self.tab[h+1][l+1] = 1

        return self


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
        
g.tab[2][2] = 1
expected = np.array([[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])
g.tour()
result = g.tab
#assert np.array_equal(result,expected) == True, f"le resultat devrait être \n {expected}\n mais vaut \n{result}\n"

g.tab[3][2] = 1
g.tab[2][2] = 1
expected = np.array([[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])
g.tour()
result = g.tab
#assert np.array_equal(result,expected) == True, f"le resultat devrait être \n {expected}\n mais vaut \n{result}\n"
 
g.tab[3][3] = 1
g.tab[2][3] = 1
#g.tab[4][3] = 1
expected = np.array([[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,1,1,1,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])
g.tour()
result = g.tab
#assert np.array_equal(result,expected) == True, f"le resultat devrait être \n {expected}\n mais vaut \n{result}\n"

#g = Jeudelavie(3,3)        

#g.tab[2][4] = 1
#g.tab[2][2] = 1
#g.tab[2][3] = 1
#expected = np.array([[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0]])
#g.tour()
#result = g.tab
#assert np.array_equal(result,expected) == True, f"le resultat devrait être \n {expected}\n mais vaut \n{result}\n"

#g = Jeudelavie(3,3)  

#g.tab[6][4] = 1
#g.tab[6][2] = 1
#g.tab[6][3] = 1
#print(g.tab)
#expected = np.array([[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,,0,0,0,0],[0,0,0,0,0,0,0,0]])
#g.tour()
#result = g.tab
#assert np.array_equal(result,expected) == True, f"le resultat devrait être \n {expected}\n mais vaut \n{result}\n"





g = Jeudelavie(3,3)

g.tab[2][2] = 1
g.tab[2][3] = 1
g.tab[2][4] = 1










