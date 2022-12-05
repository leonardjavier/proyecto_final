import sqlite3 as sql

def creaDB ():
    try:
      conn = sql.connect("Restaurantes.db")
      conn.commit()
      conn.close()

    except Exception as e:
        print(f"A ocurrido un error: {e}")
  

if __name__ == "__main__":
    creaDB()

