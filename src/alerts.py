import datetime
import os

LOG_FILE = "logs/sentinel.log"

def log_alert(ip, reason):
    # Asegurarnos de que la carpeta existe
    if not os.path.exists('logs'):
        os.makedirs('logs')
        
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] ALERTA: IP {ip} - {reason}\n"
    
    # Añadimos el parámetro buffering=1 o hacemos flush
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry)
        f.flush() # <--- Esto obliga a Windows a escribir el archivo YA
    
    print(f"--- Evidencia guardada físicamente en {LOG_FILE} ---")