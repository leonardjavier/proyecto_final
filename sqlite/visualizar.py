import sqlite3 as sql 

def VerTabla () :
    conn = sql.connect("Restaurantes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Restaurantes")
    datos = cursor.fetchall()
    conn.commit()
    conn.close()

    for lista in datos:
        print(lista)

if __name__ == "__main__":
    VerTabla()