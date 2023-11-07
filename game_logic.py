import pickle
import character
import pygame
import projectile
import enemy
import math
import pytmx

#x et y correspondent au coordonées du personnage, ou n'importe quel autre objet sur la carte.
#tmx_data correspond aux données de la map chargée
#renvoi 2 si la collision ne permets pas au personnage de passer, 
#room#xx si le peronnage rentre la une piece numero xx
#damage#xx si le personnage prends xx degats 
#0 sinon
#format hitbox :
#a b
#c d
def check_collision(x, y, w, h, tmx_data):

    for layer in tmx_data.visible_layers:
        
        

        if layer.data:
            tile = layer.data[y // tmx_data.tileheight][x // tmx_data.tilewidth]
            if tile:
                
                print(f"Coordonnées ({x}, {y}) correspondent au layer : {layer.name}")

                if "collision" in layer.name:
                    return 2

    


def get_score():  
    dict_score = {}
    #recuperation des scores sauvegardés
    try:
        with open("./data/score.pkl", "rb") as fichier:
            dict_temp = pickle.load(fichier)
            dict_score = {cle: valeur for cle, valeur in sorted(dict_temp.items(), key=lambda item: item[1], reverse=True)}

    except (EOFError, FileNotFoundError):
        # Gérer le cas où le fichier est vide ou n'existe pas
        dict_score = {}
    
    return dict_score

def ajout_score(pseudo, score=0) :
    dict_score = get_score()
    dict_score[pseudo] = score
    with open("./data/score.pkl", "wb") as fichier:
        pickle.dump(dict_score, fichier)

def move_character(character_obj, key, map_data):

    
    rect = character_obj.get_rect()
    x = rect.centerx+1
    y = rect.centery+1
    w = rect.width
    h = rect.height
    if key[pygame.K_q]:
        coll = check_collision(x-3, y+1, w, h, map_data) #simulation mouvement à gauche
        if coll != 2:
            character_obj.move_left()  # Appel à la méthode move_left du personnage
    elif key[pygame.K_d]:
        coll = check_collision(x+3, y-1, w, h, map_data) #simulation mouvement à droite
        if coll != 2:
            character_obj.move_right()  # Appel à la méthode move_right du personnage
    if key[pygame.K_z]:
        coll = check_collision(x+1, y-3, w, h, map_data) #simulation mouvement à haut
        if coll != 2:
            character_obj.move_up()  # Appel à la méthode move_up du personnage
    elif key[pygame.K_s]:
        coll = check_collision(x-1, y+3, w, h, map_data) #simulation mouvement à bas
        if coll != 2:
            character_obj.move_down()  # Appel à la méthode move_down du personnage

def tirer(character_x,character_y,souris_x,souris_y,screen,path):
    un_proj = projectile.Projectile(character_x,character_y,souris_x,souris_y, path)
    return un_proj