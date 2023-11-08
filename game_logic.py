import pickle
import character
import pygame
import projectile
import enemy
import math
import pytmx
import constants

#x et y correspondent au coordonées du personnage, ou n'importe quel autre objet sur la carte.
#tmx_data correspond aux données de la map chargée
#renvoi 2 si la collision ne permets pas au personnage de passer, 
#room#xx si le peronnage rentre la une piece numero xx
#damage#xx si le personnage prends xx degats 
#0 sinon
#format hitbox :
#a b
#c d
def check_collision(rect, tmx_data):
    #pour chaque layer:
    for layer in tmx_data.visible_layers:
        #s'il existe :
        if layer.data:
            #on regarde pour chaque tuiles correspondant au rectangle du personnage sur la carte :
            for x in range (rect.left // tmx_data.tilewidth +1, rect.left // tmx_data.tilewidth + rect.width // tmx_data.tilewidth+1):
                for y in range (rect.top // tmx_data.tileheight+1, rect.top // tmx_data.tileheight + rect.height // tmx_data.tileheight+1):
                    tile = layer.data[y][x]
                    if tile:
                        #si le rectangle est superposé à un mur (code 99 dans le nom du layer):
                        if "99" in layer.name:
                            return 2 #retour du code 2 (collision)
                
            
#direction = u pour up, d pour down, l pour left et r pour right
#retourne un nouveau rectangle correspondant à la prochaine position du rectangle en parametre
def get_next_rect(rect, direction):
    if "u" in direction:
        rectangle = pygame.Rect(rect.x, rect.y-constants.CHARACTER_SPEED, rect.width, rect.height)
    elif "d" in direction:
        rectangle = pygame.Rect(rect.x, rect.y+constants.CHARACTER_SPEED, rect.width, rect.height)
    elif "l" in direction:
        rectangle = pygame.Rect(rect.x-constants.CHARACTER_SPEED, rect.y, rect.width, rect.height)
    elif "r" in direction:
        rectangle = pygame.Rect(rect.x+constants.CHARACTER_SPEED, rect.y, rect.width, rect.height)
    else:
        rectangle = pygame.Rect(rect.x, rect.y, rect.width, rect.height)
    
    return rectangle


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
    x = rect.centerx
    y = rect.centery
    w = rect.width
    h = rect.height
    if key[pygame.K_q]:
        coll = check_collision(get_next_rect(rect, "l"), map_data) #simulation mouvement à gauche
        if coll != 2:
            character_obj.move_left()  # Appel à la méthode move_left du personnage
    elif key[pygame.K_d]:
        coll = check_collision(get_next_rect(rect, "r"), map_data)  #simulation mouvement à droite
        if coll != 2:
            character_obj.move_right()  # Appel à la méthode move_right du personnage
    if key[pygame.K_z]:
        coll = check_collision(get_next_rect(rect, "u"), map_data)  #simulation mouvement à haut
        if coll != 2:
            character_obj.move_up()  # Appel à la méthode move_up du personnage
    elif key[pygame.K_s]:
        coll = check_collision(get_next_rect(rect, "s"), map_data)  #simulation mouvement à bas
        if coll != 2:
            character_obj.move_down()  # Appel à la méthode move_down du personnage

def tirer(character_x,character_y,souris_x,souris_y,screen,path):
    un_proj = projectile.Projectile(character_x,character_y,souris_x,souris_y, path)
    return un_proj