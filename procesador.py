import pandas as pd
from database import conectar_db

def guardar_atribucion(influencer, url, fecha, ventas, monto):
    conn = conectar_db()
    if conn:
        cur = conn.cursor()
        query = """
            INSERT INTO campanas (influencer, url_video, fecha_pub, ventas_atribuidas, monto_total)
            VALUES (%s, %s, %s, %s, %s)
        """
        cur.execute(query, (influencer, url, fecha, ventas, monto))
        conn.commit()
        cur.close()
        conn.close()
        print(f"💾 ¡Datos guardados en DB para {influencer}!")

# Simulación de proceso
if __name__ == "__main__":
    print("🤖 Procesador de Atribución v2.0")
    # Aquí iría tu lógica de yt-dlp y cruce de ventas
    # Ejemplo de guardado manual para probar:
    guardar_atribucion("Influencer_Test", "https://youtube.com/watch?v=123", "2026-03-27 10:00:00", 5, 1500.50)
