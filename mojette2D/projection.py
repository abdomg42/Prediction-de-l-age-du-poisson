# Transformée de Mojette directe : de l'image vers les projections
 
 
def numero_de_bin(p, q, k, l):
    # k = colonne, l = ligne
    # les pixels qui ont le même b sont sur la même droite
    return p * l - q * k
 
 
def projeter(image, p, q):
    projection = {}
    for l in range(len(image)):
        for k in range(len(image[0])):
            b = numero_de_bin(p, q, k, l)
            projection[b] = projection.get(b, 0) + image[l][k]
    return projection
 
 
def transformee_mojette(image, directions):
    return {(p, q): projeter(image, p, q) for (p, q) in directions}