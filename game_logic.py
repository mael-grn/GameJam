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

    '''
    collision_detected = False

    for layer in tmx_data.visible_layers:
        if layer.data:
            left_top = ((x - w//2) // tmx_data.tilewidth, (y-h//2) // tmx_data.tileheight)
            right_top = ((x + w//2) // tmx_data.tilewidth, (y-h//2) // tmx_data.tileheight)
            left_bottom = ((x - w//2) // tmx_data.tilewidth, (y + h//2) // tmx_data.tileheight)
            right_bottom = ((x + w//2) // tmx_data.tilewidth, (y + h//2) // tmx_data.tileheight)

            # Generate additional points along the sides
            additional_points = []

            for i in range(left_top[1] + 1, left_bottom[1]):
                additional_points.append((left_top[0], i))
            for i in range(right_top[1] + 1, right_bottom[1]):
                additional_points.append((right_top[0], i))
            for i in range(left_top[0] + 1, right_top[0]):
                additional_points.append((i, left_top[1]))
            for i in range(left_bottom[0] + 1, right_bottom[0]):
                additional_points.append((i, left_bottom[1]))

            # Combine all points to check for collisions
            points_to_check = [left_top, right_top, left_bottom, right_bottom] + additional_points

            

            for point in points_to_check:
                if layer.data[point[1]][point[0]] and "99" in layer.name:
                    print("wall")
                    return 2
                    collision_detected = True
                    break

    if not collision_detected:
        print("none")
        return 0

    '''
            
            


    


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

    
    rect = character_obj.get_rect()
    x = rect.x
    y = rect.y
    w = rect.width
    h = rect.height
    if key[pygame.K_q]:
        coll = check_collision(x-2, y, w, h, map_data) #simulation mouvement à gauche
        if coll != 2:
            character_obj.move_left()  # Appel à la méthode move_left du personnage
    elif key[pygame.K_d]:
        coll = check_collision(x+2, y, w, h, map_data) #simulation mouvement à droite
        if coll != 2:
            character_obj.move_right()  # Appel à la méthode move_right du personnage
    if key[pygame.K_z]:
        coll = check_collision(x, y-2, w, h, map_data) #simulation mouvement à haut
        if coll != 2:
            character_obj.move_up()  # Appel à la méthode move_up du personnage
    elif key[pygame.K_s]:
        coll = check_collision(x, y+2, w, h, map_data) #simulation mouvement à bas
        if coll != 2:
            character_obj.move_down()  # Appel à la méthode move_down du personnage

def tirer(character_x,character_y,souris_x,souris_y,screen):
    un_proj = projectile.Projectile(character_x,character_y,souris_x,souris_y)
    return un_proj