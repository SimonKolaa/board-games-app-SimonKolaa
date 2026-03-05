import sqlite3
import os

# Creiamo la cartella instance dentro video-app
if not os.path.exists("video-app/instance"):
    os.makedirs("video-app/instance")

db_path = os.path.join("video-app/instance", "board_games.sqlite")

# Ci connettiamo (se il file non esiste, lo crea)
connection = sqlite3.connect(db_path)

# Leggiamo lo schema SQL
with open("video-app/app/schema.sql") as f:
    connection.executescript(f.read())

print("Database creato con successo in:", db_path)
connection.close()