import time
from collections import defaultdict

class DetectionEngine:
    def __init__(self, threshold=15, window=10):
        self.threshold = threshold  # Máximo de intentos permitidos
        self.window = window        # Tiempo en segundos
        self.history = defaultdict(list)
        self.detected_ips = set()

    def is_suspicious(self, ip):
        current_time = time.time()
        
        # Registramos el timestamp del paquete actual para esa IP
        self.history[ip].append(current_time)

        # Limpiamos registros viejos que ya pasaron la ventana de tiempo
        self.history[ip] = [t for t in self.history[ip] if current_time - t <= self.window]

        # Si supera el umbral y no la hemos alertado ya, disparamos
        if len(self.history[ip]) > self.threshold:
            if ip not in self.detected_ips:
                self.detected_ips.add(ip)
                return True
        return False