import pygame
import character
import screens.error as error
import pytmx
import game_logic
import enemy
import screens.game_over
import time
import piece

def ouvrir_niveau(screen):
    # Définit l'horloge pour connaître le temps qui a passé
    clock = pygame.time.Clock()
    # Pour savoir quand la boucle du jeu se termine
    running = True
    # Le temps passé entre deux rafraîchissements de l'écran en millisecondes
    dt = 0

    # Crée un personnage
    character_obj = character.Character(640, 360)  # Position initiale du personnage

     # Chargement de la carte
    tmx_map = pytmx.load_pygame('./assets/maps/sol.tmx')
    tmx_map_data = pytmx.TiledMap('./assets/maps/sol.tmx')

    i=0
    ind_proj_char =0
    projectiles = []
    min_proj_count = 5  # Initialisation à une valeur infinie
    monstre_a_tirer = None
    delay =0
    monstres = []  # Créez une liste vide pour stocker les monstres
    projectilesMonstres = [] #crée liste pour projectiles monstres
    monstre1 = enemy.Enemy("Monstre1", 200, 200, 100, 10, "./assets/img/mechant_pc.png")
    monstre2 = enemy.Enemy("Monstre2", 300, 300, 100, 10, "./assets/img/mechant_pc.png")
    monstre3 = enemy.Enemy("Monstre3", 400, 400, 100, 10, "./assets/img/mechant_pc.png")
    monstres.append(monstre1)
    monstres.append(monstre2)
    monstres.append(monstre3)
    pieces=[]
    tire = False
    pygame.mixer.init()
    pygame.mixer.music.load('./assets/music/intro_chill.mp3')
    pygame.mixer.music.play()

    while running:
        screen.fill((0, 0, 0))
        if len(monstres)==0:
            tire = False
        if pygame.mixer.music.get_busy() == 0:  # La musique s'est terminée
                if(tire):
                    pygame.mixer.music.load('./assets/music/intro_chill.mp3')
                    pygame.mixer.music.play()
                    tire = False
                else:
                    pygame.mixer.music.load('./assets/music/combat.mp3')
                    pygame.mixer.music.play()
                    tire = True
       #affichage de la carte
        for layer in tmx_map.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, image in layer.tiles():
                    screen.blit(image, (x * tmx_map.tilewidth, y * tmx_map.tileheight))

        character_obj.draw_hearts(screen)

        # Parcourt tous les événements pour les traiter
        for event in pygame.event.get():
            # QUIT signifie que l'utilisateur a fermé la fenêtrez
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1 and tire:
                mouse_x, mouse_y = event.pos
                character_obj.add_proj(game_logic.tirer(character_obj.get_centre_x(),character_obj.get_centre_y(),mouse_x,mouse_y,screen,"./assets/img/note_tire.png"))
        # Liste des indices des projectiles à supprimer
        indices_proj_a_supprimer = []

        # Parcourez les projectiles de character_obj
        for index, proj in enumerate(character_obj.get_proj()):
            proj.update()
            
            # Parcourez les monstres
            for monstre in monstres:
                rectangle = pygame.Rect(proj.get_x(),proj.get_y(),50,50)
                if proj.rect.colliderect(monstre.rect):
                    monstre.take_damage(1)  # Chaque projectile inflige 1 point de dégât
                    if not monstre.is_alive():
                        une_piece=piece.Piece(monstre.rect.x, monstre.rect.y, "./assets/img/piece.png", "./assets/img/pieceReverse.png")
                        pieces.append(une_piece)
                        monstres.remove(monstre)  # Supprimez l'ennemi s'il n'a plus de points de vie
                    # indices_proj_a_supprimer.append(index)  # Ajoutez l'index du projectile à supprimer à la liste
                    break  # Sortez de la boucle des ennemis, car le projectile a déjà touché un ennemi
        if len(pieces)>0:
            for piece_obj in pieces:
                piece_obj.draw(screen)
            
        if proj.rect.colliderect(monstre.rect) or game_logic.check_collision(rectangle,tmx_map_data):
            indices_proj_a_supprimer.append(index)  # Ajoutez l'index du projectile à supprimer à la liste


        # Supprimez les projectiles de character_obj à partir de la fin pour éviter les problèmes d'index
        indices_proj_a_supprimer.reverse()  # Inversez la liste des indices
        for index in indices_proj_a_supprimer:
            character_obj.del_proj(index)

        # Affichez les projectiles restants
        for proj in character_obj.get_proj():
            proj.draw(screen)
        


        for monstre in monstres:
            num_proj =0
            delay += 1/60
            if (len(monstre.get_proj())<3 and delay>=1):
                monstre.add_proj(game_logic.tirer(monstre.get_centre_x(),monstre.get_centre_y(),character_obj.get_centre_x(),character_obj.get_centre_y(),screen, "./assets/img/tir_pc.png"))
                delay=0
            if(len(monstre.get_proj())>0):
                for proj in monstre.get_proj():
                    rectangle = pygame.Rect(proj.get_x(),proj.get_y(),50,50)
                    if proj.rect.colliderect(character_obj.rect) or game_logic.check_collision(rectangle,tmx_map_data):
                        monstre.del_proj(num_proj)  # Supprimez le projectile s'il touche un ennemi
                    proj.update()
                    proj.draw(screen)
                    num_proj = num_proj+1   
        
        for monstre in monstres:
            monstre.draw(screen)  # Dessinez le monstre à l'écran

        character_rect = character_obj.get_rect()
        for monstre in monstres:
            if(len(monstre.get_proj())>0):
                for proj in monstre.get_proj():
                    if proj.rect.colliderect(character_obj.rect):
                        character_obj.take_damage(1)
                        character_obj.update()
            if character_rect.colliderect(monstre.rect):
                character_obj.take_damage(1)
                character_obj.update()
            if not character_obj.is_alive():
                # Le personnage est mort, vous pouvez gérer la fin du jeu ou d'autres actions appropriées
                running = False
                pygame.mixer.music.stop
                pygame.mixer.music.load('./assets/music/menu.mp3')
                pygame.mixer.music.play()
                screens.game_over.ouvrir_game_over(screen)

        # Affiche le personnage
        game_logic.move_character(character_obj, pygame.key.get_pressed(), tmx_map_data)
        character_obj.draw(screen)
        # Comme les dessins sont faits dans un buffer, permute le buffer
        pygame.display.flip()
        # Limite le frame rate à 60 images par seconde et retourne le temps réel passé
        dt = clock.tick(60) 

    # Termine proprement le module
    pygame.quit()
