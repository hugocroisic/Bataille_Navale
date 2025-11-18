class Bateau:
    def __init__(self, ligne, colonne, longueur=1, vertical=False, marque='⛵'):
        self.ligne = ligne          
        self.colonne = colonne     
        self.longueur = longueur    
        self.vertical = vertical    
        self.marque = marque

    @property
    def positions(self):
        if self.vertical:
            return [
                (self.ligne + i, self.colonne)
                for i in range(self.longueur)
            ]
        else:
            return [
                (self.ligne, self.colonne + i)
                for i in range(self.longueur)
            ]
        
    def coule(self, grille):
        for (l, c) in self.positions:
            ch = grille.grille[grille._index(l, c)]
            if ch != grille.frappe:  
                return False
        return True
    

class PorteAvion(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=4, vertical=vertical, marque='🚢')


class Croiseur(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=3, vertical=vertical, marque='⛴')


class Torpilleur(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical, marque='🚣')


class SousMarin(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical, marque='🐟')


def chevauchent(b1, b2):
    return bool(set(b1.positions) & set(b2.positions))

