import sqlite3

class Bdd:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("./bdd/BDD.db")
    
    def open_cursor(self):
        return self.connection.cursor()
    
    def close_cursor(self, cursor):
        cursor.close()
    
    def close_bdd(self):
        self.connection.close()

    def create_player(self, pseudo, character):
        cursor = self.open_cursor()
        request = f"INSERT INTO Player VALUES (?,?);"
        cursor.execute(request, (pseudo, character))
        self.connection.commit()
        self.close_cursor(cursor) 
    
    def create_party(self, player, timer, level, map):
        cursor = self.open_cursor()
        request = f"INSERT INTO Party VALUES (?,?,?,?);"
        cursor.execute(request, (player, timer, level, map))
        self.connection.commit()
        self.close_cursor(cursor)
    
    def get_player(self, pseudo):
        cursor = self.open_cursor()
        request = f"SELECT * FROM Player WHERE pseudo = ?;"
        cursor.execute(request, (pseudo,))
        value = cursor.fetchone()
        self.close_cursor(cursor)
        dicto = {"pseudo": value[0], "character": value[1]}
        return dicto
    
    def get_party(self, pseudo):
        cursor = self.open_cursor()
        request = f"SELECT * FROM Party WHERE player = ?;"
        cursor.execute(request, (pseudo,))
        value = cursor.fetchone()
        self.close_cursor(cursor)
        dicto = {"pseudo": value[0], "timer": value[1], "level": value[2], "map": value[3]}
        return dicto
    
    def update_party(self, timer=None, level=None, map=None):
        pass
    

    
    