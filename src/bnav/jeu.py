def trouver_bateau_a(flotte, l, c):
    for b in flotte:
        if (l, c) in b.positions:
            return b
    return None

def tirer_avec_retour(grille, flotte, l, c):
    idx = grille._index(l, c)
    ch = grille.grille[idx]

    if ch == grille.frappe:
        return "déjà tiré", None

    b = trouver_bateau_a(flotte, l, c)
    if b is None:
        grille.grille[idx] = grille.frappe
        return "raté", None

    grille.grille[idx] = grille.frappe
    if b.coule(grille):
        return "coulé", b
    else:
        return "touché", b