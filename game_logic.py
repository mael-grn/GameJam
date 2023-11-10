import pickle
import character
import pygame
import projectile
import enemy
import math
import pytmx
import constants
import piece
import screens.main_menu as main_menu

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
                for y in range (rect.top // tmx_data.tileheight+2, rect.top // tmx_data.tileheight + rect.height // tmx_data.tileheight+2):
                    tile = layer.data[y][x]
                    if tile:
                        #si le rectangle est superposé à un mur (code 99 dans le nom du layer):
                        if "99" in layer.name:
                            if "foodtruck" in layer.name:
                                return {2 : "foodtruck"} #retour du code 2 (collision)
                            return {2 : ""}
                        elif "vers" in layer.name:
                            return {1 : layer.name.split("_")[1]}
                        elif "fin" in layer.name:
                            
                            return {3 : ""}
                        
                        
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


def set_score(pseudo, score=0) :
    dict_score = get_score()
    dict_score[pseudo] = score
    with open("./data/score.pkl", "wb") as fichier:
        pickle.dump(dict_score, fichier)


def move_character(screen,character_obj, key, map_data): 
    rect = character_obj.get_rect()
    

    if key[pygame.K_q]:
        coll = check_collision(get_next_rect(rect, "l"), map_data) #simulation mouvement à gauche
        if not 2 in coll:
            character_obj.move_left()  # Appel à la méthode move_left du personnage
        elif 2 in coll and coll[2]=="foodtruck":
            character_obj.move_right()
            character_obj.echange_foodtruck(affiche_dialogue(screen, "Si vous avez 3 pièces sur votre compte Izly, vous pouvez acheter un sawndwich qui vous donnera 1 coeur suplémentaire ( E pour annuler )", [2]))
            

    elif key[pygame.K_d]:
        coll = check_collision(get_next_rect(rect, "r"), map_data)  #simulation mouvement à droite
        if not 2 in coll:
            character_obj.move_right()  # Appel à la méthode move_right du personnage
        elif 2 in coll and coll[2]=="foodtruck":
            character_obj.move_left()
            character_obj.echange_foodtruck(affiche_dialogue(screen, "Si vous avez 3 pièces sur votre compte Izly, vous pouvez acheter un sawndwich qui vous donnera 1 coeur suplémentaire ( E pour annuler )", [2]))

    if key[pygame.K_z]:
        coll = check_collision(get_next_rect(rect, "u"), map_data)  #simulation mouvement à haut
        if not 2 in coll:
            character_obj.move_up()  # Appel à la méthode move_up du personnage
        elif 2 in coll and coll[2]=="foodtruck":
            character_obj.move_down()
            character_obj.echange_foodtruck(affiche_dialogue(screen, "Si vous avez 3 pièces sur votre compte Izly, vous pouvez acheter un sawndwich qui vous donnera 1 coeur suplémentaire ( E pour annuler )", [2]))

    elif key[pygame.K_s]:
        coll = check_collision(get_next_rect(rect, "d"), map_data)  #simulation mouvement à bas
        if not 2 in coll:
            character_obj.move_down()  # Appel à la méthode move_down du personnage
        elif 2 in coll and coll[2]=="foodtruck":
            character_obj.move_up()
            character_obj.echange_foodtruck(affiche_dialogue(screen, "Si vous avez 3 pièces sur votre compte Izly, vous pouvez acheter un sawndwich qui vous donnera 1 coeur suplémentaire ( E pour annuler )", [2]))

def tirer(character_x,character_y,souris_x,souris_y,screen,path, character=False):
    un_proj = projectile.Projectile(character_x,character_y,souris_x,souris_y, path, character)
    return un_proj

def afficher_map(screen, tmx_map):
    for layer in tmx_map.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, image in layer.tiles():
                    screen.blit(image, (x * tmx_map.tilewidth, y * tmx_map.tileheight))

#other_button est une liste d'autre bouton à etre pris en compte. si passé en parametre, alors :
#   - si 1 dans la liste : bouton a apparait, la fonction renvoie 1 si pressé
#   - si 2 dans la liste : bouton e apparait, la fonction renvoie 2 si pressé
#la fonction renvoi 0 si entrer (bouton pour fermer le dialogue) est pressé

def affiche_dialogue(screen, text, other_button= []):

    running = True
    clock = pygame.time.Clock()
    dt = 0

    enter_button_path = "./assets/buttons/enter.png"
    a_button_path = "./assets/buttons/a.png"
    e_button_path = "./assets/buttons/e.png"

    there_is_a = 1 in other_button
    there_is_e = 2 in other_button

    font = pygame.font.Font(constants.ROBOTO_PATH, 20) 



    #traitement du texte (retour à la ligne au bout de 62 caractères)

    while running:

        if pygame.mixer.music.get_busy() == 0:  # La musique s'est terminée
                pygame.mixer.music.load('./assets/music/intro_chill.mp3')
                pygame.mixer.music.play()

        #afficher la fenetre de dialogue
        bg = pygame.image.load("./assets/img/dialog.png")
        bg_big = pygame.transform.scale(bg, (bg.get_width()*4, bg.get_height()*4))
        bg_rec = bg_big.get_rect()
        bg_rec.center = ((screen.get_width() // 2),screen.get_height()- (50 +bg.get_height()*2) )
        screen.blit(bg_big, bg_rec)
        #affichage du texte

        
        line_height = font.get_linesize() +2


        lines = wrap_text(text, 68)
        count =1
        
        for line in lines:
            
            content = font.render(line, True, (0,0,0))
            content_rec = content.get_rect()
            content_rec.topleft=(110, (screen.get_height() - bg.get_height()*4.5) + count*line_height)
            screen.blit(content, content_rec)
            count += 1


        #afficher du bouton entrer
        enter_button = pygame.image.load(enter_button_path)
        enter_button_big = pygame.transform.scale(enter_button, (enter_button.get_width()*4, enter_button.get_height()*4))
        enter_button_rec = enter_button_big.get_rect()
        enter_button_rec.center = ((screen.get_width() -150),screen.get_height()- 50 )
        screen.blit(enter_button_big, enter_button_rec)

        #afficher le bouton a s'il existe
        a_button = pygame.image.load(a_button_path)
        a_button_big = pygame.transform.scale(a_button, (a_button.get_width()*4, a_button.get_height()*4))
        a_button_rec = a_button_big.get_rect()
        a_button_rec.center = ((screen.get_width() -250),screen.get_height()- 50 )

        #afficher le bouton e s'il existe
        e_button = pygame.image.load(e_button_path)
        e_button_big = pygame.transform.scale(e_button, (e_button.get_width()*4, e_button.get_height()*4))
        e_button_rec = e_button_big.get_rect()
        e_button_rec.center = ((screen.get_width() -320),screen.get_height()- 50 )

        if there_is_a:
            screen.blit(a_button_big, a_button_rec)

        if there_is_e:
            screen.blit(e_button_big, e_button_rec)



        # Parcourt tous les evenements pour les traiter
        for event in pygame.event.get():
            # QUIT signifie que l'utilisateur a fermé la fenêtre
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            
            if event.type == pygame.MOUSEBUTTONUP:

                #si clique sur bouton jouer
                if enter_button_rec.collidepoint(event.pos):
                    running = False
                    return 0
                if a_button_rec.collidepoint(event.pos) and there_is_a:
                    running = False
                    return 1
                if e_button_rec.collidepoint(event.pos) and there_is_e:
                    running = False
                    return 2
                
            if event.type == pygame.MOUSEMOTION:
                if enter_button_rec.collidepoint(event.pos):
                    # Changer la couleur du texte lorsque la souris survole le bouton
                    enter_button_path = "./assets/buttons/enter_press.png"
                else:
                    enter_button_path = "./assets/buttons/enter.png"
                if a_button_rec.collidepoint(event.pos) and there_is_a:
                    # Changer la couleur du texte lorsque la souris survole le bouton
                    a_button_path = "./assets/buttons/a_press.png"
                else:
                    a_button_path = "./assets/buttons/a.png"
                if e_button_rec.collidepoint(event.pos) and there_is_e:
                    # Changer la couleur du texte lorsque la souris survole le bouton
                    e_button_path = "./assets/buttons/e_press.png"
                else:
                    e_button_path = "./assets/buttons/e.png"

            #si les touches du clavier sont pressées
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    enter_button_path = "./assets/buttons/enter_press.png"
                
                if event.key == pygame.K_a and there_is_a:
                    a_button_path = "./assets/buttons/a_press.png"

                if event.key == pygame.K_e and there_is_e:
                    e_button_path = "./assets/buttons/e_press.png"


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    running = False
                    return 0
                
                if event.key == pygame.K_a and there_is_a:
                    running = False
                    return 1

                if event.key == pygame.K_e and there_is_e:
                    running = False
                    return 2
                    
                    

                    

        # Comme les dessions sont fait dans un buffer, permute le buffer
        pygame.display.flip()
        # Limite le frame rate à 60 images par secondes et retourne le temps réel passé
        dt = clock.tick(60) 

    pygame.mixer.music.stop()

def wrap_text(text, max_line_length=62):


    # On sépare le texte en mots.
# On initialise la liste des lignes avec une ligne vide.
    lines = [""]

    # On sépare le texte en mots.
    words = text.split(" ")

    # On parcourt les mots un par un.
    for word in words:
        # Si la ligne actuelle est trop longue, on la termine par des points de suspension.
        if len(lines[-1]) + len(word) > max_line_length:
            lines.append("")

        # On ajoute le mot à la ligne actuelle.
        lines[-1] += word + " "

    # On enlève les points de suspension de la dernière ligne.
    if lines[-1].endswith("..."):
        lines[-1] = lines[-1][:-3]

    return lines

#gere les impacts des projectiles sur les monstres
def impact_handler(character_obj, pieces, monstres, tmx_data, indices_proj_a_supprimer):
    for index, proj in enumerate(character_obj.get_proj()):
            rectangle = pygame.Rect(proj.get_x(),proj.get_y(),50,50)
            proj.update()
            
            for monstre in monstres:
                if proj.rect.colliderect(monstre.rect):
                    monstre.take_damage(1)  # Chaque projectile inflige 1 point de dégât
                    if not monstre.is_alive() and monstre.attaque !=3:
                        une_piece=piece.Piece(monstre.rect.x, monstre.rect.y, "./assets/img/piece.png", "./assets/img/pieceReverse.png")
                        pieces.append(une_piece)
                        if monstre.attaque !=3:
                            monstres.remove(monstre)  # Supprimez l'ennemi s'il n'a plus de points de vie
                    # indices_proj_a_supprimer.append(index)  # Ajoutez l'index du projectile à supprimer à la liste
                    break  # Sortez de la boucle des ennemis, car le projectile a déjà touché un ennemies
            if len(monstres)>0:
                if proj.rect.colliderect(monstre.rect) or 2 in check_collision(rectangle,tmx_data):
                    indices_proj_a_supprimer.append(index)  # Ajoutez l'index du projectile à supprimer à la liste    
            else:
                if 2 in check_collision(rectangle,tmx_data):
                   indices_proj_a_supprimer.append(index)  # Ajoutez l'index du projectile à supprimer à la liste 
    
       
    return indices_proj_a_supprimer

def coin_handler(character_obj, pieces, screen, indices_proj_a_supprimer):
    if len(pieces)>0:
        for piece_obj in pieces:
            piece_obj.draw(screen)
            if piece_obj.check_collision(character_obj.get_rect()):
                character_obj.increase_pieces(1)
                pieces.remove(piece_obj)  # Supprimez la pièce

    # Supprimez les projectiles de character_obj à partir de la fin pour éviter les problèmes d'index
    indices_proj_a_supprimer.reverse()  # Inversez la liste des indices
    for index in indices_proj_a_supprimer:
        character_obj.del_proj(index)

    # Affichez les projectiles restants
    for proj in character_obj.get_proj():
        proj.draw(screen)

    return indices_proj_a_supprimer
        
def play_sound(sound):
    # Initialisation de Pygame
    pygame.init()

    # Créez un objet mixer pour gérer les sons
    pygame.mixer.init()

    # Chargez le fichier audio que vous souhaitez jouer
    son = pygame.mixer.Sound('./assets/sounds/'+sound+'.mp3')

    # Jouez le son
    son.play()

def affiche_pause(screen, character_obj):



    running = True
    clock = pygame.time.Clock()
    dt = 0

    resume_button_path = "./assets/buttons/normal.png"
    quit_button_path = "./assets/buttons/normal.png"



    #traitement du texte (retour à la ligne au bout de 62 caractères)

    while running:

        font = pygame.font.Font("./assets/fonts/pinball.ttf", 30) 
        font_big = pygame.font.Font("./assets/fonts/pinball.ttf", 50)

        # Affichage du titre
        #arriere plan
        titre_bg = pygame.image.load("./assets/img/title_bg.png")
        #redimmensionner le logo
        titre_bg_big = pygame.transform.scale(titre_bg, (titre_bg.get_width()*4, titre_bg.get_height()*4))
        titre_bg_rec = titre_bg_big.get_rect()
        titre_bg_rec.center = ((screen.get_width() // 2), screen.get_height()//2)
        screen.blit(titre_bg_big, titre_bg_rec)
        #texte
        titre = font_big.render("PAUSE", True, (0,0,0))
        titre_rec = titre.get_rect()
        titre_rec.center = (screen.get_width() // 2, screen.get_height()//2)
        screen.blit(titre, titre_rec)

        #afficher du bouton resume
        resume_button = pygame.image.load(resume_button_path)
        resume_button_big = pygame.transform.scale(resume_button, (resume_button.get_width()*4, resume_button.get_height()*4))
        resume_button_rec = resume_button_big.get_rect()
        resume_button_rec.center = ((screen.get_width() //3),screen.get_height()//3 *2 )
        screen.blit(resume_button_big, resume_button_rec)
        #texte
        resume = font.render("RESUME", True, (0,0,0))
        resume_rec = resume.get_rect()
        resume_rec.center = ((screen.get_width() //3),screen.get_height()//3 *2)
        screen.blit(resume, resume_rec)

        #afficher le bouton quitter
        quit_button = pygame.image.load(quit_button_path)
        quit_button_big = pygame.transform.scale(quit_button, (quit_button.get_width()*4, quit_button.get_height()*4))
        quit_button_rec = quit_button_big.get_rect()
        quit_button_rec.center = ((screen.get_width() //3)*2,screen.get_height()//3 *2)
        screen.blit(quit_button_big, quit_button_rec)
        #texte
        quit = font.render("MENU", True, (0,0,0))
        quit_rec = quit.get_rect()
        quit_rec.center = (screen.get_width() //3)*2,screen.get_height()//3 *2
        screen.blit(quit, quit_rec)

        # Parcourt tous les evenements pour les traiter
        for event in pygame.event.get():
            # QUIT signifie que l'utilisateur a fermé la fenêtre
            if event.type == pygame.QUIT:
                running = False
                bonus = 0
                if character_obj.boss_defeated:
                    bonus=50
                set_score(character_obj.pseudo, character_obj.pieces*5 + character_obj.keys*15 + bonus)
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Si clique sur bouton quitter
                if quit_button_rec.collidepoint(event.pos):
                    quit_button_path = "./assets/buttons/press.png"
                    print(True)
                #si clique sur bouton jouer
                if resume_button_rec.collidepoint(event.pos):
                    resume_button_path = "./assets/buttons/press.png"



            if event.type == pygame.MOUSEBUTTONUP:
                # Si clique sur bouton quitter
                if quit_button_rec.collidepoint(event.pos):
                    play_sound("clic")
                    running=False
                    bonus = 0
                    if character_obj.boss_defeated:
                        bonus=50
                    print(character_obj.pseudo + " : " + str(character_obj.pieces))
                    set_score(character_obj.pseudo, character_obj.pieces*5 + character_obj.keys*15 + bonus)
                    pygame.mixer.music.load('./assets/music/menu.mp3')
                    pygame.mixer.music.play()
                    main_menu.ouvrir_menu(screen)

  
                if resume_button_rec.collidepoint(event.pos):
                    play_sound("clic")
                    running=False
                    


            if event.type == pygame.MOUSEMOTION:
                if quit_button_rec.collidepoint(event.pos):
                    # Changer la couleur du texte lorsque la souris survole le bouton
                    quit_button_path = "./assets/buttons/over.png"
                else:
                    quit_button_path = "./assets/buttons/normal.png"

                if resume_button_rec.collidepoint(event.pos):
                    # Changer la couleur du texte lorsque la souris survole le bouton
                    resume_button_path = "./assets/buttons/over.png"
                else:
                    resume_button_path = "./assets/buttons/normal.png"




                    
                    

                    

        # Comme les dessions sont fait dans un buffer, permute le buffer
        pygame.display.flip()
        # Limite le frame rate à 60 images par secondes et retourne le temps réel passé
        dt = clock.tick(60) 



def set_difficulty(diff):
    if "demo" in diff:
        constants.COLLECTE_CLEE = False
        constants.INVINCIBILITE=True
        constants.CHARACTER_SPEED=7
    elif "easy" in diff:
        constants.PROJ_SPEED=3
        constants.CHARACTER_SPEED=7
    #normal prends les valeurs par defaut
    elif "hard" in diff:
        constants.PROJ_SPEED = 7
        constants.INVINCIBILITE_TEMPORAIRE=False
