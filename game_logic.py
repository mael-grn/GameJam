import pickle

#x et y correspondent au coordonées du personnage, ou n'importe quel autre objet sur la carte.
#id represente l'identifiant de l'objet avec lequel on veut detecter la collision, dans le fichier tmx
#tmx_map correspond a la carte dans laquel on se trouve
def check_collision(x, y, id, tmx_map):

    # Calculez les indices de tuiles correspondant aux coordonnées du personnage
    tile_x = x // tmx_map.tilewidth
    tile_y = y // tmx_map.tileheight

    # Vérifiez s'il y a une collision à ces indices de tuiles
    if id in tmx_map.get_tile_properties(tile_x, tile_y, 0):
        return True  # Collision détectée
    return False  # Pas de collision

def get_score():  
    dict_score = {}
    #recuperation des scores sauvegardés
    try:
        with open("./data/score.pkl", "rb") as fichier:
            dict_score = pickle.load(fichier)
    except (EOFError, FileNotFoundError):
        # Gérer le cas où le fichier est vide ou n'existe pas
        dict_score = {}
    return dict_score

def ajout_score(pseudo, score=0) :
    dict_score = get_score()
    dict_score[pseudo] = score
    with open("./data/score.pkl", "wb") as fichier:
        pickle.dump(dict_score, fichier)