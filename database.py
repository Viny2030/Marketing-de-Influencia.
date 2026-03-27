import psycopg2
import os
import time

def conectar_db():
    # Datos que coinciden con tu docker-compose.yml
    try:
        conn = psycopg2.connect(
            dbname='marketing_atribucion',
            user='user_marketing',
            password='password_influencia',
            host='localhost',
            port='5432'
        )
        return conn
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        return None

def crear_tablas():
    conn = conectar_db()
    if conn:
        cur = conn.cursor()
        # Tabla para registrar cada posteo de influencer y su ROI
        cur.execute("""
            CREATE TABLE IF NOT EXISTS campanas (
                id SERIAL PRIMARY KEY,
                influencer VARCHAR(255),
                url_video TEXT,
                fecha_pub TIMESTAMP,
                ventas_atribuidas INTEGER,
                monto_total FLOAT,
                fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        conn.commit()
        cur.close()
        conn.close()
        print("✅ Estructura de base de datos (Tablas) lista en Docker.")

if __name__ == "__main__":
    # Damos 2 segundos por si el docker está arrancando
    time.sleep(2)
    crear_tablas()
