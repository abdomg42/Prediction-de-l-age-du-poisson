# Critère de Katz : dit si les directions suffisent pour reconstruire l'image
 
 
def katz_ok(directions, nb_colonnes, nb_lignes):
    somme_p = sum(abs(p) for p, q in directions)
    somme_q = sum(abs(q) for p, q in directions)
    return somme_p >= nb_colonnes or somme_q >= nb_lignes
 