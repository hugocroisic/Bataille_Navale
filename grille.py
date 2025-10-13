import numpy as np

class Grille:
    def __init__(self, n_ligne=10, n_colonne=10):
        self.n_ligne = n_ligne
        self.n_colonne = n_colonne
        self.matrice = self.constructeur()

    def constructeur(self):        
        return np.full((self.n_ligne,self.n_colonne),'.')
    
    def afficher(self):
        return self.matrice
    
    def tirer (self,x,y):      
        if not (0 <= x < self.n_ligne and 0 <= y < self.n_colonne):
            raise IndexError("Coordonnées hors grille")  
        self.matrice[x,y] = "x"



