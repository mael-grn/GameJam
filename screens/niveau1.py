import pygame
import character
import screens.error as error
import pytmx
import game_logic
import enemy
import screens.game_over

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
    projectiles = []
    tmx_map_data = pytmx.TiledMap('./assets/maps/sol.tmx')
    
    monstres = []  # Créez une liste vide pour stocker les monstres
   
    monstre1 = enemy.Enemy("Monstre1", 200, 200, 100, 10, "./assets/img/mechant_pc.png")
    monstre2 = enemy.Enemy("Monstre2", 300, 300, 100, 10, "./assets/img/mechant_pc.png")
    monstre3 = enemy.Enemy("Monstre3", 400, 400, 100, 10, "./assets/img/mechant_pc.png")
    monstres.append(monstre1)
    monstres.append(monstre2)
    monstres.append(monstre3)

    pygame.mixer.init()
    pygame.mixer.music.load('./assets/music/intro_chill.mp3')
    pygame.mixer.music.play()

    while running:
        screen.fill((0, 0, 0))
        if pygame.mixer.music.get_busy() == 0:  # La musique s'est terminée
                pygame.mixer.music.load('./assets/music/combat.mp3')
                pygame.mixer.music.play()
       #affichage de la carte
        for layer in tmx_map.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, image in layer.tiles():
                    screen.blit(image, (x * tmx_map.tilewidth, y * tmx_map.tileheight))

        # Parcourt tous les événements pour les traiter
        for event in pygame.event.get():
            # QUIT signifie que l'utilisateur a fermé la fenêtre
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
                mouse_x, mouse_y = event.pos
                projectiles.append(game_logic.tirer(character_obj.get_centre_x(), character_obj.get_centre_y(), mouse_x, mouse_y, screen))
        
        for proj in projectiles:
            proj.update()        
             
            for monstre in monstres:
                if proj.rect.colliderect(monstre.rect):
                    monstre.take_damage(1)  # Chaque projectile inflige 1 point de dégât
                    if not monstre.is_alive():
                        monstres.remove(monstre)  # Supprimez l'ennemi s'il n'a plus de points de vie
                    projectiles.remove(proj)  # Supprimez le projectile s'il touche un ennemi
                    break  # Sortez de la boucle des ennemis, car le projectile a déjà touché un ennemi
            proj.draw(screen)    

        for monstre in monstres:
            monstre.draw(screen)  

        character_rect = character_obj.get_rect()
        for monstre in monstres:
            if character_rect.colliderect(monstre.rect):
                character_obj.take_damage(1)  # Le personnage perd 1 point de vie en cas de collision
                if not character_obj.is_alive():
                    # Le personnage est mort, vous pouvez gérer la fin du jeu ou d'autres actions appropriées
                    running = False
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
