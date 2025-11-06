class Grille:
    def __init__(self, n_ligne=10, n_colonne=10, vide='∿', frappe='x'):
        self.n_ligne = n_ligne
        self.n_colonne = n_colonne
        self.vide = vide
        self.frappe = frappe
        self.grille = [self.vide] * (self.n_ligne * self.n_colonne)

    
    def _index(self, ligne, colonne):
        return ligne * self.n_colonne + colonne
    
    def tirer(self, ligne, colonne, touche=None):
        if touche is None:
            touche = self.frappe
        idx = self._index(ligne, colonne)
        self.grille[idx] = touche




