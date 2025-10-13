from grille import Grille
import numpy as np

def test_constructeur():
    assert(Grille(5,8).constructeur().shape == (5,8))

def test_afficher():
    assert np.array_equal(Grille(5,8).afficher(), np.full((5,8),'.')) # Ici, je n'utilise pas "==" car avec numpy a == b renvoie un tableau de bouléen et non un booléen, or assert attend un booléen, j'aurais pu faire np.all(a==b) mais je ne trouvais pas cela très clair

def test_tirer():
    grille =  Grille(5,8)
    grille.tirer(1,2)
    assert(grille.matrice[1,2] == 'x')

def test_tirer_hors_grille():
    g = Grille(5, 8)
    try:
        g.tirer(10, 10)
        assert False, "IndexError attendu mais non levé"
    except IndexError:
        pass  