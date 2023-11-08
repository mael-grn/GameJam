import pygame
import character
import screens.error as error
import pytmx
import game_logic
import enemy
import screens.game_over
import time
import piece
import salle

def ouvrir_niveau(screen):
    # Définit l'horloge pour connaître le temps qui a passé
    clock = pygame.time.Clock()
    # Pour savoir quand la boucle du jeu se termine
    running = True
    # Le temps passé entre deux rafraîchissements de l'écran en millisecondes
    dt = 0

    #variables d'etat
    current_room = "sol"
    there_is_monsters = True
    pieces=[]
    tire = False #si on peut tirer
    delay =0 #control de la cadence de tire

    character_obj = character.Character(450, 600)  # Position initiale du personnage

    #montre salle 21
    monstre21=enemy.Enemy("monstre21",450,180,100,5,"./assets/img/mechant_pc.png")

    # Création des salles
    amphiC1 = salle.Salle("amphiC1", character_obj,[], [], {"amphi" : (19*32, 7*32), "etage1" : (16*32, 17*32)})
    amphi = salle.Salle("amphi", character_obj, [], [], {"amphiC1" : (6*32, 20*32)})
    couloir1 = salle.Salle("couloir1", character_obj, [], [], {"salle33" : (10*32, 9*32), "salle39" : (25*32, 9*32), "sol" : (29*32, 12*32), "couloir2" : (2*32, 12*32)}) 
    couloir2 = salle.Salle("couloir2", character_obj, [], [], {"couloir3" : (2*32, 12*32), "sousSolCouloir1" : (17*32, 10*32), "couloir1" : (29*32, 12*32)})
    couloir3 = salle.Salle("couloir3", character_obj, [], [], {"salle21" : (18*32, 10*32), "couloir2" : (29*32, 12*32)})
    etage1Couoir1 = salle.Salle("etage1Couoir1", character_obj, [], [], {"etage1" : (2*32, 12*32), "salle110" : (10*32, 10*32), "salle115" : (25*32, 10*32)})
    etage1 = salle.Salle("etage1", character_obj, [], [], {"sol" : (8*32, 12*32), "amphiC1" : (24*32, 10*32), "etage1Couloir1" : (25*32, 17*32)})
    foodtruck = salle.Salle("foodtruck", character_obj, [], [], {"sol" : (22*32, 20*32), "sousSolCouloir2" : (5*32, 9*32)})
    salle21 = salle.Salle("salle21", character_obj, [], [], {"couloir3" : (16*32, 19*32)}) 
    salle33 = salle.Salle("salle33", character_obj, [], [], {"couloir1" : (17*32, 20*32)})
    salle39 = salle.Salle("salle39", character_obj, [], [], {"couloir1" : (16*32, 18*32)})
    salle110 = salle.Salle("salle110", character_obj, [], [], {"etage1Couloir1" : (8*32, 19*32)})
    salle115 = salle.Salle("salle115", character_obj, [], [], {"etage1Couloir1" : (16*32, 19*32)})
    salleS35 = salle.Salle("salleS35", character_obj, [], [], {"sousSolCouloir2" : (14*32, 14*32)})
    salleS36 = salle.Salle("salleS36", character_obj, [], [], {"sousSolCouloir1" : (14*32, 14*32)})
    salleS37 = salle.Salle("salleS37", character_obj, [], [], {"sousSolCouloir3" : (24*32, 18*32)})
    sol = salle.Salle("sol", character_obj, [], [], {"couloir1" : (4*32, 14*32),"etage1" : (7*32, 9*32), "foodtruck" : (19*32, 9*32)})
    sousSolCouloir1 = salle.Salle("sousSolCouloir1", character_obj, [], [], {"sousSolCouloir2" : (2*32, 12*32), "couloir2" : (10*32, 10*32), "salleS36" : (25*32, 10*32), "sousSolCouloir3" : (29*32, 12*32)})
    sousSolCouloir2 = salle.Salle("sousSolCouloir2", character_obj, [], [], {"foodtruck" : (9*32, 10*32), "sousSolCouloir1" : (29*32, 12*32), "salleS35" : (18*32, 10*32)})
    sousSolCouloir3 = salle.Salle("sousSolCouloir3", character_obj, [], [], {"salleS37" : (11*32, 10*32), "sousSolCouloir1" : (2*32, 12*32)})

    room_list = {}
    for salle_item in [amphiC1, amphi, couloir1, couloir2, couloir3, etage1Couoir1, etage1, foodtruck, salle21, salle33, salle39, salle110, salle115, salleS35, salleS36, salleS37, sol, sousSolCouloir1, sousSolCouloir2, sousSolCouloir3]:
        room_list[salle_item.map] = salle_item
    #maj des salles

    salle21.enemies.append(monstre21)

    current_salle=sol ## Salle de spawn

    
    tmx_map = pytmx.load_pygame('./assets/maps/' + current_salle.map+".tmx")
    tmx_map_data = pytmx.TiledMap('./assets/maps/' + current_salle.map+".tmx")

    
    

     # Chargement de la carte




    
    monstres = []  # Créez une liste vide pour stocker les monstres
    monstre1 = enemy.Enemy("Monstre1", 200, 200, 100, 10, "./assets/img/mechant_pc.png")
    monstre2 = enemy.Enemy("Monstre2", 300, 300, 100, 10, "./assets/img/mechant_pc.png")
    monstre3 = enemy.Enemy("Monstre3", 400, 400, 100, 10, "./assets/img/mechant_pc.png")
    monstres.append(monstre1)
    monstres.append(monstre2)
    monstres.append(monstre3)



    #musique
    pygame.mixer.init()
    pygame.mixer.music.load('./assets/music/intro_chill.mp3')
    pygame.mixer.music.play()

    


    while running:

        screen.fill((0, 0, 0))

        #ne pas activer le tire si aucun monstre
        if len(monstres)==0 and not there_is_monsters:
            tire = False

