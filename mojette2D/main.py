# Exemple : on projette une image 3x3 puis on la reconstruit

from projection import transformee_mojette
from katz import katz_ok
from reconstruction import reconstruire


image = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
directions = [(0, 1), (1, 1), (-1, 1)]

print("Image de départ :")
for ligne in image:
    print(ligne)

projections = transformee_mojette(image, directions)
print("\nProjections :")
for d, proj in projections.items():
    print(d, {b: proj[b] for b in sorted(proj)})

print("\nKatz OK :", katz_ok(directions, 3, 3))

print("\nReconstruction :")
resultat = reconstruire(projections, 3, 3)

print("\nImage retrouvée :")
for ligne in resultat:
    print(ligne)
print("\nMême image :", resultat == image)


# exemple d'utilisation de code : 
# Image de départ :
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]

# Projections :
# (0, 1) {-2: 18, -1: 15, 0: 12}
# (1, 1) {-2: 3, -1: 8, 0: 15, 1: 12, 2: 7}
# (-1, 1) {-4: 9, -3: 14, -2: 15, -1: 6, 0: 1}

# Katz OK : True

# Reconstruction :
# Étape 1 : bin -2 de la direction (1, 1), pixel (2, 0) = 3
# Étape 2 : bin 2 de la direction (1, 1), pixel (0, 2) = 7
# Étape 3 : bin 0 de la direction (-1, 1), pixel (0, 0) = 1
# Étape 4 : bin 0 de la direction (0, 1), pixel (0, 1) = 4
# Étape 5 : bin 1 de la direction (1, 1), pixel (1, 2) = 8
# Étape 6 : bin -1 de la direction (-1, 1), pixel (1, 0) = 2
# Étape 7 : bin -1 de la direction (0, 1), pixel (1, 1) = 5
# Étape 8 : bin 0 de la direction (1, 1), pixel (2, 2) = 9
# Étape 9 : bin -2 de la direction (0, 1), pixel (2, 1) = 6

# Image retrouvée :
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]

# Même image : True