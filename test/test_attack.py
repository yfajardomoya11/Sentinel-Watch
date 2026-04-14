from scapy.all import IP, TCP, send
import time

target_ip = "127.0.0.1" # Tu propia máquina

print(f"[*] Iniciando simulacro de escaneo hacia {target_ip}...")

for port in range(1, 25):
    # Enviamos un paquete TCP a cada puerto
    packet = IP(dst=target_ip)/TCP(dport=port, flags="S")
    send(packet, verbose=False)
    print(f"[+] Paquete enviado al puerto: {port}")
    time.sleep(0.1) # Pequeña pausa

print("[*] Simulacro terminado. Revisa la terminal de Sentinel-Watch.")