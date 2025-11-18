from src.bnav.bateau import Bateau
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

    def __str__(self):
        lignes = []
        for i in range(self.n_ligne):
            row = self.grille[i*self.n_colonne:(i+1)*self.n_colonne]
            lignes.append(''.join(row))
        return '\n'.join(lignes)
    
    def ajoute(self, bateau):

        positions = bateau.positions

        # Vérifier que toutes les positions sont dans la grille
        for (l, c) in positions:
            if not (0 <= l < self.n_ligne and 0 <= c < self.n_colonne):
                return False  # on ne modifie rien

        # Vérifier qu'on n'écrase pas déjà quelque chose (facultatif mais sain)
        for (l, c) in positions:
            if self.grille[self._index(l, c)] != self.vide:
                return False

        # Tout est ok -> on place le bateau
        for (l, c) in positions:
            self.grille[self._index(l, c)] = bateau.marque
        return True
    
    def afficher_publique(self, flotte) -> str:
        lignes = []
        for l in range(self.n_ligne):
            row = []
            for c in range(self.n_colonne):
                idx = self._index(l, c)
                ch = self.grille[idx]

                # y a-t-il un bateau sur cette case ?
                b = None
                for _b in flotte:
                    if (l, c) in _b.positions:
                        b = _b
                        break

                if b is None:
                    # eau
                    row.append('x' if ch == self.frappe else self.vide)
                else:
                    # bateau
                    if b.coule(self):
                        row.append(b.marque)        # révélé (overlay)
                    else:
                        row.append('💣' if ch == self.frappe else self.vide)
            lignes.append(''.join(row))
        return '\n'.join(lignes)