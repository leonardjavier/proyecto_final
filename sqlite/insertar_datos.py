import sqlite3 as sql

def Insertar (df):
    try:
        conn = sql.connect("Restaurantes.db")
        df.to_sql("Restaurantes", conn , if_exists="replace")
    except Exception as e:
        print(f"Se ha producido un error: {e}")
        conn.close()
    conn.commit()
    conn.close()
    
