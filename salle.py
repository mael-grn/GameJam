import pyymx
import character
import piece
import enemy

class Salle:
    def __init__(self, tmx_file, character, enemies, pieces):
        self.map = tmx_file  
        self.character = character
        self.enemies = enemies 
        self.pieces = pieces   

        # Charger la carte depuis le fichier TMX
        tmx_data = pytmx.TiledMap(tmx_file)
        self.map_data = tmx_data




        

    



    
