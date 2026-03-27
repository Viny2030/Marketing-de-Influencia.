import yt_dlp
import time
from datetime import datetime
from database import conectar_db # Tu conexión a Docker

def obtener_datos_video(url_video):
    ydl_opts = {'quiet': True, 'no_warnings': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url_video, download=False)
        return {
            "influencer": info.get('uploader'),
            "titulo": info.get('title'),
            "fecha_pub": info.get('upload_date'),
            "timestamp": info.get('timestamp') 
        }

def scraper_continuo():
    print("🚀 Scraper 24/7 activado. Monitoreando links.txt...")
    while True:
        try:
            # 1. Leer los links que pusiste en el archivo
            with open('links.txt', 'r') as f:
                links = [line.strip() for line in f if line.strip()]

            for link in links:
                datos = obtener_datos_video(link)
                # 2. Aquí iría tu lógica de 'calcular_atribucion' que ya hicimos
                # 3. Guardar en la base de datos de Docker
                print(f"✅ [{datetime.now().strftime('%H:%M:%S')}] Procesado: {datos['influencer']}")
            
            print("💤 Durmiendo 1 hora hasta la próxima revisión...")
            time.sleep(3600) # Espera 1 hora (3600 segundos)
            
        except Exception as e:
            print(f"❌ Error en el ciclo: {e}")
            time.sleep(60) # Si falla, reintenta en 1 minuto

if __name__ == "__main__":
    scraper_continuo()
