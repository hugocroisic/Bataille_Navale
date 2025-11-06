from bateau import Bateau, chevauchent

def test_bateau_defaut():
    b = Bateau(2, 3)
    assert b.ligne == 2
    assert b.colonne == 3
    assert b.longueur == 1
    assert b.vertical is False

def test_positions_horizontales():
    b = Bateau(2, 3, longueur=3)
    assert b.positions == [(2, 3), (2, 4), (2, 5)]

def test_positions_verticales():
    b = Bateau(2, 3, longueur=3, vertical=True)
    assert b.positions == [(2, 3), (3, 3), (4, 3)]

def test_chevauchent_vrai():
    b1 = Bateau(2, 3, longueur=3)
    b2 = Bateau(2, 4, longueur=2)
    assert chevauchent(b1, b2) is True

def test_chevauchent_faux():
    b1 = Bateau(0, 0, longueur=2)
    b2 = Bateau(3, 3, longueur=2)
    assert chevauchent(b1, b2) is False
