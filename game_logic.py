import pickle
import character
import pygame
import projectile

#x et y correspondent au coordonées du personnage, ou n'importe quel autre objet sur la carte.
#tmx_data correspond aux données de la map chargée
#renvoi wall si la collision ne permets pas au personnage de passer, 
#room#xx si le peronnage rentre la une piece numero xx
#damage#xx si le personnage prends xx degats 
#none sinon
def check_collision(character_x, character_y, tmx_data):
    
    for layer in tmx_data.visible_layers:
       
        if layer.data:
            #print(" x : " + str(character_x) + " y : "+str(character_y)+ " calc1 : "+ str(character_x // 32)+ " calc2 : " + str(character_y // 32))
            tile = layer.data[character_y // tmx_data.tileheight][character_x // tmx_data.tilewidth]
            if tile:
                name = layer.name 
                print(f"Coordonnées ({character_x}, {character_y}) correspondent au layer : {layer.name}")
                if "99" in name:
                    
                    return "wall"
                
            return "none"
    
    


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

def move_character(character_obj, key, map_data):
    
    if key[pygame.K_q]:
        coll = check_collision(character_obj.get_x(), character_obj.get_y(), map_data)
        if coll != "wall":
            character_obj.move_left()  # Appel à la méthode move_left du personnage
    elif key[pygame.K_d]:
        coll = check_collision(character_obj.get_x(), character_obj.get_y(), map_data)
        if coll != "wall":
            character_obj.move_right()  # Appel à la méthode move_right du personnage
    if key[pygame.K_z]:
        coll = check_collision(character_obj.get_x(), character_obj.get_y(), map_data)
        if coll != "wall":
            character_obj.move_up()  # Appel à la méthode move_up du personnage
    elif key[pygame.K_s]:
        coll = check_collision(character_obj.get_x(), character_obj.get_y(), map_data)
        if coll != "wall":
            character_obj.move_down()  # Appel à la méthode move_down du personnage

def tirer(character_x,character_y,souris_x,souris_y,screen):
    if(souris_x> 1024/2):
        direction =0
    else:
        direction =1
    un_proj = projectile.Projectile(character_x,character_y, direction)
    return un_proj