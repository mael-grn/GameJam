import pytmx
import character
import piece
import enemy

class Salle:
    def __init__(self, tmx_file, character, enemies, pieces, entry, key=False):
        self.map = tmx_file  
        self.entry = entry
        self.character = character
        self.enemies = enemies 
        self.pieces = pieces   

        self.key = key






    



    
