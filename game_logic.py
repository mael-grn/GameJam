import pickle
import character
import pygame
import projectile

#x et y correspondent au coordonées du personnage, ou n'importe quel autre objet sur la carte.
#id represente l'identifiant de l'objet avec lequel on veut detecter la collision, dans le fichier tmx
#tmx_map correspond a la carte dans laquel on se trouve
def check_collision(character_x, character_y, tmx_data):
    
    for layer in tmx_data.visible_layers:
       
        if layer.data:
            tile = layer.data[character_x // tmx_data.tileheight][character_y // tmx_data.tilewidth]
            if tile:
                print(f"Coordonnées ({character_x}, {character_y}) correspondent au layer : {layer.name}")


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

def move_character(character_obj, key, map):
    
    if key[pygame.K_q]:

        character_obj.move_left()  # Appel à la méthode move_left du personnage
    elif key[pygame.K_d]:
        character_obj.move_right()  # Appel à la méthode move_right du personnage
    if key[pygame.K_z]:
        character_obj.move_up()  # Appel à la méthode move_up du personnage
    elif key[pygame.K_s]:
        character_obj.move_down()  # Appel à la méthode move_down du personnage

def tirer(character_x,character_y,souris_x,souris_y,screen):
    if(souris_x> 1024/2):
        direction =0
    else:
        direction =1
    un_proj = projectile.Projectile(character_x,character_y, direction)
    return un_proj