#----------------------------------------------------------------------------------------------------------------gestion musique
        if pygame.mixer.music.get_busy() == 0:  # La musique s'est terminée
                if(tire):
                    pygame.mixer.music.load('./assets/music/intro_chill.mp3')
                    pygame.mixer.music.play()
                    tire = False
                else:
                    pygame.mixer.music.load('./assets/music/combat.mp3')
                    pygame.mixer.music.play()
                    tire = True

#----------------------------------------------------------------------------------------------------------------map
        #afficher la map
        game_logic.afficher_map(screen, tmx_map)

        #gestion changement de salle
        coll = game_logic.check_collision(character_obj.get_rect(), tmx_map_data)

        #code changement salle : 1 : xx ou xx est le nom de la salle
        if 1 in coll:
            if current_room != coll[1]:
                char_rect = character_obj.get_rect()
                next_room = room_list[coll[1]]
                print(next_room.map)
                char_rect.centerx = next_room.entry[current_room][0]
                char_rect.centery = next_room.entry[current_room][1]
                current_room = coll[1]
                tmx_map = pytmx.load_pygame('./assets/maps/' + current_room + '.tmx')
                tmx_map_data = pytmx.TiledMap('./assets/maps/' + current_room + '.tmx')
                
        
#-----------------------------------------------------------------------------------------------------------------affichage dialogue debut
        if dt==0: #si toute premiere iteration boucle (debut du jeu)
            game_logic.affiche_dialogue(screen, "Tot ce matin, je me suis decide a me rendre a l'IUT2 de Grenoble pour terminer mon TP en informatique. Pourtant, a cette heure matinale, il n'y a personne en vue. Une atmosphere etrangement calme regne dans les couloirs, eveillant en moi un sentiment d'inquietude. Que se trame-t-il ? C'est le debut d'une journee mysterieuse, et je suis bien determine a en decouvrir les secrets.")

