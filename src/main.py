from sniffer import start_sniffing
from analyzer import DetectionEngine
from alerts import log_alert  # <--- Nueva importación
from scapy.all import IP

engine = DetectionEngine(threshold=10, window=5)

def process_packet(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        
        if engine.is_suspicious(src_ip):
            message = f"Superó el umbral de {engine.threshold} paquetes en {engine.window}s"
            print(f"\n[!!!] ALERTA: Actividad sospechosa detectada desde {src_ip}")
            
            # Llamamos a la función de logging
            log_alert(src_ip, message)

if __name__ == "__main__":
    try:
        print("--- SENTINEL-WATCH V1.0 INICIADO ---")
        start_sniffing(process_packet)
    except KeyboardInterrupt:
        print("\n[!] Apagando Sentinel-Watch. ¡Pura vida!")