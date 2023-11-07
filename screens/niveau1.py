import pygame
import character
import screens.error as error
import pytmx
import game_logic

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
    tmx_map = pytmx.load_pygame('./assets/maps/couloir1.tmx')
    tmx_map_data = pytmx.TiledMap('./assets/maps/couloir1.tmx')
    game_logic.check_collision(character_obj.get_x(), character_obj.get_y(), tmx_map_data)

    while running:

        screen.fill((0, 0, 0))
         
        

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

                
        
        
        # Affiche le personnage
        #character_obj.inputs(pygame.key.get_pressed())
        game_logic.move_character(character_obj, pygame.key.get_pressed(), tmx_map)
        character_obj.draw(screen)
       
        # Comme les dessins sont faits dans un buffer, permute le buffer
        pygame.display.flip()
        # Limite le frame rate à 60 images par seconde et retourne le temps réel passé
        dt = clock.tick(60) 

    # Termine proprement le module
    pygame.quit()


