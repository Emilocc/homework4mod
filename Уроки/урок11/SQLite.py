import sqlite3
from dataclasses import dataclass

@dataclass()
class User:
    name: str
    age:int
    gender: str



# class User:
#     def __int__(self,name: str, age: int, gender: str):
#         self.name = name
#         self.age = age
#         self.gender = gender



# try:
#     connection = sqlite3.connect('sqlite.db')
# except sqlite3.DatabaseError:
#     print("Eror404")
#
# finally:
#     connection.close()
#
def create_user_table(cur: sqlite3.Cursor):
    command = """"
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age TEXT,
    gender TEXT)
    
    """
    cur.execute(command)

def add_user(cur: sqlite3.Cursor,user: User):
    command = """"
    INSERT INTO users(name, age, gender) VALUES(?,?,?)
    """
    cur.execute(command,(user.name,user.age,user.gender))


if __name__ == '__main__':
    with sqlite3.connect('sqlite.db') as connection:
        cursor = connection.cursor()
        create_user_table(cursor)
        Emil = User(name="Emil",age=16,gender="М")
        irina = User(name="irina",age=17,gender="Ж")
        add_user(cursor, Emil)
        add_user(cursor, irina)

