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
import random
import key
import constants
import reveil
import screens.credit as credit

def ouvrir_niveau(screen, pseudo):
    # Définit l'horloge pour connaître le temps qui a passé
    clock = pygame.time.Clock()
    # Pour savoir quand la boucle du jeu se termine
    running = True
    # Le temps passé entre deux rafraîchissements de l'écran en millisecondes
    dt = 0
    affiche_dial_pc = False
    temps = 0
    deja_rentre_salle_pc = False
    #variables d'etat
    current_room = "sol"
    there_is_monsters = False
    pieces=[]
    tire = False #si on peut tirer
    delay =0 #control de la cadence de tire
    there_is_key=False


    current_room = "sol"
    
    character_obj = character.Character(450, 600, pseudo)  # Position initiale du personnage
    
    key_obj = key.Key(0, 0)


    #montres
    monstre21=enemy.Enemy("monstre21",450,180,100,5,"./assets/img/mechant_pc.png",1)
    monstre33_1 = enemy.Enemy("m33_1",384,150,100,5,"./assets/img/mechant_pc.png",1)
    monstre33_2 = enemy.Enemy("m33_2",768,150,100,5,"./assets/img/mechant_pc.png",1)
    monstre39 = enemy.Enemy("m39",512,300,100,5,"./assets/img/mechant_pc.png",1)
    monstre110_1 = enemy.Enemy("m110_1",850,400,100,5,"./assets/img/mechant_droit.png",4)
    monstre110_2 = enemy.Enemy("m110_2",100,300,100,5,"./assets/img/mechant_droit.png",4)
    monstre115_1 = enemy.Enemy("m115_1",220,224,100,5,"./assets/img/mechant_droit.png",4)
    monstre115_2 = enemy.Enemy("m115_2",700,224,100,5,"./assets/img/mechant_droit.png",4)
    monstres35_1 = enemy.Enemy("ms35_1",864,400,80,5,"./assets/img/monstre_projecteur_3.png",2)
    monstres35_2 = enemy.Enemy("ms35_2",864,220,80,5,"./assets/img/monstre_projecteur_1.png",2)
    monstres36_1 = enemy.Enemy("ms36_1",256,352,80,5,"./assets/img/monstre_projecteur_1.png",2)
    monstres36_2 = enemy.Enemy("ms36_2",704,320,80,5,"./assets/img/monstre_projecteur_2.png",2)
    monstres37_1 = enemy.Enemy("ms37_1",320,320,80,5,"./assets/img/monstre_projecteur_2.png",2)
    monstres37_2 = enemy.Enemy("ms37_2",800,224,80,5,"./assets/img/monstre_projecteur_1.png",2)
    boss = enemy.Enemy("boss",512,50,100,30,"./assets/img/monstre_amphi_1.png",3)
    iteration_img =0
    le_reveil = reveil.Reveil(544,64,"./assets/img/reveille_toiiii.png")







    # Création des salles
    amphiC1 = salle.Salle("amphiC1", character_obj,[], [], {"amphi" : (19*32, 7*32), "etage1" : (16*32, 15*32)})
    amphi = salle.Salle("amphi", character_obj, [], [], {"amphiC1" : (6*32, 20*32)})
    couloir1 = salle.Salle("couloir1", character_obj, [], [], {"salle33" : (10*32, 11*32), "salle39" : (25*32, 11*32), "sol" : (29*32, 12*32), "couloir2" : (4*32, 12*32)}) 
    couloir2 = salle.Salle("couloir2", character_obj, [], [], {"couloir3" : (4*32, 12*32), "sousSolCouloir1" : (20*32, 10*32), "couloir1" : (29*32, 12*32)})
    couloir3 = salle.Salle("couloir3", character_obj, [], [], {"salle21" : (18*32, 11*32), "couloir2" : (29*32, 12*32)})
    etage1Couoir1 = salle.Salle("etage1Couloir1", character_obj, [], [], {"etage1" : (4*32, 12*32), "salle110" : (10*32, 10*32), "salle115" : (25*32, 10*32)})
    etage1 = salle.Salle("etage1", character_obj, [], [], {"sol" : (10*32, 12*32), "amphiC1" : (24*32, 10*32), "etage1Couloir1" : (25*32, 17*32)})
    foodtruck = salle.Salle("foodtruck", character_obj, [], [], {"sol" : (22*32, 20*32), "sousSolCouloir2" : (5*32, 11*32)})
    salle21 = salle.Salle("salle21", character_obj, [], [], {"couloir3" : (16*32, 17*32)}, constants.COLLECTE_CLEE) 
    salle33 = salle.Salle("salle33", character_obj, [], [], {"couloir1" : (17*32, 17*32)})
    salle39 = salle.Salle("salle39", character_obj, [], [], {"couloir1" : (16*32, 17*32)})
    salle110 = salle.Salle("salle110", character_obj, [], [], {"etage1Couloir1" : (8*32, 19*32)})
    salle115 = salle.Salle("salle115", character_obj, [], [], {"etage1Couloir1" : (16*32, 19*32)}, constants.COLLECTE_CLEE)
    salleS35 = salle.Salle("salleS35", character_obj, [], [], {"sousSolCouloir2" : (14*32, 14*32)})
    salleS36 = salle.Salle("salleS36", character_obj, [], [], {"sousSolCouloir1" : (14*32, 18*32)})
    salleS37 = salle.Salle("salleS37", character_obj, [], [], {"sousSolCouloir3" : (24*32, 16*32)}, constants.COLLECTE_CLEE)
    sol = salle.Salle("sol", character_obj, [], [], {"couloir1" : (4*32, 14*32),"etage1" : (7*32, 9*32), "foodtruck" : (19*32, 9*32)})
    sousSolCouloir1 = salle.Salle("sousSolCouloir1", character_obj, [], [], {"sousSolCouloir2" : (4*32, 12*32), "couloir2" : (13*32, 10*32), "salleS36" : (25*32, 10*32), "sousSolCouloir3" : (29*32, 12*32)})
    sousSolCouloir2 = salle.Salle("sousSolCouloir2", character_obj, [], [], {"foodtruck" : (12*32, 10*32), "sousSolCouloir1" : (29*32, 12*32), "salleS35" : (18*32, 10*32)})
    sousSolCouloir3 = salle.Salle("sousSolCouloir3", character_obj, [], [], {"salleS37" : (11*32, 10*32), "sousSolCouloir1" : (4*32, 12*32)})

    room_list = {}
    for salle_item in [amphiC1, amphi, couloir1, couloir2, couloir3, etage1Couoir1, etage1, foodtruck, salle21, salle33, salle39, salle110, salle115, salleS35, salleS36, salleS37, sol, sousSolCouloir1, sousSolCouloir2, sousSolCouloir3]:
        room_list[salle_item.map] = salle_item
    #maj des salles



    salle21.enemies.append(monstre21)
    salle33.enemies.append(monstre33_1)
    salle33.enemies.append(monstre33_2)
    salle39.enemies.append(monstre39)
    salle110.enemies.append(monstre110_1)
    salle110.enemies.append(monstre110_2)
    salle115.enemies.append(monstre115_1)
    salle115.enemies.append(monstre115_2)
    salleS35.enemies.append(monstres35_1)
    salleS35.enemies.append(monstres35_2)
    salleS36.enemies.append(monstres36_1)
    salleS36.enemies.append(monstres36_2)
    salleS37.enemies.append(monstres37_1)
    salleS37.enemies.append(monstres37_2)
    amphi.enemies.append(boss)
    #pas supprimer!!
    current_room_obj=sol ## Salle de spawn



    
    tmx_map = pytmx.load_pygame('./assets/maps/' + current_room+".tmx")
    tmx_map_data = pytmx.TiledMap('./assets/maps/' + current_room+".tmx")

    
    

     # Chargement de la carte






    #musique
    pygame.mixer.init()
    pygame.mixer.music.load('./assets/music/intro_chill.mp3')
    pygame.mixer.music.play()

    


    while running:

        screen.fill((0, 0, 0))

        #ne pas activer le tire si aucun monstre
        # if len(current_room_obj.enemies)==0 and not there_is_monsters:
        #     tire = False

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
            char_rect = character_obj.get_rect()
            have_access=True
            #si le personnage n'as pas de clées, il ne peut pas aller au sous sol ou à l'etage.

            if constants.COLLECTE_CLEE:
                if character_obj.keys == 0 and coll[1] in [etage1.map, sousSolCouloir1.map, sousSolCouloir2.map, sousSolCouloir3.map, amphiC1.map]:
                    have_access=False

                    character_obj.move_down()
                    if coll[1] == etage1.map:
                        character_obj.move_right()
                    if coll[1] == sousSolCouloir1.map:
                         character_obj.move_down()
                         character_obj.move_down()
                         character_obj.move_down()
                    if coll[1] == sousSolCouloir2.map:
                         character_obj.move_right()

                    if coll[1] in [sousSolCouloir1.map, sousSolCouloir2.map, sousSolCouloir3.map]:
                        game_logic.affiche_dialogue(screen, "L'accès est bloqué. Il me faudrait une clé...")
                    else:
                        game_logic.affiche_dialogue(screen, "L'accès est bloqué. Il me faudrait deux clés...")

                

                if character_obj.keys == 1 and coll[1] in [etage1.map, amphiC1]:
                    have_access=False
                    character_obj.move_down()
                    character_obj.move_right()

                    game_logic.affiche_dialogue(screen, "L'accès est bloqué. Il me faudrait deux clés...")

                if character_obj.keys == 2 and coll[1] == amphiC1.map:
                    have_access=False
                    character_obj.move_down()
                    character_obj.move_right()

                    game_logic.affiche_dialogue(screen, "L'accès est bloqué. Il me faudrait deux clés...")

                if not deja_rentre_salle_pc and coll[1] in [salle33.map, salle39.map, salle21.map]:
                    affiche_dial_pc = True
                    deja_rentre_salle_pc = True

            if current_room != coll[1] and have_access:

                #repositionner le personnage
                next_room = room_list[coll[1]]
                print(next_room.map)
                char_rect.centerx = next_room.entry[current_room][0]
                char_rect.centery = next_room.entry[current_room][1]
                current_room = coll[1]

                #charger la map
                tmx_map = pytmx.load_pygame('./assets/maps/' + current_room + '.tmx')
                tmx_map_data = pytmx.TiledMap('./assets/maps/' + current_room + '.tmx')

                

                current_room_obj = next_room

                #verifier s'il doit y avoir des monstres
                if current_room_obj.enemies:
                     there_is_monsters=True


        