#----------------------------------------------------------------------------------------------------------------afficher elements
        #coeurs
        character_obj.draw_hearts(screen)
        character_obj.draw_pieces(screen)

        #personnage
        game_logic.move_character(character_obj, pygame.key.get_pressed(), tmx_map_data)
        character_obj.draw(screen)

#------------------------------------------------------------------------------------------------------------------- event handler
        for event in pygame.event.get():

            # fermer la fenetre
            if event.type == pygame.QUIT:
                running = False

            #gestion du tire 
            if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1 and tire and len(character_obj.get_proj())<5:
                mouse_x, mouse_y = event.pos
                character_obj.add_proj(game_logic.tirer(character_obj.get_centre_x(),character_obj.get_centre_y(),mouse_x,mouse_y,screen,"./assets/img/note_tire.png"))
                tire = False
                while(delay<1.0):
                    delay += 1/60
                    tire = True
                delay=0

#---------------------------------------------------------------------------------------------------------------gestion du jeu (monstre, piece, projectile)
        # Liste des indices des projectiles à supprimer
        indices_proj_a_supprimer = []
        indices_proj_a_supprimer = game_logic.impact_handler(character_obj, pieces, monstres, tmx_map_data, indices_proj_a_supprimer)        
        indices_proj_a_supprimer = game_logic.coin_handler(character_obj, pieces, screen, indices_proj_a_supprimer)

        #-------------------------------------------------------------------------------------------------attaque (projectiles) des monstres et affichage
        
        if there_is_monsters:
            for monstre in monstres:
                current_time = time.time()  # Obtenez le temps actuel

                # Vérifiez si suffisamment de temps s'est écoulé depuis le dernier tir
                if current_time - monstre.last_shot_time >= 2.0:
                    # Permet à l'ennemi de tirer un projectile
                    monstre.add_proj(game_logic.tirer(monstre.get_centre_x(), monstre.get_centre_y(), character_obj.get_centre_x(), character_obj.get_centre_y(), screen, "./assets/img/tir_pc.png"))
                    monstre.last_shot_time = current_time  # Mettez à jour le temps du dernier tir

                num_proj = 0
                if len(monstre.get_proj()) > 0:
                    for proj in monstre.get_proj():
                        rectangle = pygame.Rect(proj.get_x(), proj.get_y(), 50, 50)
                        if proj.rect.colliderect(character_obj.rect) or 2 in game_logic.check_collision(rectangle, tmx_map_data):
                            monstre.del_proj(num_proj)  # Supprimez le projectile s'il touche un ennemi
                        proj.update()
                        proj.draw(screen)
                        num_proj = num_proj + 1

            
            for monstre in monstres:
                monstre.draw(screen)  # Dessinez le monstre à l'écran

            #gestion des degats que fonts les projectiles :
            for monstre in monstres:
                if(len(monstre.get_proj())>0):
                    for proj in monstre.get_proj():
                        if proj.rect.colliderect(character_obj.rect):
                            character_obj.take_damage(1)
                            character_obj.update()
                if character_obj.get_rect().colliderect(monstre.rect):
                    character_obj.take_damage(1)
                    character_obj.update()
                if not character_obj.is_alive():
                    # Le personnage est mort, vous pouvez gérer la fin du jeu ou d'autres actions appropriées
                    running = False
                    pygame.mixer.music.stop
                    pygame.mixer.music.load('./assets/music/menu.mp3')
                    pygame.mixer.music.play()
                    game_logic.play_sound("gameOver")
                    screens.game_over.ouvrir_game_over(screen)



        


        # Comme les dessins sont faits dans un buffer, permute le buffer
        pygame.display.flip()
        # Limite le frame rate à 60 images par seconde et retourne le temps réel passé
        dt = clock.tick(60) 

    # Termine proprement le module
    pygame.quit()
