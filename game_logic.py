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
                            return {2 : ""} #retour du code 2 (collision)
                        elif "vers" in layer.name:
                            return {1 : layer.name.split("_")}
                        
    return {0:""}
                
            
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
        if not 2 in coll:
            character_obj.move_left()  # Appel à la méthode move_left du personnage
    elif key[pygame.K_d]:
        coll = check_collision(get_next_rect(rect, "r"), map_data)  #simulation mouvement à droite
        if not 2 in coll:
            character_obj.move_right()  # Appel à la méthode move_right du personnage
    if key[pygame.K_z]:
        coll = check_collision(get_next_rect(rect, "u"), map_data)  #simulation mouvement à haut
        if not 2 in coll:
            character_obj.move_up()  # Appel à la méthode move_up du personnage
    elif key[pygame.K_s]:
        coll = check_collision(get_next_rect(rect, "s"), map_data)  #simulation mouvement à bas
        if not 2 in coll:
            character_obj.move_down()  # Appel à la méthode move_down du personnage

def tirer(character_x,character_y,souris_x,souris_y,screen,path):
    un_proj = projectile.Projectile(character_x,character_y,souris_x,souris_y, path)
    return un_proj

def afficher_map(screen, tmx_map):
    for layer in tmx_map.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, image in layer.tiles():
                    screen.blit(image, (x * tmx_map.tilewidth, y * tmx_map.tileheight))

def affiche_dialogue(screen, text):

    running = True
    clock = pygame.time.Clock()
    dt = 0

    button_path = "./assets/buttons/enter.png"

    #traitement du texte (retour à la ligne au bout de 62 caractères)

    while running:

        #afficher la fenetre de dialogue
        bg = pygame.image.load("./assets/img/dialog.png")
        bg_big = pygame.transform.scale(bg, (bg.get_width()*4, bg.get_height()*4))
        bg_rec = bg_big.get_rect()
        bg_rec.center = ((screen.get_width() // 2),screen.get_height()- (50 +bg.get_height()*2) )
        screen.blit(bg_big, bg_rec)
        #affichage du texte

        font = pygame.font.Font("./assets/fonts/pinball.ttf", 20) 
        line_height = font.get_linesize() +10


        lines = wrap_text(text, 55)
        count =1
        
        for line in lines:
            
            content = font.render(line, True, (0,0,0))
            content_rec = content.get_rect()
            content_rec.topleft=(110, (screen.get_height() - bg.get_height()*4.5) + count*line_height)
            screen.blit(content, content_rec)
            count += 1


        #afficher du bouton entrer
        button = pygame.image.load(button_path)
        button_big = pygame.transform.scale(button, (button.get_width()*4, button.get_height()*4))
        button_rec = button_big.get_rect()
        button_rec.center = ((screen.get_width() -150),screen.get_height()- 100 )
        screen.blit(button_big, button_rec)



        # Parcourt tous les evenements pour les traiter
        for event in pygame.event.get():
            # QUIT signifie que l'utilisateur a fermé la fenêtre
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            #si les touches du clavier sont pressées
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    button_path = "./assets/buttons/enter_press.png"


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    running = False
                    
                    

                    

        # Comme les dessions sont fait dans un buffer, permute le buffer
        pygame.display.flip()
        # Limite le frame rate à 60 images par secondes et retourne le temps réel passé
        dt = clock.tick(60) 

def wrap_text(text, max_line_length=62):

    nbr_ligne = len(text)//max_line_length +1
    lines = []

    for i in range(0, nbr_ligne):
        start = i * max_line_length
        end = (i + 1) * max_line_length
        ligne = text[start:end]
        lines.append(ligne)

    return lines