#-----------------------------------------------------------------------------------------------------------------affichage dialogue debut
        if temps==0 : #si toute premiere iteration boucle (debut du jeu)
            val=game_logic.affiche_dialogue(screen, "Aujourd'hui, c'est la rentrée, ma première journée à l'IUT. C'est tellement stressant... Mais tout devrait bien se passer. Tout de même, j'ai comme un mauvais pressentiment.")
            
        if temps==1:
            val=game_logic.affiche_dialogue(screen, "Pour vous déplacer, utilisez les touches Z, Q, S, D. Pour tirer, cliquez sur votre cible.")
        if temps==2:
            val=game_logic.affiche_dialogue(screen, "Attention : pour savoir quand tirer, tendez bien l'oreille !")

        if affiche_dial_pc:
            game_logic.affiche_dialogue(screen, "J'ai un mauvais pressentiment... Je devrais rester sur mes gardes.")
            affiche_dial_pc=False

#----------------------------------------------------------------------------------------------------------------afficher elements
        #coeurs
        character_obj.draw_hearts(screen)
        character_obj.draw_pieces(screen)
        if constants.COLLECTE_CLEE:
            character_obj.draw_keys(screen)

        #personnage
        game_logic.move_character(screen,character_obj, pygame.key.get_pressed(), tmx_map_data)
        character_obj.draw(screen)

