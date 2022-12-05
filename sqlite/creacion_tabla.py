import sqlite3 as sql

def CreacionTabla () :
    try:
        conn = sql.connect("Restaurantes.db")
        cursor = conn.cursor()
        cursor.execute(
            """CREATE TABLE Restaurantes(
                userID text,
                smoker blob,
                dress_preference text,
                drink_level text,
                birth_year integer,
                activity text,
                color text, 
                budget text,
                height integer,
                latitude real,
                longitude real
            )
            """
        )
    except Exception as e:
        print(f"Se ha produciodo un error: {e}")
        conn.close()
    conn.commit()
    conn.close()


if __name__ == "__main__":
    CreacionTabla ()

