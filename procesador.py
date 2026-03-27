import time
import schedule # Necesitás: pip install schedule
from procesador import calcular_y_guardar # Reutilizamos tu lógica anterior

def tarea_diaria():
    print(f"🕒 [{datetime.now()}] Iniciando escaneo de canales...")
    try:
        calcular_y_guardar()
        print("✅ Escaneo completado con éxito.")
    except Exception as e:
        print(f"❌ Error en el escaneo: {e}")

# Programamos para que corra cada 1 hora
schedule.every(1).hours.do(tarea_diaria)

print("🚀 Scraper 24/7 Iniciado. No cierres esta terminal.")

while True:
    schedule.run_pending()
    time.sleep(60) # Revisa cada minuto si hay tareas pendientes