#------------------------------------------------------------------------------------------------------------------- event handler
        for event in pygame.event.get():

            # fermer la fenetre
            if event.type == pygame.QUIT:
                running = False
                bonus = 0
                if character_obj.boss_defeated:
                    bonus=50
                game_logic.set_score(pseudo, character_obj.pieces*5 + character_obj.keys*15 + bonus)

            #gestion du tire 
            if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1 and tire and len(character_obj.get_proj())<5:
                
                mouse_x, mouse_y = event.pos
                character_obj.add_proj(game_logic.tirer(character_obj.get_centre_x(),character_obj.get_centre_y(),mouse_x,mouse_y,screen,"./assets/img/note_tire.png", True))
                tire = False
                while(delay<1.0):
                    delay += 1/60
                    tire = True
                delay=0
            
            if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                 game_logic.affiche_pause(screen, character_obj)

#---------------------------------------------------------------------------------------------------------------gestion du jeu (monstre, piece, projectile)
        # Liste des indices des projectiles à supprimer
        indices_proj_a_supprimer = []
        indices_proj_a_supprimer = game_logic.impact_handler(character_obj, current_room_obj.pieces, current_room_obj.enemies, tmx_map_data, indices_proj_a_supprimer)        
        indices_proj_a_supprimer = game_logic.coin_handler(character_obj, current_room_obj.pieces, screen, indices_proj_a_supprimer)

        #-------------------------------------------------------------------------------------------------attaque (projectiles) des monstres et affichage
        
        if there_is_monsters:
            for monstre in current_room_obj.enemies:
                current_time = time.time()
                if monstre.premier_tire:
                    monstre.last_shot_time = current_time -1.0
                    monstre.premier_tire = False
                if monstre.attaque ==1:   
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
                elif monstre.attaque==2:
                    # Vérifiez si suffisamment de temps s'est écoulé depuis le dernier tir
                    if current_time - monstre.last_shot_time >= 1.5:
                        # Permet à l'ennemi de tirer un projectile
                        monstre.add_proj(game_logic.tirer(monstre.get_centre_x(), monstre.get_centre_y(), character_obj.get_centre_x(), character_obj.get_centre_y(), screen, "./assets/img/tir_projecteur.png"))
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
                elif monstre.attaque==4:
                    # Vérifiez si suffisamment de temps s'est écoulé depuis le dernier tir
                    if current_time - monstre.last_shot_time >= 1.0 and monstre.get_centre_x() < character_obj.get_centre_x():
                        # Permet à l'ennemi de tirer un projectile
                        monstre.add_proj(game_logic.tirer(monstre.get_centre_x(), monstre.get_centre_y(), character_obj.get_centre_x(), character_obj.get_centre_y(), screen, "./assets/img/tir-livre.png"))
                        monstre.last_shot_time = current_time  # Mettez à jour le temps du dernier tir
                    elif current_time - monstre.last_shot_time >= 1.0:
                        monstre.add_proj(game_logic.tirer(monstre.get_centre_x(), monstre.get_centre_y(), character_obj.get_centre_x(), character_obj.get_centre_y(), screen, "./assets/img/tir-livre_retourne.png"))
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
                else:
                    if monstre.hp>0:
                        monstre.update(50,864,576,864,576,192,50,192)

                        if monstre.hp<=20:
                            monstre.set_img("./assets/img/monstre_amphi_5.png") 
                            monstre.speed = 5
                        if monstre.hp <=10:
                            monstre.speed = 7
                            monstre.set_img("./assets/img/monstre_amphi_6.png")

                        # Vérifiez si suffisamment de temps s'est écoulé depuis le dernier tir
                        if current_time - monstre.last_shot_time >= 2.0 and monstre.hp>20 or current_time - monstre.last_shot_time >= 0.5 and monstre.hp<20 and monstre.hp>=1:
                            # Permet à l'ennemi de tirer un projectile
                            if monstre.hp>10:
                                monstre.add_proj(game_logic.tirer(monstre.get_centre_x(), monstre.get_centre_y(), character_obj.get_centre_x(), character_obj.get_centre_y(), screen, "./assets/img/tir_micro_1.png"))
                                monstre.last_shot_time = current_time  # Mettez à jour le temps du dernier tir
                            else:
                                monstre.add_proj(game_logic.tirer(monstre.get_centre_x(), monstre.get_centre_y(), character_obj.get_centre_x(), character_obj.get_centre_y(), screen, "./assets/img/tir_micro_1.png"))
                                monstre.add_proj(game_logic.tirer(monstre.get_centre_x(), monstre.get_centre_y(), 928, 96, screen, "./assets/img/tir_micro_1.png"))
                                monstre.add_proj(game_logic.tirer(monstre.get_centre_x(), monstre.get_centre_y(), 928, 576, screen, "./assets/img/tir_micro_1.png"))
                                monstre.add_proj(game_logic.tirer(monstre.get_centre_x(), monstre.get_centre_y(), 192, 576, screen, "./assets/img/tir_micro_1.png"))
                                monstre.add_proj(game_logic.tirer(monstre.get_centre_x(), monstre.get_centre_y(), 192, 96, screen, "./assets/img/tir_micro_1.png"))
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
                    else:
                        character_obj.boss_defeated = True
                        current_time = time.time()
                        if current_time - monstre.last_img_time >= 2.0 and iteration_img==0:
                            monstre.set_img("./assets/img/monstre_amphi_5.png")
                            iteration_img+=1
                            monstre.last_img_time = current_time
                        elif iteration_img==0:
                            monstre.draw_dead(screen)
                        elif current_time - monstre.last_img_time >= 2.0 and iteration_img==1:
                            monstre.set_img("./assets/img/mort1_micro.png")
                            monstre.last_img_time = current_time
                            iteration_img+=1
                        elif iteration_img==1:
                            monstre.draw_dead(screen)
                        elif current_time - monstre.last_img_time >= 2.0 and iteration_img==2:
                            monstre.set_img("./assets/img/mort2_micro.png")
                            monstre.last_img_time = current_time
                            iteration_img+=1
                        elif iteration_img==2:
                            monstre.draw_dead(screen)   
                        elif iteration_img==3:
                            le_reveil.draw(screen)
                            monstre.draw_dead(screen)   
                            game_logic.play_sound("son_reveil")
                            game_logic.affiche_dialogue(screen,"oh, un reveil ? qu'est ce que c'est que ca ?")
                            iteration_img = iteration_img+1
                        elif iteration_img ==4:
                                monstre.draw_dead(screen)   
                                le_reveil.draw(screen)
                                if le_reveil.check_collision(character_obj):
                                    game_logic.affiche_dialogue(screen,"woaaaaaah")
                                    iteration_img +=1
                        elif iteration_img==5:
                                    character_obj.rect.x = 320
                                    character_obj.rect.y = 320
                                    iteration_img +=1
                                    tmx_map = pytmx.load_pygame('./assets/maps/' + 'chambre' + '.tmx')
                                    tmx_map_data = pytmx.TiledMap('./assets/maps/' + 'chambre' + '.tmx')
                                    coll = game_logic.check_collision(character_obj.get_rect(), tmx_map_data)
                                    if 3 in coll:
                                        running=False
                                        bonus = 0
                                        if character_obj.boss_defeated:
                                            bonus=50
                                        game_logic.set_score(character_obj.pseudo, character_obj.pieces*5 + character_obj.keys*15 + bonus)
                                        pygame.mixer.music.load('./assets/music/menu.mp3')
                                        pygame.mixer.music.play()
                                        credit.ouvrir_credit(screens)
                        elif iteration_img==6:
                            iteration_img +=1
                            pygame.mixer.music.load('./assets/music/music_fin.mp3')
                            pygame.mixer.music.play()
                            game_logic.affiche_dialogue(screen,"Ouf, ce n'était qu'un cauchemar...")


                                    



            for monstre in current_room_obj.enemies:
                monstre.draw(screen)  # Dessinez le monstre à l'écran

            #gestion des degats que fonts les projectiles :
            for monstre in current_room_obj.enemies:
                if(len(monstre.get_proj())>0):
                    for proj in monstre.get_proj():
                        rectangle = character_obj.rect
                        rectangle1 = game_logic.get_next_rect(rectangle, 'u')
                        rectangle2 = game_logic.get_next_rect(rectangle, 'd')
                        rectangle3 = game_logic.get_next_rect(rectangle, 'l')
                        rectangle4 = game_logic.get_next_rect(rectangle, 'r')
                        if (proj.rect.colliderect(rectangle) or proj.rect.colliderect(rectangle1) or proj.rect.colliderect(rectangle2) or proj.rect.colliderect(rectangle3) or proj.rect.colliderect(rectangle4)) and monstre.hp>0 :
                            character_obj.take_damage(1)
                            character_obj.update()
                if character_obj.get_rect().colliderect(monstre.rect) and monstre.hp>0:
                    character_obj.take_damage(1)
                    character_obj.update()
                if not character_obj.is_alive():
                    # Le personnage est mort, vous pouvez gérer la fin du jeu ou d'autres actions appropriées
                    running = False
                    pygame.mixer.music.stop
                    pygame.mixer.music.load('./assets/music/menu.mp3')
                    pygame.mixer.music.play()
                    game_logic.play_sound("gameOver")
                    bonus = 0
                    if character_obj.boss_defeated:
                        bonus=50
                    game_logic.set_score(pseudo, character_obj.pieces*5 + character_obj.keys*15 + bonus)
                    screens.game_over.ouvrir_game_over(screen)

        #affiche la clee (s'il y en a une)
        if current_room_obj.key:
            
            if current_room == "salle21" and len(current_room_obj.enemies)==0:
                 key_obj.rect.centerx=16*32
                 key_obj.rect.centery=6*32
            elif current_room == "salleS37"and len(current_room_obj.enemies)==0:
                 key_obj.rect.centerx=10*32
                 key_obj.rect.centery=10*32
            elif current_room == "salle115"and len(current_room_obj.enemies)==0 :
                 key_obj.rect.centerx=16*32
                 key_obj.rect.centery=16*32
            if len(current_room_obj.enemies)==0:
                key_obj.draw(screen)

            if character_obj.get_rect().colliderect(key_obj.get_rect()):
                current_room_obj.key=False
                character_obj.increase_keys()


        


        # Comme les dessins sont faits dans un buffer, permute le buffer
        pygame.display.flip()
        # Limite le frame rate à 60 images par seconde et retourne le temps réel passé
        dt = clock.tick(60) 
        temps += 1

    # Termine proprement le module
    pygame.quit()
